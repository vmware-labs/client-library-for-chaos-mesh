from abc import ABC
from dataclasses import asdict

from chaosmesh.experiments.base.k8s.network import NetworkChaos
from chaosmesh.k8s.selector import Selector


class NetworkPartitionExperiment(NetworkChaos, ABC):
    """
    A network partition experiment for Kubernetes.
    """

    def __init__(self, **kwargs):
        """
        Initialize the NetworkPartitionExperiment.

        :param kwargs: keyword arguments for the experiment.
        """

        super(NetworkPartitionExperiment, self).__init__(**kwargs)

    @property
    def defaults(self):
        """
        Get the default configuration for the experiment.

        :return: default configuration for the experiment.
        """

        return {
            "action": self.action(),
            "duration": "",
            "mode": "all",
        }

    def validate(self) -> None:
        """
        Validate the experiment parameters.
        """

        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "invalid Selector type, should be of type k8s.selector"

        assert self.kwargs['external_targets'] is not None, "external_targets cannot be None"
        assert isinstance(self.kwargs['external_targets'], list), "external_targets should be of type list"

        assert self.kwargs['direction'] is not None, "direction cannot be None"

    def action(self) -> str:
        """
        Get the action of the experiment.

        :return: action of the experiment.
        """

        return "partition"

    def spec(self, namespace, name) -> dict:
        """
        Get the specification of the experiment.

        :param namespace: namespace of the experiment.
        :param name: name of the experiment.

        :return: specification of the experiment.
        """

        return {
            "selector": asdict(self.kwargs['selector']),
            "mode": self.kwargs.get('mode'),
            "action": self.kwargs.get('action'),
            "duration": self.kwargs.get('duration'),
            "direction": self.kwargs.get('direction'),
            "externalTargets": self.kwargs.get('external_targets'),
        }
