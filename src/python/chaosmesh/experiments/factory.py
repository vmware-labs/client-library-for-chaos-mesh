from chaosmesh.experiments import Experiment
from chaosmesh.experiments.hosts.stress.cpu import HostsStressCPU
from chaosmesh.experiments.hosts.stress.memory import HostsStressMemory
from chaosmesh.experiments.k8s.jvmfault.gc import GC
from chaosmesh.experiments.k8s.jvmfault.raise_exception import RaiseException
from chaosmesh.experiments.k8s.podfault.container_kill import ContainerKill
from chaosmesh.experiments.k8s.podfault.pod_failure import PodFailure
from chaosmesh.experiments.k8s.podfault.pod_kill import PodKill
from chaosmesh.experiments.k8s.stress.cpu import PodStressCPU
from chaosmesh.experiments.k8s.stress.memory import PodStressMemory


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

    def get_experiment(self, e: Experiment, **kwargs):
        return self.experiments[e](**kwargs)
