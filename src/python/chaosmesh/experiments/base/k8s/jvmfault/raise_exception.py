from abc import ABC

from chaosmesh.experiments.base.k8s.jvmfault import JVMFault
from chaosmesh.k8s.selector import Selector


class BaseRaiseExceptionExperiment(JVMFault, ABC):
    """
    This class represents the base experiment to raise exceptions in a JVM application.

    It inherits from the `JVMFault` class and provides the default parameters for the experiment.
    The experiment raises exceptions in the target class and method of the JVM application.

    Attributes:
        kwargs (dict): Keyword arguments to initialize the `JVMFault` class.
    """

    def __init__(self, **kwargs):
        """
        Initialize the `BaseRaiseExceptionExperiment` class.

        Calls the `__init__` method of the `JVMFault` class with the provided keyword arguments.
        """
        super(BaseRaiseExceptionExperiment, self).__init__(**kwargs)

    @property
    def defaults(self):
        """
        Returns a dictionary with the default parameters for the experiment.

        The default parameters include:
        - `action`: The type of the experiment, which is set to "exception".
        - `cpuCount`: The number of CPU cores to be affected by the experiment.
        - `duration`: The duration of the experiment.
        - `latency`: The latency to introduce in the application.
        - `memType`: The type of memory to be affected by the experiment.
        - `mode`: The mode of the experiment, which is set to "all".
        - `ruleData`: The rule data for the experiment.
        - `value`: The value for the experiment.

        Returns:
            dict: The default parameters for the experiment.
        """
        return {
            "action": self.action(),
            "cpuCount": 0,
            "duration": "",
            "latency": 0,
            "memType": "",
            "mode": "all",
            "ruleData": "",
            "value": ""
        }

    def action(self) -> str:
        """
        Returns the type of the experiment, which is set to "exception".

        Returns:
            str: The type of the experiment, which is set to "exception".
        """
        return "exception"

    def validate(self):
        """
        Validates the parameters of the experiment.

        Raises:
            AssertionError: If the `targetClass` parameter is None.
            AssertionError: If the `method` parameter is None.
            AssertionError: If the `exception` parameter is None.
            AssertionError: If the `port` parameter is None.
            AssertionError: If the `selector` parameter is None.
            AssertionError: If the `selector` parameter is not of type `Selector`.

        """
        assert self.kwargs['targetClass'] is not None, "`targetClass` cannot be None"
        assert self.kwargs['method'] is not None, "method cannot be None"
        assert self.kwargs['exception'] is not None, "exception cannot be None"
        assert self.kwargs['port'] is not None, "port cannot be None"

        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "invalid Selector type, should be of type k8s.selector"
