from chaosmesh.experiments.base.hosts.disk.fill import BaseFillExperiment


class Fill(BaseFillExperiment):
    """
    A class for running disk fill experiments with the specified parameters.
    """

    def __init__(self, **kwargs):
        """
        Initializes the experiment with the provided keyword arguments.

        Args:
            **kwargs: Keyword arguments specifying the parameters of the experiment.
        """
        super(Fill, self).__init__(**kwargs)
