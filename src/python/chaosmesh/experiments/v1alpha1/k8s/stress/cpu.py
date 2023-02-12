from chaosmesh.experiments.base.k8s.stress.cpu import BasePodStressCPUExperiment


class PodStressCPU(BasePodStressCPUExperiment):
    """
    A class that creates a PodStressCPU experiment in ChaosMesh.

    This class is derived from `BasePodStressCPUExperiment` and provides a way to create a PodStressCPU experiment in ChaosMesh.

    Attributes:
        kwargs (dict): A dictionary of arguments for the experiment.

    """

    def __init__(self, **kwargs):
        """
        Initializes the `PodStressCPU` class with the given arguments.

        Args:
            kwargs (dict): A dictionary of arguments for the experiment.

        """
        super(PodStressCPU, self).__init__(**kwargs)
