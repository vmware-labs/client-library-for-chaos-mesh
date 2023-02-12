from chaosmesh.experiments.base.k8s.podfault.container_kill import BaseContainerKillExperiment


class ContainerKill(BaseContainerKillExperiment):
    """
    The `ContainerKill` class creates a chaosmesh experiment that simulates killing a container.

    This class inherits from the `BaseContainerKillExperiment` and adds the chaosmesh experiment
    functionalities.

    Attributes:
        kwargs (dict): A dictionary of arguments for the experiment.

    """

    def __init__(self, **kwargs):
        """
        Initializes the `ContainerKill` class with the given arguments.

        Args:
            kwargs (dict): A dictionary of arguments for the experiment.

        """
        super(ContainerKill, self).__init__(**kwargs)
