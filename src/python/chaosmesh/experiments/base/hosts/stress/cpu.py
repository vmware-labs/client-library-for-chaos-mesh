from abc import ABC

from chaosmesh.experiments.base.hosts.stress import StressTest


class BaseHostsStressCPUExperiment(StressTest, ABC):
    """
    BaseHostsStressCPUExperiment class is a derived class from StressTest and is used to perform CPU stress tests on a host.

    Attributes:
    -----------
    kwargs : dict
        A dictionary of arguments to initialize the experiment.

    Methods:
    --------
    action() -> str:
        Returns the action string "stress-cpu".

    validate() -> None:
        Validates the inputs in the kwargs dictionary to make sure all required parameters are present.
        Raises an assertion error if the address, load, or workers are None.

    spec(namespace: str, name: str) -> dict:
        Returns a dictionary representation of the experiment.
        The dictionary contains information about the action, address, mode, stress-cpu and the duration.
    """

    def __init__(self, **kwargs):
        """
        Constructor to initialize the BaseHostsStressCPUExperiment class.

        Parameters:
        -----------
        kwargs : dict
            A dictionary of arguments to initialize the experiment.
        """
        super(BaseHostsStressCPUExperiment, self).__init__(**kwargs)

    def action(self) -> str:
        """
        Returns the action string "stress-cpu".

        Returns:
        --------
        str:
            The string "stress-cpu".
        """
        return "stress-cpu"

    def validate(self) -> None:
        """
        Validates the inputs in the kwargs dictionary to make sure all required parameters are present.
        Raises an assertion error if the address, load, or workers are None.
        """
        assert self.kwargs['address'] is not None, "address cannot be None"

        assert self.kwargs['load'] is not None, "load cannot be None"
        assert isinstance(self.kwargs['load'], int), "load type should be int"

        assert self.kwargs['workers'] is not None, "workers cannot be None"

    def spec(self, namespace, name) -> dict:
        """
        Returns a dictionary representation of the experiment.
        The dictionary contains information about the action, address, mode, stress-cpu and the duration.

        Parameters:
        -----------
        namespace: str
            Namespace to run the experiment in.

        name: str
            Name of the experiment.

        Returns:
        --------
        dict:
            Dictionary representation of the experiment.
        """
        return {
            "action": self.action(),
            "address": self.kwargs['address'],
            "mode": self.kwargs.get('mode'),
            "stress-cpu": {
                "load": self.kwargs['load'],
                "workers": self.kwargs['workers']
            },
            "duration": self.kwargs['duration']
        }
