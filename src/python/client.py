from enum import Enum

from src.python.experiments.k8s.podfault.pod_failure import PodFailure


class Experiment(Enum):
    K8S_POD_FAILURE = "POD_FAILURE"
    K8S_POD_KILL = "POD_KILL"
    K8S_CONTAINER_KILL = "POD_CONTAINER_KILL"


class ExperimentFactory:
    instance = None

    experiments = {
        Experiment.K8S_POD_FAILURE: PodFailure
    }

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = ExperimentFactory()
        return cls.instance

    def get(self, e: Experiment, **kwargs):
        return self.experiments[e](**kwargs)


class ChaosMeshClient:

    def __init__(self):
        self.factory = ExperimentFactory().get_instance()

    def start(self, e: Experiment, namespace, name, **kwargs):
        self.factory.get(e, **kwargs).submit(namespace, name)

    def pause(self, e: Experiment, namespace, name, **kwargs):
        self.factory.get(e, **kwargs).pause(namespace, name)

    def delete(self, e: Experiment, namespace, name, **kwargs):
        self.factory.get(e, **kwargs).delete(namespace=namespace, name=name)
