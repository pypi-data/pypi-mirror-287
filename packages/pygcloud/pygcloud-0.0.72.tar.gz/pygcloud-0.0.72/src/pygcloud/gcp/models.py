"""
Data models related to GCP services

@author: jldupont
"""

from typing import List, Dict
from dataclasses import dataclass, field
from pygcloud.utils import JsonObject
from pygcloud.utils import FlexJSONEncoder


class Spec:

    def __post_init__(self):
        """
        Helper for typical URI type name i.e.

        projects/PROJECT/locations/LOCATION/RESOURCE/id
        """
        if not getattr(self, "name", False):
            return

        parts = self.name.split("/")
        if len(parts) != 6:
            self.name = parts[-1]
            return

        self.location = parts[3]
        self.name = parts[-1]

    @classmethod
    def parse_json(cls, json_str: str) -> dict:
        import json

        try:
            json_obj = json.loads(json_str)
        except Exception:
            raise ValueError(f"Cannot parse for JSON: {json_str}")

        return json_obj

    @classmethod
    def from_obj(cls, obj):
        """
        This recursively builds a class instance
        based on the annotations
        """

        if isinstance(obj, list):
            return [cls.from_obj(item) for item in obj]

        if not isinstance(obj, dict):
            return obj

        import typing

        fields = cls.__annotations__

        result: dict = {}  # type: ignore

        for key, value in obj.items():

            _field = fields.get(key, None)
            if _field is None:
                continue

            origin = typing.get_origin(_field)

            if origin != list:
                result[key] = value
                continue

            # we are just dealing with the simplest case
            # ... at least for now e.g.
            # List[BackendGroup]
            #
            # and not something like:
            # List[Union[...]]
            classe = typing.get_args(_field)[0]

            # print(f"Key = {key}, origin={origin}, classe={classe.__name__}, value={value}")

            if hasattr(classe, "from_obj"):
                entries = classe.from_obj(value)
            else:
                entries = value

            result[key] = entries

        return cls(**result)

    @classmethod
    def from_string(cls, json_str: str):
        """
        Create a dataclass from a JSON string
        Make sure to only include fields declare
        in the dataclass
        """
        obj = cls.parse_json(json_str)
        return cls.from_obj(obj)

    @classmethod
    def from_json_list(cls, json_str: str, path: str = None):
        """
        Excepts to parse a JSON list from the specified string.
        An optional 'path' can be specified i.e. key to reach list.
        """
        assert isinstance(json_str, str)

        import json

        try:
            json_list = json.loads(json_str)
        except Exception as e:
            raise Exception(f"Error trying to load list from JSON string: {e}")

        if path is not None:
            json_list = json_list.get(path, [])

        assert isinstance(json_list, list)

        return [cls.from_obj(obj) for obj in json_list]

    def to_dict(self):
        result = {}

        fields = self.__annotations__

        for _field in fields:
            value = getattr(self, _field)

            if hasattr(value, "to_dict"):
                value = value.to_dict()

            result[_field] = value

        return result

    def to_json_string(self):
        import json

        return json.dumps(self.to_dict(), cls=FlexJSONEncoder)


@dataclass
class ProjectDescription(Spec):
    name: str
    projectId: str
    projectNumber: str
    lifecycleState: str
    parent: dict


@dataclass
class ServiceDescription(Spec):
    """
    A service description as retrieved through
    `gcloud services list --enabled`
    """

    name: str
    state: str
    parent: str
    project_number: int = 0
    api: str = "???"

    def __post_init__(self):
        parts = self.name.split("/")
        self.project_number = parts[1]
        self.api = parts[-1]


@dataclass
class IAMBinding(Spec):
    """
    By default, if the 'email' does not
    contain a namespace prefix, it will be
    set to "serviceAccount"
    """

    email: str
    role: str
    ns: str = field(default=None)

    def __post_init__(self):
        if self.ns is not None:
            return

        maybe_split = self.email.split(":")
        if len(maybe_split) == 2:
            self.ns = maybe_split[0]
            self.email = maybe_split[1]
        else:
            self.ns = "serviceAccount"

    @property
    def sa_email(self):
        return f"{self.ns}:{self.email}"

    @property
    def member(self):
        return f"{self.ns}:{self.email}"


class _IAMMember:
    @classmethod
    def from_obj(cls, obj):

        if isinstance(obj, list):
            return [
                cls.from_obj(item) for item in obj
            ]

        assert isinstance(obj, str), \
            print(f"{cls.__name__}: Expecting string, got: {obj}")

        parts = obj.split(':')
        ns = parts[0]
        email = parts[-1]

        return cls(ns=ns, email=email)


