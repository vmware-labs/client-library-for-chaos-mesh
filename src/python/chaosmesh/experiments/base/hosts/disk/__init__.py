from abc import ABC

from chaosmesh.k8s.experiment import ChaosExperiment


class DiskFault(ChaosExperiment, ABC):
    """
    This class represents a disk fault experiment using the Chaos Experiment framework.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new instance of the DiskFault class.
        :param kwargs: Optional keyword arguments for configuring the experiment.
        """
        super(DiskFault, self).__init__(**kwargs)

    def api_resources(self) -> dict:
        """
        Returns a dictionary containing the Kubernetes API group, version, and plural for the experiment.
        :return: A dictionary containing the API resources for the experiment.
        """
        return {"group": 'chaos-mesh.org', "version": 'v1alpha1', "plural": "physicalmachinechaos"}

    @property
    def schedule(self) -> dict:
        return {
            "type": "DiskFault",
            "spec": "diskFault"
        }

    @property
    def defaults(self) -> dict:
        """
        Returns a dictionary containing default values for the experiment configuration.
        :return: A dictionary containing default values for the experiment configuration.
        """
        return {
            "action": self.action(),
            "duration": "",
        }

    def validate(self) -> None:
        """
        Validates the experiment configuration to ensure that all required parameters are present.
        :raises AssertionError: If any required parameters are missing.
        """
        assert self.kwargs['address'] is not None, "address cannot be None"
        assert isinstance(self.kwargs['address'], list), "address should be of type list"

        assert self.kwargs[
                   'size'] is not None, "size cannot be None, the supported formats of the size are: c(=1), w(=2), kB(=1000), K(=1024), MB(=1000*1000), M(=1024*1024), GB and so on"
        assert self.kwargs['path'] is not None, "path cannot be None"

        assert self.kwargs['payload_process_num'] is not None, "payload_process_num cannot be None"
        assert self.kwargs.get('payload_process_num', 0) > 0, "payload_process_num should be greater than or equal to 1"

    def action(self) -> str:
        """
        Performs the main action of the experiment.
        :return: A string representing the result of the experiment.
        """
        pass
