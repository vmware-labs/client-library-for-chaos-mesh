from abc import ABC

from chaosmesh.experiments.base.hosts.disk import DiskFault


class BaseWritePayloadExperiment(DiskFault, ABC):
    """
    A class for implementing a base experiment that writes a payload to a disk.

    Args:
        DiskFault (class): A class that simulates disk faults.
        ABC (class): A class that represents an abstract base class.

    """

    def __init__(self, **kwargs):
        """
        Initializes a new instance of the BaseWritePayloadExperiment class.

        Args:
            **kwargs (dict): A dictionary of keyword arguments.

        """
        super(BaseWritePayloadExperiment, self).__init__(**kwargs)

    def action(self) -> str:
        """
        Returns the action for the experiment.

        Returns:
            str: The action for the experiment.

        """
        return "disk-write-payload"

    def spec(self, namespace, name) -> dict:
        """
        Returns a dictionary that represents the experiment specification.

        Args:
            namespace (str): The namespace of the experiment.
            name (str): The name of the experiment.

        Returns:
            dict: A dictionary that represents the experiment specification.

        """
        return {
            "action": self.kwargs['action'],
            "address": self.kwargs['address'],
            "disk-write-payload": {
                "size": self.kwargs['size'],
                "path": self.kwargs['path'],
                "payload-process-num": self.kwargs['payload_process_num'],
            },
            "duration": self.kwargs['duration']
        }
