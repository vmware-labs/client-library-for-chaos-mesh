from abc import ABC

from chaosmesh.experiments.base.k8s.jvmfault import JVMFault
from chaosmesh.k8s.selector import Selector


class BaseGCExperiment(JVMFault, ABC):
    """
    Base class for GC experiments in ChaosMesh.

    This class provides a basic implementation of a GC experiment in ChaosMesh and serves as a base for other GC experiments. It inherits from `JVMFault` and implements the abstract base class `ABC`.
    :param kwargs: Additional keyword arguments.
    :type kwargs: dict
    """

    def __init__(self, **kwargs):
        """
        Initializes the `BaseGCExperiment` class.

        :param kwargs: Additional keyword arguments.
        :type kwargs: dict
        """
        super(BaseGCExperiment, self).__init__(**kwargs)

    @property
    def defaults(self):
        """
        Returns the default settings for the GC experiment.

        :return: A dictionary containing the default settings.
        :rtype: dict
        """
        return {
            "action": self.action(),
            "class": "",
            "cpuCount": 0,
            "duration": "",
            "exception": "",
            "latency": 0,
            "memType": "",
            "method": "",
            "mode": "all",
            "ruleData": "",
            "value": "",
        }

    def action(self) -> str:
        """
        Returns the action for the GC experiment.

        :return: The action for the GC experiment.
        :rtype: str
        """
        return "gc"

    def validate(self):
        """
        Validates the GC experiment settings.

        This method checks that the required settings (i.e. `selector` and `port`) are not `None` and of the correct type (`Selector`).

        :raises: AssertionError if the required settings are not set or of the incorrect type.
        """
        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "invalid Selector type, should be of type k8s.selector"

        assert self.kwargs['port'] is not None, "port cannot be None"
