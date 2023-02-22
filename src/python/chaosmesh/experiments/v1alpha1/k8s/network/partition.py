from chaosmesh.experiments.base.k8s.network.partition import NetworkPartitionExperiment


class NetworkPartition(NetworkPartitionExperiment):
    """
    A network partition experiment for Kubernetes.
    """

    def __init__(self, **kwargs):
        """
        Initialize the NetworkPartition.

        :param kwargs: keyword arguments for the experiment.
        """

        super(NetworkPartition, self).__init__(**kwargs)
