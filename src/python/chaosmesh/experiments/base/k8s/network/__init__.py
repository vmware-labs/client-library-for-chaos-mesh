"""
This module defines the `NetworkChaos` class, which is a sub-class of `ChaosExperiment` from `chaosmesh.k8s.experiment` package.
"""

from abc import ABC

from chaosmesh.k8s.experiment import ChaosExperiment


class NetworkChaos(ChaosExperiment, ABC):
    """
    A class to define the network chaos experiment that extends the `ChaosExperiment` and `ABC` classes.
    """

    def __init__(self, **kwargs):
        """
        Initialize the `NetworkChaos` instance with keyword arguments.

        Args:
            **kwargs: Keyword arguments to configure the network chaos experiment.
        """
        super(NetworkChaos, self).__init__(**kwargs)

    def action(self) -> str:
        """
        Override the `action` method from the `ChaosExperiment` class to implement the network chaos experiment.

        Returns:
            str: A string representation of the network chaos experiment action.
        """
        pass

    @property
    def schedule(self) -> dict:
        return {
            "type": "NetworkChaos",
            "spec": "networkChaos"
        }

    @property
    def defaults(self) -> dict:
        """
        Define the default values for the network chaos experiment.

        Returns:
            dict: A dictionary of default values for the network chaos experiment.
        """
        yield

    def api_resources(self) -> dict:
        """
        Define the API resources for the network chaos experiment.

        Returns:
            dict: A dictionary of API resources for the network chaos experiment.
        """
        return {"group": 'chaos-mesh.org', "version": 'v1alpha1', "plural": "networkchaos"}

    def validate(self) -> None:
        """
        Validate the configuration of the network chaos experiment.
        """
        pass

    def spec(self, namespace, name) -> dict:
        """
        Define the specification of the network chaos experiment.

        Args:
            namespace (str): The namespace of the network chaos experiment.
            name (str): The name of the network chaos experiment.

        Returns:
            dict: A dictionary representing the specification of the network chaos experiment.
        """
        pass
