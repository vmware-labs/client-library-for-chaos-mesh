from chaosmesh.experiments.base.hosts.stress.memory import BaseHostsStressMemoryExperiment


class HostsStressMemory(BaseHostsStressMemoryExperiment):
    """
    This class creates a memory stress experiment for k8s hosts in ChaosMesh.

    It is a subclass of BaseHostsStressMemoryExperiment and inherits all the attributes and methods from it.

    Args:
        **kwargs: Keyword arguments that can be used to initialize the attributes of the parent class.
    """

    def __init__(self, **kwargs):
        """
        The constructor method that initializes the attributes of the class and its parent class.

        Args:
            **kwargs: Keyword arguments that can be used to initialize the attributes of the parent class.
        """
        super(HostsStressMemory, self).__init__(**kwargs)
