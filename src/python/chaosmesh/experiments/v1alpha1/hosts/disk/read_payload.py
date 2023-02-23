from chaosmesh.experiments.base.hosts.disk.read_payload import BaseReadPayloadExperiment


class ReadPayload(BaseReadPayloadExperiment):
    """
    A subclass of BaseReadPayloadExperiment class that represents a disk read payload experiment.

    This class inherits properties and methods from the BaseReadPayloadExperiment class and overrides its constructor.
    """

    def __init__(self, **kwargs):
        """
        Initializes the ReadPayload object with the arguments passed to it.

        Args:
            **kwargs: Arbitrary keyword arguments. These arguments are used to set the attributes of the ReadPayload
            object.
        """
        super(ReadPayload, self).__init__(**kwargs)
