from chaosmesh.experiments.base.k8s.podfault.pod_failure import BasePodFailureExperiment


class PodFailure(BasePodFailureExperiment):
    """
    A class for creating a PodFailure chaos experiment in ChaosMesh.

    This class is a subclass of `BasePodFailureExperiment` and provides an implementation for creating a chaos experiment that causes a Pod to fail.

    Attributes:
        kwargs (dict): A dictionary of arguments for the chaos experiment.
    """

    def __init__(self, **kwargs):
        """
        Initializes the `PodFailure` class with the given arguments.

        Args:
            kwargs (dict): A dictionary of arguments for the chaos experiment.

        """
        super(PodFailure, self).__init__(**kwargs)
