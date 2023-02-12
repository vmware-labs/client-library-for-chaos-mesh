from chaosmesh.experiments.base.k8s.jvmfault.raise_exception import BaseRaiseExceptionExperiment


class RaiseException(BaseRaiseExceptionExperiment):
    """
    Class that represents the RaiseException experiment in ChaosMesh.

    This class is a subclass of `BaseRaiseExceptionExperiment` and inherits all the attributes and methods of its parent class. It can be used to raise an exception in the target container to simulate a failure scenario.

    Attributes:
        kwargs (dict): A dictionary that stores all the experiment's arguments.
    """

    def __init__(self, **kwargs):
        """
        Initializes the `RaiseException` class with the given arguments.

        Args:
            kwargs (dict): A dictionary of arguments for the experiment.

        """
        super(RaiseException, self).__init__(**kwargs)
