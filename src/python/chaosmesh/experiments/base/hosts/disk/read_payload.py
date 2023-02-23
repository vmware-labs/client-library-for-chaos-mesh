from abc import ABC

from chaosmesh.experiments.base.hosts.disk import DiskFault


class BaseReadPayloadExperiment(DiskFault, ABC):
    """
    This class represents a base read payload experiment using the DiskFault and ABC classes.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new instance of the BaseReadPayloadExperiment class.
        :param kwargs: Optional keyword arguments for configuring the experiment.
        """
        super(BaseReadPayloadExperiment, self).__init__(**kwargs)

    def action(self) -> str:
        """
        Returns the name of the action performed by the experiment.
        :return: A string representing the name of the action.
        """
        return "disk-read-payload"

    def spec(self, namespace, name) -> dict:
        """
        Returns a dictionary containing the experiment specification.
        :param namespace: The Kubernetes namespace in which to create the experiment.
        :param name: The name of the experiment.
        :return: A dictionary containing the experiment specification.
        """
        return {
            "action": self.kwargs['action'],
            "address": self.kwargs['address'],
            "disk-read-payload": {
                "size": self.kwargs['size'],
                "path": self.kwargs['path'],
                "payload-process-num": self.kwargs['payload_process_num'],
            },
            "duration": self.kwargs['duration'],
        }
