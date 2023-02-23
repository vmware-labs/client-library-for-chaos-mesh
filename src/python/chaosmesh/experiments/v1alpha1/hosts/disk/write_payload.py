from chaosmesh.experiments.base.hosts.disk.write_payload import BaseWritePayloadExperiment


class WritePayload(BaseWritePayloadExperiment):
    """
    A class for implementing an experiment that writes a payload to a disk.

    Args:
        BaseWritePayloadExperiment (class): A class that represents a base experiment for writing a payload to a disk.

    """

    def __init__(self, **kwargs):
        """
        Initializes a new instance of the WritePayload class.

        Args:
            **kwargs (dict): A dictionary of keyword arguments.

        """
        super(WritePayload, self).__init__(**kwargs)