@dataclass
class IAMMember(_IAMMember, Spec):
    """
    NOTE in some cases, 'email' is really a name or id
         e.g. ns: projectEditor
              email: $project_id
    """
    ns: str
    email: str

    @property
    def member(self):
        return f"{self.ns}:{self.email}"


@dataclass
class IAMBindings(Spec):

    members: List[IAMMember]
    role: str


@dataclass
class IAMPolicy(Spec):

    bindings: List[IAMBindings]

    @classmethod
    def from_json_list(cls, json_str: str, path: str = None):
        bindings = IAMBindings.from_json_list(json_str, path="bindings")
        return cls(bindings=bindings)

    from_string = from_json_list

    def contains(self, binding: IAMBinding) -> bool:
        """
        Determine if a specific binding is contained in the policy
        """
        binding: IAMBindings

        member = IAMMember(
            ns=binding.ns,
            email=binding.email
        )

        # scan through all bindings looking
        # for all entries pertaining to the target member
        for _binding in self.bindings:
            # print(f"> processing binding: {_binding}")

            if member in _binding.members:
                # print(f"Found member: {member}")

                if binding.role == _binding.role:
                    return True

        return False


@dataclass
class IPAddress(Spec):
    """
    Compute Engine IP address
    """

    name: str
    address: str
    addressType: str
    ipVersion: str


@dataclass
class CloudRunRevisionSpec(Spec):
    """
    Cloud Run Revision Specification (flattened)
    """

    name: str
    url: str
    labels: Dict

    @classmethod
    def from_obj(cls, obj):
        d = {
            "url": obj["status.url"],
            "labels": obj["spec.template.metadata.labels"],
            "name": obj["metadata.name"],
        }

        return cls(**d)

    @classmethod
    def from_string(cls, json_str: str):
        obj = JsonObject.from_string(json_str)
        return cls.from_obj(obj)

    @classmethod
    def from_json_list(cls, json_list, path: str = None):
        liste: List = cls.parse_json(json_list)  # type: ignore

        entries = []
        for obj_dict in liste:
            jso = JsonObject(obj_dict)
            obj = cls.from_obj(jso)
            entries.append(obj)

        return entries


@dataclass
class BackendGroup(Spec):
    balancingMode: str
    group: str
    capacityScaler: int


@dataclass
class BackendServiceSpec(Spec):

    name: str
    port: int
    portName: str
    protocol: str
    backends: List[BackendGroup]


@dataclass
class FwdRule(Spec):
    """Attribute names come directly from gcloud describe"""

    name: str
    IPAddress: str
    IPProtocol: str
    loadBalancingScheme: str
    networkTier: str
    portRange: str
    target: str


@dataclass
class GCSBucket(Spec):
    name: str
    location: str
    default_storage_class: str
    location_type: str
    metageneration: int
    public_access_prevention: str
    uniform_bucket_level_access: str


@dataclass
class SSLCertificate(Spec):
    """
    CAUTION: sensitive information in the 'certificate' field
    """

    name: str
    type: str
    managed: dict = field(default_factory=dict)


@dataclass
class HTTPSProxy(Spec):
    name: str
    sslCertificates: list = field(default_factory=list)
    urlMap: str = field(default_factory=str)


@dataclass
class SchedulerJob(Spec):
    name: str
    retryConfig: dict
    schedule: str
    state: str
    timeZone: str
    location: str = "???"
    pubsubTarget: dict = field(default_factory=dict)


@dataclass
class PubsubTopic(Spec):
    name: str

    def __post_init__(self):
        parts = self.name.split("/")
        self.name = parts[-1]


@dataclass
class FirestoreDb(Spec):
    name: str
    type: str
    locationId: str
    concurrencyMode: str
    pointInTimeRecoveryEnablement: str

    def __post_init__(self):
        parts = self.name.split("/")
        self.name = parts[-1]


@dataclass
class CloudRunNegSpec(Spec):

    name: str
    networkEndpointType: str
    region: str = field(default_factory=str)
    cloudRun: dict = field(default_factory=dict)


@dataclass
class TaskQueue(Spec):

    name: str
    state: str
    location: str = field(default_factory=str)
    rateLimits: dict = field(default_factory=dict)
    retryConfig: dict = field(default_factory=dict)


@dataclass
class UrlMap(Spec):

    id: str = field(default_factory=str)
    name: str = field(default_factory=str)
    defaultService: str = field(default_factory=str)


@dataclass
class ServiceAccountSpec(Spec):
    name: str
    email: str
    projectId: str
    uniqueId: str
    oauth2ClientId: str
    displayName: str = field(default_factory=str)
    description: str = field(default_factory=str)

    def is_default(self):
        """
        Is this service account a default one
        """
        return "iam.gserviceaccount.com" not in self.email
