from dataclasses import dataclass


# the naming conversion should in-lined with the k8s resource definition

@dataclass
class Metadata:
    namespace: str
    name: str
    labels: dict

    def __init__(self, namespace: str, name: str, labels: dict) -> None:
        self.namespace = namespace
        self.name = name
        self.labels = labels


@dataclass
class Manifest:
    kind: str
    apiVersion: str
    metadata: Metadata
    spec: dict

    def __init__(self, kind: str, api_version: str, metadata: Metadata, spec: dict) -> None:
        self.kind = kind
        self.apiVersion = api_version
        self.metadata = metadata
        self.spec = spec
