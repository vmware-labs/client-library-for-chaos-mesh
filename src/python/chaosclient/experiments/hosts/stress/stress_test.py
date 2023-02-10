from abc import ABC

from chaosclient.k8s.experiment import ChaosExperiment


class StressTest(ChaosExperiment, ABC):

    def __init__(self, **kwargs):
        super(StressTest, self).__init__(**kwargs)

    def api_resources(self):
        return {"group": 'chaos-mesh.org', "version": 'v1alpha1', "plural": "physicalmachinechaos"}

    @property
    def defaults(self):
        return {
            "duration": "",
            "workers": 1
        }

    def action(self) -> str:
        pass
