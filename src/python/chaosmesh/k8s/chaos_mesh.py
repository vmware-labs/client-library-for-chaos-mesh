from abc import ABC

from chaosmesh.k8s.crd import CustomObjectsApi


class ChaosMesh(CustomObjectsApi, ABC):
    """
    A base class for Chaos Mesh experiments. Inherits from CustomObjectsApi, which provides functionality for working with
    Kubernetes custom resources.

    """

    def __init__(self, **kwargs):
        """
        Initializes a new instance of the ChaosMesh class.

        Args:
            **kwargs: Additional keyword arguments.

        """
        self.kwargs = kwargs
        super(ChaosMesh, self).__init__()

        # initialize defaults
        for key, value in self.defaults.items():
            self.kwargs[key] = kwargs.get(key, value)

    @property
    def defaults(self) -> dict:
        """
        The default values for the experiment.

        Returns:
            dict: The default values.

        """
        yield

    def validate(self) -> None:
        """
        Validate the experiment's specification before submitting it to Kubernetes.

        """
        pass

    def submit(self, namespace, name, labels=None):
        """
        Submit an experiment to Kubernetes.

        Args:
            namespace (str): The namespace in which to create the experiment.
            name (str): The name of the experiment.
            labels (dict): The labels to apply to the experiment.

        Returns:
            dict: The created experiment.

        Raises:
            AssertionError: If namespace or name is None.

        """
        assert namespace is not None, "namespace can not be None"
        assert name is not None, "name can not be None"

        # validating the spec before applying it to k8s
        self.validate()

        return self.create(name=name, namespace=namespace, labels=labels)

    def create(self, name, namespace, labels=None):
        """
        Create an experiment in Kubernetes.

        Args:
            name (str): The name of the experiment.
            namespace (str): The namespace in which to create the experiment.
            labels (dict): The labels to apply to the experiment.

        """
        pass
