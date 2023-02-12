from chaosmesh.experiments.base.k8s.jvmfault.gc import BaseGCExperiment


class GC(BaseGCExperiment):
    """
    GC is a subclass of the `BaseGCExperiment` class. It is used to perform GC experiments in ChaosMesh.

    This class is initialized with the same keyword arguments as the `BaseGCExperiment` class.
    """

    def __init__(self, **kwargs):
        """
        Initialize the GC class. This method calls the `__init__` method of the parent class, `BaseGCExperiment`,
        with the provided keyword arguments.

        Args:
            **kwargs: Keyword arguments to pass to the parent class's `__init__` method.
        """
        super(GC, self).__init__(**kwargs)
