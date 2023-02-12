from chaosmesh.experiments.base.hosts.stress.cpu import BaseHostsStressCPUExperiment


class HostsStressCPU(BaseHostsStressCPUExperiment):
    """
    The `HostsStressCPU` class creates a CPU stress experiment for Kubernetes hosts in Chaos Mesh.

    This class extends the `BaseHostsStressCPUExperiment` class and inherits its properties and methods.
    """

    def __init__(self, **kwargs):
        """
        Initialize the `HostsStressCPU` class by calling the superclass's `__init__` method with the provided arguments.

        :param kwargs: Keyword arguments passed to the superclass's `__init__` method.
        """
        super(HostsStressCPU, self).__init__(**kwargs)
