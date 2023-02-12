from abc import ABC
from dataclasses import asdict

from chaosmesh.experiments.base.k8s.stress import StressTest
from chaosmesh.k8s.selector import Selector


class BasePodStressCPUExperiment(StressTest, ABC):
    """
    BasePodStressCPUExperiment is a class that implements the abstract base class StressTest and is used to perform a stress test on CPU resources of Pods.

    Args:
        **kwargs: The keyword arguments that are passed to the class constructor.

    Attributes:
        kwargs (dict): A dictionary of arguments passed to the class constructor.
    """

    def __init__(self, **kwargs):
        """
        The constructor for the BasePodStressCPUExperiment class. It initializes the attributes of the class by calling the superclass constructor.

        Args:
            **kwargs: The keyword arguments that are passed to the class constructor.
        """
        super(BasePodStressCPUExperiment, self).__init__(**kwargs)

    def validate(self) -> None:
        """
        The validate method is used to validate the arguments passed to the class. It checks if the selector argument is not None and is of type `Selector`. It also checks if the workers and load arguments are not None.

        Raises:
            AssertionError: If the selector argument is None or is not of type `Selector`.
            AssertionError: If the workers argument is None.
            AssertionError: If the load argument is None.
        """
        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "check the selector type"

        assert self.kwargs['workers'] is not None, "workers cannot be None"
        assert self.kwargs['load'] is not None, "size cannot be None"

    def spec(self, namespace, name) -> dict:
        """
        The spec method is used to create the specification for the experiment.

        Args:
            namespace (str): The namespace in which the experiment is to be run.
            name (str): The name of the experiment.

        Returns:
            dict: A dictionary that represents the specification of the experiment.
        """
        return {
            "selector": asdict(self.kwargs['selector']),
            "mode": self.kwargs.get('mode'),
            "stressors": {
                "cpu": {
                    "workers": self.kwargs.get('workers'),
                    "load": self.kwargs.get('load')
                }
            },
            "duration": self.kwargs.get('duration')
        }
