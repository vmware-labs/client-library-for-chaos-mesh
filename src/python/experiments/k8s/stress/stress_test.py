from abc import ABC

from ...experiment import ChaosExperiment


class StressTest(ChaosExperiment, ABC):

    def __init__(self, **kwargs):
        super(StressTest, self).__init__()
        self.kwargs = kwargs
        self.kwargs['mode'] = self.kwargs.get('mode', self.defaults.get('mode'))

        self.kwargs['workers'] = self.kwargs.get('workers', 1)
        self.kwargs['load'] = self.kwargs.get('load', 100)
        self.kwargs['duration'] = self.kwargs.get('duration', '')
        self.kwargs['size'] = self.kwargs.get('size', '10')

        self.kwargs['labels'] = self.kwargs.get('labels', {})

    @property
    def defaults(self) -> dict:
        return {
            "mode": "all",
            "workers": 1
        }

    def api_resources(self):
        return {"group": 'chaos-mesh.org', "version": 'v1alpha1', "plural": "stresschaos"}
