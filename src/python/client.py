from enum import Enum

from .experiments.k8s.podfault.pod_failure import PodFailure
from .selector import Selector


class Experiment(Enum):
    K8S_POD_FAILURE = "POD_FAILURE"
    K8S_POD_KILL = "POD_KILL"
    K8S_CONTAINER_KILL = "POD_CONTAINER_KILL"


class ExperimentFactory:
    instance = None

    experiments = {
        Experiment.K8S_POD_FAILURE: PodFailure()
    }

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = ExperimentFactory()
        return cls.instance

    def get(self, e: Experiment):
        return self.experiments[e]


class ChaosMeshClient:

    def __init__(self):
        self.factory = ExperimentFactory().get_instance()

    def start(self, namespace: str, selector: Selector, e: Experiment):
        self.factory.get(e).start(namespace=namespace, selector=selector)
