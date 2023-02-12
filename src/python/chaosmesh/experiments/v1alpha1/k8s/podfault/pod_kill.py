from chaosmesh.experiments.base.k8s.podfault.pod_kill import BasePodKillExperiment


class PodKill(BasePodKillExperiment):
    """
    The `PodKill` class creates a `PodKill` experiment in ChaosMesh.

    The `PodKill` class is a subclass of `BasePodKillExperiment` and provides functionalities to create a `PodKill` experiment in ChaosMesh. The class is initialized with arguments that are passed as a dictionary. The arguments are then passed to the parent class.

    Args:
        kwargs (dict): A dictionary of arguments passed to the experiment.

    """

    def __init__(self, **kwargs):
        """
        Initializes the `PodKill` class.

        This method is called during the instantiation of the class. It initializes the parent class with the given arguments.

        Args:
            kwargs (dict): A dictionary of arguments passed to the parent class.

        """
        super(PodKill, self).__init__(**kwargs)
