from abc import ABC
from dataclasses import asdict

from chaosmesh.experiments.base.k8s.network import NetworkChaos
from chaosmesh.k8s.selector import Selector


class BaseNetworkBandwidthExperiment(NetworkChaos, ABC):
    """
    Defines a network bandwidth chaos experiment.

    Extends:
        NetworkChaos: An abstract class that provides common methods for network-related chaos experiments.
        ABC: An abstract base class that provides a common API for classes that are designed to be subclassed.

    Args:
        **kwargs: Arbitrary keyword arguments to configure the network bandwidth experiment.

    Attributes:
        defaults (dict): A dictionary of default values for the experiment configuration.

    """

    def __init__(self, **kwargs):
        """
        Initializes a new instance of the NetworkBandwidthExperiment class.

        Args:
            **kwargs: Arbitrary keyword arguments to configure the network bandwidth experiment.
        """
        super(BaseNetworkBandwidthExperiment, self).__init__(**kwargs)

    @property
    def defaults(self):
        """
        Gets the default values for the experiment configuration.

        Returns:
            dict: A dictionary of default values for the experiment configuration.
        """
        return {
            "action": self.action(),
            "duration": "",
            "minburst": 0,
            "mode": "all",
            "peakrate": 0
        }

    def validate(self) -> None:
        """
        Validates the configuration of the experiment.

        Raises:
            AssertionError: If the configuration is invalid.
        """
        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "invalid Selector type, should be of type k8s.selector"

        assert self.kwargs['rate'] is not None, "rate cannot be None, the rate allows are bps, kbps, mbps, gbps, tbps unit. For example, bps means bytes per second"

        assert self.kwargs['buffer'] is not None, "buffer cannot be None"
        assert self.kwargs.get('buffer', 0) > 0, "buffer should be greater than or equal to 1"

        assert self.kwargs['limit'] is not None, "limit cannot be None"
        assert self.kwargs.get('limit', 0) > 0, "limit should be greater than or equal to 1"

        assert self.kwargs['direction'] is not None, "direction cannot be None, allowed values are from, to, both"

        assert self.kwargs['external_targets'] is not None, "external_targets cannot be None"
        assert isinstance(self.kwargs['external_targets'], list), "external_targets should be of type list"

    def action(self) -> str:
        """
        Gets the action string for the experiment.

        Returns:
            str: The action string for the experiment.
        """
        return "bandwidth"

    def spec(self, namespace, name) -> dict:
        """
        Gets the experiment specification in dictionary format.

        Args:
            namespace (str): The namespace of the experiment.
            name (str): The name of the experiment.

        Returns:
            dict: The experiment specification in dictionary format.
        """
        return {
            "selector": asdict(self.kwargs['selector']),
            "mode": self.kwargs.get('mode'),
            "action": self.kwargs.get('action'),
            "duration": self.kwargs.get('duration'),
            "bandwidth": {
                "rate": self.kwargs.get('rate'),
                "buffer": self.kwargs.get('buffer'),
                "limit": self.kwargs.get('limit'),
                "peakrate": self.kwargs.get('peakrate'),
                "minburst": self.kwargs.get('minburst'),
            },
            "direction": self.kwargs.get('direction'),
            "externalTargets": self.kwargs['external_targets']
        }
