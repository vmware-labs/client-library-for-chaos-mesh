from abc import ABC

from chaosmesh.experiments.base.k8s.podfault import PodChaos


class BasePodFailureExperiment(PodChaos, ABC):
    """
    The BasePodFailureExperiment class is a subclass of the PodChaos class used to implement a chaos experiment that
    simulates the failure of a pod.

    Parameters
    ----------
    **kwargs : any number of keyword arguments

    """

    def __init__(self, **kwargs):
        """
        Initialize the BasePodFailureExperiment class by passing any keyword arguments to the super class's __init__ method.

        """
        super(BasePodFailureExperiment, self).__init__(**kwargs)

    def action(self) -> str:
        """
        Returns the string "pod-failure" to indicate that this type of chaos experiment involves simulating the failure of a pod.

        Returns
        -------
        str
            "pod-failure"

        """
        return "pod-failure"
