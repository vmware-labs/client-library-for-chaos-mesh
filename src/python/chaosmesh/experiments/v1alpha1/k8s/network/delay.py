from chaosmesh.experiments.base.k8s.network.delay import BaseNetworkDelayExperiment


class NetworkDelay(BaseNetworkDelayExperiment):
    """
    A network delay experiment for Kubernetes.
    """

    def __init__(self, **kwargs):
        """
        Initialize the NetworkDelay.

        :param kwargs: keyword arguments for the experiment.
        """

        super(NetworkDelay, self).__init__(**kwargs)
