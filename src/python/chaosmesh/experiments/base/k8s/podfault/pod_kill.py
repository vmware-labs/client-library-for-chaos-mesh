from abc import ABC

from chaosmesh.experiments.base.k8s.podfault import PodChaos


class BasePodKillExperiment(PodChaos, ABC):
    """
    The BasePodKillExperiment class is a subclass of the PodChaos class used to implement a chaos experiment that simulates
    the killing of a pod.

    Parameters
    ----------
    **kwargs : any number of keyword arguments

    """

    def __init__(self, **kwargs):
        """
        Initialize the BasePodKillExperiment class by passing any keyword arguments to the super class's __init__ method.

        """
        super(BasePodKillExperiment, self).__init__(**kwargs)

    def action(self) -> str:
        """
        Returns the string "pod-kill" to indicate that this type of chaos experiment involves simulating the killing of a pod.

        Returns
        -------
        str
            "pod-kill"

        """
        return "pod-kill"
