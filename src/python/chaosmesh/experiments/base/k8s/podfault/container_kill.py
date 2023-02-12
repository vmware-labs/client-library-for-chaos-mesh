from abc import ABC
from dataclasses import asdict

from chaosmesh.experiments.base.k8s.podfault import PodChaos
from chaosmesh.k8s.selector import Selector


class BaseContainerKillExperiment(PodChaos, ABC):
    """
    Subclass of PodChaos that implements a chaos experiment that kills one or more containers in a
    pod by their name.
    """

    def __init__(self, **kwargs):
        """
        Initializes the BaseContainerKillExperiment class by calling the super class's __init__ method.
        :param kwargs: Keyword arguments that are passed to the super class.
        """
        super(BaseContainerKillExperiment, self).__init__(**kwargs)

    def action(self) -> str:
        """
        Returns the type of chaos action to be performed, which is 'container-kill' in this case.
        :return: The type of chaos action as a string.
        """
        return "container-kill"

    def validate(self) -> None:
        """
        Validates the arguments passed to the experiment by checking that the label selector is not None and
        of type Selector. Additionally, the container name must not be None.
        """
        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "check the selector type"

        assert self.kwargs['container_names'] is not None, "container name cannot be None"

    def spec(self, namespace, name) -> dict:
        """
        Returns the specifications for the chaos experiment, including the selector, mode, container names,
        action and grace period.
        :param namespace: The namespace in which the experiment is to be performed.
        :param name: The name of the experiment.
        :return: A dictionary containing the specifications for the chaos experiment.
        """
        return {
            "selector": asdict(self.kwargs['selector']),
            "mode": self.kwargs['mode'],
            "containerNames": self.kwargs['container_names'],
            "action": self.kwargs.get('action'),
            "gracePeriod": self.kwargs.get('gracePeriod')
        }
