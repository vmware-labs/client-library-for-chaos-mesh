from abc import ABC
from dataclasses import asdict

from chaosmesh.k8s.experiment import ChaosExperiment
from chaosmesh.k8s.selector import Selector


class PodChaos(ChaosExperiment, ABC):
    """
    Abstract class representing a Pod Chaos experiment.

    This class is used as the base for all the concrete Pod Chaos experiments.
    """

    def __init__(self, **kwargs):
        """
        Initializes the PodChaos instance.

        :param kwargs: Additional arguments to pass to the superclass constructor.
        """
        super(PodChaos, self).__init__(**kwargs)

    @property
    def defaults(self) -> dict:
        """
        Returns the default values for the Pod Chaos experiment.

        :return: The default values for the Pod Chaos experiment.
        :rtype: dict
        """
        return {
            "action": self.action(),
            "gracePeriod": 0,
            "mode": "all",
            "labels": {},
            "pods": {},
            "value": "",
            "duration": ""
        }

    @property
    def schedule(self) -> dict:
        return {
            "type": "PodChaos",
            "spec": "podChaos"
        }

    def action(self) -> str:
        """
        Returns the action to perform on the selected pods.

        :return: The action to perform on the selected pods.
        :rtype: str
        """
        pass

    def api_resources(self) -> dict:
        """
        Returns the API resources required to perform the Pod Chaos experiment.

        :return: The API resources required to perform the Pod Chaos experiment.
        :rtype: dict
        """
        return {"group": 'chaos-mesh.org', "version": 'v1alpha1', "plural": "podchaos"}

    def validate(self):
        """
        Validates the arguments for the Pod Chaos experiment.

        This method will raise an AssertionError if the required arguments are not present.
        """
        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "check the selector type"

    def spec(self, namespace, name) -> dict:
        """
        Returns the specification for the Pod Chaos experiment.

        :param namespace: The namespace where the experiment will be performed.
        :type namespace: str
        :param name: The name of the experiment.
        :type name: str
        :return: The specification for the Pod Chaos experiment.
        :rtype: dict
        """
        return {
            "selector": asdict(self.kwargs['selector']),
            "mode": self.kwargs.get('mode'),
            "value": self.kwargs.get('value'),
            "action": self.kwargs.get('action'),
            "gracePeriod": self.kwargs.get('gracePeriod'),
            "duration": self.kwargs.get('duration')
        }
