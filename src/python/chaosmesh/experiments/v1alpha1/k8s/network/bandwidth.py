from chaosmesh.experiments.base.k8s.network.bandwidth import BaseNetworkBandwidthExperiment


class NetworkBandwidth(BaseNetworkBandwidthExperiment):
    """
    NetworkBandwidth is a subclass of NetworkBandwidthExperiment, which defines a Kubernetes network chaos
    experiment that modifies network bandwidth.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new instance of the NetworkBandwidth class with the specified keyword arguments.

        Args:
            **kwargs: A dictionary of keyword arguments that are passed to the NetworkBandwidthExperiment constructor.

        Returns:
            A new instance of the NetworkBandwidth class.
        """
        super(NetworkBandwidth, self).__init__(**kwargs)
