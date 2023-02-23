from abc import ABC

from chaosmesh.experiments.base.hosts.disk import DiskFault


class BaseFillExperiment(DiskFault, ABC):
    """
    A base class for implementing an experiment that fills the disk with data.

    Args:
        DiskFault (class): A class that represents a fault in the disk.
        ABC (class): A class that represents an abstract base class.

    """

    def __init__(self, **kwargs):
        """
        Initializes a new instance of the BaseFillExperiment class.

        Args:
            **kwargs (dict): A dictionary of keyword arguments.

        """
        super(BaseFillExperiment, self).__init__(**kwargs)

    def action(self) -> str:
        """
        Returns the action of the experiment.

        Returns:
            str: The action of the experiment.

        """
        return "disk-fill"

    def validate(self) -> None:
        """
        Validates the keyword arguments passed to the experiment.

        Raises:
            AssertionError: If any of the validation conditions are not met.

        """
        assert self.kwargs['address'] is not None, "address cannot be None"
        assert isinstance(self.kwargs['address'], list), "address should be of type list"

        assert self.kwargs[
                   'size'] is not None, "size cannot be None, the supported formats of the size are: c(=1), w(=2), kB(=1000), K(=1024), MB(=1000*1000), M(=1024*1024), GB and so on"
        assert self.kwargs['path'] is not None, "path cannot be None"

        assert isinstance(self.kwargs['fill_by_fallocate'], bool), "fill_by_fallocate should be of type bool"
        assert self.kwargs['fill_by_fallocate'] is not None, "fill_by_fallocate cannot be None"

    def spec(self, namespace, name) -> dict:
        """
        Returns the specification of the experiment.

        Args:
            namespace (str): The namespace of the experiment.
            name (str): The name of the experiment.

        Returns:
            dict: The specification of the experiment.

        """
        return {
            "action": self.kwargs['action'],
            "address": self.kwargs['address'],
            "disk-fill": {
                "size": self.kwargs['size'],
                "path": self.kwargs['path'],
                "fill-by-fallocate": self.kwargs['fill_by_fallocate'],
            },
            "duration": self.kwargs['duration']
        }
