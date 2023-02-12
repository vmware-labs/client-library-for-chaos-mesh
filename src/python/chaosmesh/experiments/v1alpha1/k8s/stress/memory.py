from chaosmesh.experiments.base.k8s.stress.memory import BasePodStressMemoryExperiment


class PodStressMemory(BasePodStressMemoryExperiment):
    """
    The `PodStressMemory` class creates a memory stress experiment in ChaosMesh.

    This class is derived from `BasePodStressMemoryExperiment` and provides all the necessary functionalities for creating and submitting a memory stress experiment to ChaosMesh.

    Args:
        kwargs (dict): A dictionary of arguments for the experiment.

    """

    def __init__(self, **kwargs):
        """
        Initializes the `PodStressMemory` class with the given arguments.

        Args:
            kwargs (dict): A dictionary of arguments for the experiment.

        """
        super(PodStressMemory, self).__init__(**kwargs)
