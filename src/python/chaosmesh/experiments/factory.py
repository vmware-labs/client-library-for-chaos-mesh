from chaosmesh.experiments import Experiment, v1alpha1
from chaosmesh.experiments.v1alpha1.hosts.disk.fill import Fill
from chaosmesh.experiments.v1alpha1.hosts.disk.read_payload import ReadPayload
from chaosmesh.experiments.v1alpha1.hosts.disk.write_payload import WritePayload
from chaosmesh.experiments.v1alpha1.hosts.stress.cpu import HostsStressCPU
from chaosmesh.experiments.v1alpha1.hosts.stress.memory import HostsStressMemory
from chaosmesh.experiments.v1alpha1.k8s.jvmfault.gc import GC
from chaosmesh.experiments.v1alpha1.k8s.jvmfault.raise_exception import RaiseException
from chaosmesh.experiments.v1alpha1.k8s.network.bandwidth import NetworkBandwidth
from chaosmesh.experiments.v1alpha1.k8s.network.partition import NetworkPartition
from chaosmesh.experiments.v1alpha1.k8s.podfault.container_kill import ContainerKill
from chaosmesh.experiments.v1alpha1.k8s.podfault.pod_failure import PodFailure
from chaosmesh.experiments.v1alpha1.k8s.podfault.pod_kill import PodKill
from chaosmesh.experiments.v1alpha1.k8s.stress.cpu import PodStressCPU
from chaosmesh.experiments.v1alpha1.k8s.stress.memory import PodStressMemory
from chaosmesh.k8s.experiment import ChaosExperiment


class ExperimentFactory:
    """
    ExperimentFactory is a factory class to retrieve ChaosMesh experiments. 
    It provides a unified interface to get different ChaosMesh experiments based on the version.

    :param version: The version of the ChaosMesh supported by the factory.
    :type version: str
    """
    instance = None

    versions = {
        "v1alpha1": {

            # -- kubernetes experiments --

            # pod fault experiments
            Experiment.POD_FAILURE: v1alpha1.k8s.podfault.pod_failure.PodFailure,
            Experiment.POD_KILL: v1alpha1.k8s.podfault.pod_kill.PodKill,
            Experiment.CONTAINER_KILL: v1alpha1.k8s.podfault.container_kill.ContainerKill,

            # k8s stress experiments
            Experiment.POD_STRESS_CPU: v1alpha1.k8s.stress.cpu.PodStressCPU,
            Experiment.POD_STRESS_MEMORY: v1alpha1.k8s.stress.memory.PodStressMemory,

            # k8s jvm fault experiments
            Experiment.RAISE_EXCEPTION: v1alpha1.k8s.jvmfault.raise_exception.RaiseException,
            Experiment.GC: v1alpha1.k8s.jvmfault.gc.GC,

            Experiment.NETWORK_PARTITION: v1alpha1.k8s.network.partition.NetworkPartition,
            Experiment.NETWORK_BANDWIDTH: v1alpha1.k8s.network.bandwidth.NetworkBandwidth,

            # -- kubernetes experiments ends --

            # -- hosts experiments

            # stress
            Experiment.HOST_STRESS_MEMORY: v1alpha1.hosts.stress.memory.HostsStressMemory,
            Experiment.HOST_STRESS_CPU: v1alpha1.hosts.stress.cpu.HostsStressCPU,

            Experiment.HOST_READ_PAYLOAD: v1alpha1.hosts.disk.read_payload.ReadPayload,
            Experiment.HOST_WRITE_PAYLOAD: v1alpha1.hosts.disk.write_payload.WritePayload,
            Experiment.HOST_DISK_FILL: v1alpha1.hosts.disk.fill.Fill
        }
    }

    def __init__(self, version):
        """
        Initialize the ExperimentFactory instance with the given version.

        :param version: The version of the ChaosMesh supported by the factory.
        :type version: str
        """
        assert version is not None, "Version can not be None, ChaosMesh supported versions {list(self.versions.keys())}"

        assert version in self.versions, \
            f"This client does not support ChaosMesh {version}, supported versions {list(self.versions.keys())}"
        self.version = version

    @classmethod
    def get_instance(cls, version):
        """
        Get the singleton instance of the ExperimentFactory.

        :param version: The version of the ChaosMesh supported by the factory.
        :type version: str
        :return: The ExperimentFactory instance.
        :rtype: ExperimentFactory
        """
        if cls.instance is None:
            cls.instance = ExperimentFactory(version)
        return cls.instance

    def get_experiment(self, e: Experiment, **kwargs) -> ChaosExperiment:
        """
        Retrieve a ChaosMesh experiment.

        :param e: The experiment to retrieve.
        :type e: Experiment
        :param kwargs: Additional arguments to pass to the experiment retrieval function.
        :return: The requested ChaosMesh experiment.
        :rtype: object
        """
        return self.versions[self.version][e](**kwargs)
