from abc import ABC
from dataclasses import asdict

from chaosmesh.experiments.base.k8s.network import NetworkChaos
from chaosmesh.k8s.selector import Selector


class BaseNetworkDelayExperiment(NetworkChaos, ABC):
    """
    A network delay experiment for Kubernetes.

    Extends:
        NetworkChaos: An abstract class that provides common methods for network-related chaos experiments.
        ABC: An abstract base class that provides a common API for classes that are designed to be subclassed.

    Args:
        **kwargs: Arbitrary keyword arguments to configure the network delay experiment.

    Attributes:
        defaults (dict): A dictionary of default values for the experiment configuration.

    """

    def __init__(self, **kwargs):
        """
        Initialize the NetworkDelayExperiment.

        :param kwargs: keyword arguments for the experiment.
        """

        super(BaseNetworkDelayExperiment, self).__init__(**kwargs)

    @property
    def defaults(self):
        """
        Get the default configuration for the experiment.

        :return: default configuration for the experiment.
        """

        return {
            "action": self.action(),
            "correlation": "0",
            "duration": "",
            "jitter": "0ms",
            "mode": "one"
        }

    def validate(self) -> None:
        """
        Validate the experiment parameters.
        """

        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "invalid Selector type, should be of type k8s.selector"

        assert self.kwargs['latency'] is not None, "latency cannot be None"

    def action(self) -> str:
        """
        Get the action of the experiment.

        :return: action of the experiment.
        """

        return "delay"

    def spec(self, namespace, name) -> dict:
        """
        Get the specification of the experiment.

        :param namespace: namespace of the experiment.
        :param name: name of the experiment.

        :return: specification of the experiment.
        """

        return {
            "selector": asdict(self.kwargs['selector']),
            "mode": self.kwargs['mode'],
            "action": self.kwargs['action'],
            "duration": self.kwargs['duration'],
            "delay": {
                "latency": self.kwargs['latency'],
                "correlation": self.kwargs['correlation'],
                "jitter": self.kwargs['jitter'],
            },
        }

