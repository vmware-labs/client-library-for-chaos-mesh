from abc import ABC

from chaosmesh.k8s.experiment import ChaosExperiment


class StressTest(ChaosExperiment, ABC):

    def __init__(self, **kwargs):
        super(StressTest, self).__init__(**kwargs)

    @property
    def defaults(self) -> dict:
        return {
            "duration": '',
            "labels": {},
            "load": 100,
            "mode": "all",
            "size": '10',
            "workers": 1
        }

    @property
    def schedule(self) -> dict:
        return {
            "type": "StressChaos",
            "spec": "stressChaos"
        }

    def api_resources(self) -> dict:
        return {"group": 'chaos-mesh.org', "version": 'v1alpha1', "plural": "stresschaos"}
