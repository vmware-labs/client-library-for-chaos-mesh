from abc import ABC

from chaosmesh.experiments.base.hosts.stress import StressTest


class BaseHostsStressMemoryExperiment(StressTest, ABC):
    """
    Base class for hosting stress memory experiments

    This class is a subclass of StressTest and implements the `action` and `spec` methods
    for stress memory experiments. The class also defines a `validate` method to validate
    the inputs provided to the class.
    """

    def __init__(self, **kwargs):
        """
        Initialize the BaseHostsStressMemoryExperiment class

        :param kwargs: Keyword arguments to pass to the parent class StressTest
        """
        super(BaseHostsStressMemoryExperiment, self).__init__(**kwargs)

    def action(self) -> str:
        """
        Return the action name for the stress memory experiment

        :return: String "stress-mem"
        """
        return "stress-mem"

    def validate(self):
        """
        Validate the inputs for the stress memory experiment

        This method checks that the required parameters, `address` and `size`, are provided
        and are of the correct type.
        """
        assert self.kwargs['address'] is not None, "address cannot be None"
        assert self.kwargs['size'] is not None, "size cannot be None"

    def spec(self, namespace, name):
        """
        Return the specification for the stress memory experiment

        :param namespace: Namespace for the experiment
        :param name: Name of the experiment

        :return: Dictionary containing the specification for the stress memory experiment
        """
        return {
            "action": self.action(),
            "address": self.kwargs['address'],
            "mode": self.kwargs.get('mode'),
            "stress-mem": {
                "size": self.kwargs['size']
            },
            "duration": self.kwargs['duration']
        }
