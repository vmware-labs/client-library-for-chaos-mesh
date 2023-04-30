"""
This code defines a `Schedule` class that represents a Chaos Mesh schedule.

A schedule is a recurring event that can be used to run Chaos Mesh experiments.

The `Schedule` class has the following attributes:

* `experiment`: The Chaos Mesh experiment that this schedule represents.
* `kwargs`: Any additional keyword arguments that are passed to the constructor.

The `Schedule` class has the following methods:

* `api_resources()`: Returns the API resources for this schedule.
* `validate()`: Validates the schedule.
* `defaults()`: Returns the default values for this schedule.
* `spec()`: Returns the specification for this schedule.
* `create()`: Creates this schedule.

"""

import json
import logging

from chaosmesh.k8s.chaos_mesh import ChaosMesh
from chaosmesh.k8s.experiment import ChaosExperiment

log = logging.getLogger("chaosmesh")


class Schedule(ChaosMesh):

    """
    Represents a Chaos Mesh schedule.

    Args:
        experiment: The Chaos Mesh experiment that this schedule represents.
        **kwargs: Any additional keyword arguments that are passed to the constructor.
    """

    def __init__(self, experiment: ChaosExperiment, **kwargs):
        """
        Initializes a new `Schedule` object.

        Args:
            experiment: The Chaos Mesh experiment that this schedule represents.
            **kwargs: Any additional keyword arguments that are passed to the constructor.
        """
        self.experiment = experiment
        super(Schedule, self).__init__(**kwargs)

    def api_resources(self) -> dict:
        """
        Returns the API resources for this schedule.

        Returns:
            A dictionary that contains the API group, version, and plural for this schedule.
        """
        return {"group": 'chaos-mesh.org', "version": 'v1alpha1', "plural": "schedules"}

    def validate(self) -> None:
        """
        Validates the schedule.

        This method ensures that the schedule is valid and can be created.
        """
        assert self.kwargs['schedule'] is not None, "schedule cannot be None"

    @property
    def defaults(self) -> dict:
        """
        Returns the default values for this schedule.

        Returns:
            A dictionary that contains the default values for this schedule.
        """
        return {
            "historyLimit": 3,
            "concurrencyPolicy": 'Forbid',
            "startingDeadlineSeconds": None,
        }

    def spec(self, namespace, name) -> dict:
        """
        Returns the specification for this schedule.

        The specification includes the schedule name, the experiment name, and the experiment spec.

        Args:
            namespace: The namespace where the schedule will be created.
            name: The name of the schedule.

        Returns:
            A dictionary that contains the specification for this schedule.
        """
        return {
            "schedule": self.kwargs.get('schedule'),
            "startingDeadlineSeconds": self.kwargs.get('startingDeadlineSeconds'),
            "concurrencyPolicy": self.kwargs.get('concurrencyPolicy'),
            "historyLimit": self.kwargs.get('historyLimit'),
            "type": self.experiment.schedule['type'],
            self.experiment.schedule['spec']: self.experiment.spec(namespace=namespace, name=name),
        }

    def create(self, name, namespace, labels=None):
        """
        Creates this schedule.

        Args:
            name: The name of the schedule.
            namespace: The namespace where the schedule will be created.
            labels: Any labels that should be applied to the schedule.

        Returns:
            The created schedule object.
        """
        manifest = self.manifest(namespace=namespace, name=name, labels=labels)

        log.debug(f"creating chaosmesh resource {json.dumps(manifest, indent=4)}")

        applied = super().apply(namespace=namespace, object=manifest)

        log.info(f"chaosmesh experiment {name} got applied")

        return applied
