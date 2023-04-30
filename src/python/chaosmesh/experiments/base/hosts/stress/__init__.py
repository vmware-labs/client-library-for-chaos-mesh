from abc import ABC

from chaosmesh.k8s.experiment import ChaosExperiment


class StressTest(ChaosExperiment, ABC):
    """
    The StressTest is a class for defining a stress testing chaos experiment on a physical machine.

    Attributes:
    -----------
    None

    Methods:
    --------
    api_resources() -> dict:
        Returns a dictionary containing the Kubernetes API resource information for the experiment.
        
    defaults() -> dict:
        Returns a dictionary containing the default values for the experiment's parameters.
        
    action() -> str:
        Returns a string representing the type of action that the experiment performs.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new instance of the StressTest class.

        Parameters:
        -----------
        kwargs : dict
            A dictionary containing the parameters for the experiment.
        """
        super(StressTest, self).__init__(**kwargs)

    @property
    def schedule(self) -> dict:
        return {
            "type": "PhysicalMachineChaos",
            "spec": "physicalMachineChaos"
        }

    def api_resources(self) -> dict:
        """
        Returns a dictionary containing the Kubernetes API resource information for the experiment.

        Returns:
        --------
        dict
            A dictionary containing the Kubernetes API resource information for the experiment.
        """
        return {"group": 'chaos-mesh.org', "version": 'v1alpha1', "plural": "physicalmachinechaos"}

    @property
    def defaults(self) -> dict:
        """
        Returns a dictionary containing the default values for the experiment's parameters.

        Returns:
        --------
        dict
            A dictionary containing the default values for the experiment's parameters.
        """
        return {
            "duration": "",
            "mode": "all",
            "workers": 1
        }

    def action(self) -> str:
        """
        Returns a string representing the type of action that the experiment performs.

        Returns:
        --------
        str
            A string representing the type of action that the experiment performs.
        """
        pass
