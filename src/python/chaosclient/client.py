from enum import Enum

from chaosclient.experiments.hosts.stress.cpu import HostsStressCPU
from chaosclient.experiments.hosts.stress.memory import HostsStressMemory
from chaosclient.experiments.k8s.jvmfault.gc import GC
from chaosclient.experiments.k8s.jvmfault.raise_exception import RaiseException
from chaosclient.experiments.k8s.podfault.container_kill import ContainerKill
from chaosclient.experiments.k8s.podfault.pod_failure import PodFailure
from chaosclient.experiments.k8s.podfault.pod_kill import PodKill
from chaosclient.experiments.k8s.stress.cpu import PodStressCPU
from chaosclient.experiments.k8s.stress.memory import PodStressMemory


class Experiment(Enum):
    POD_FAILURE = "POD_FAILURE"
    POD_KILL = "POD_KILL"
    CONTAINER_KILL = "CONTAINER_KILL"

    POD_STRESS_CPU = "POD_STRESS_CPU"
    POD_STRESS_MEMORY = "POD_STRESS_MEMORY"

    RAISE_EXCEPTION = "RAISE_EXCEPTION"
    GC = "GC"

    HOST_STRESS_MEMORY = "HOST_STRESS_MEMORY"
    HOST_STRESS_CPU = "HOST_STRESS_CPU"


class ExperimentFactory:
    instance = None

    experiments = {

        # -- kubernetes experiments --

        # pod fault experiments
        Experiment.POD_FAILURE: PodFailure,
        Experiment.POD_KILL: PodKill,
        Experiment.CONTAINER_KILL: ContainerKill,

        # k8s stress experiments
        Experiment.POD_STRESS_CPU: PodStressCPU,
        Experiment.POD_STRESS_MEMORY: PodStressMemory,

        # k8s jvm fault experiments
        Experiment.RAISE_EXCEPTION: RaiseException,
        Experiment.GC: GC,

        # -- kubernetes experiments ends --

        # -- hosts experiments

        # stress
        Experiment.HOST_STRESS_MEMORY: HostsStressMemory,
        Experiment.HOST_STRESS_CPU: HostsStressCPU,

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
