from abc import ABC
from dataclasses import asdict

from chaosmesh.k8s.experiment import ChaosExperiment


class JVMFault(ChaosExperiment, ABC):

    def __init__(self, **kwargs):
        super(JVMFault, self).__init__(**kwargs)

    @property
    def defaults(self):
        yield

    def action(self) -> str:
        pass

    def api_resources(self):
        return {"group": 'chaos-mesh.org', "version": 'v1alpha1', "plural": "jvmchaos"}

    def spec(self, namespace, name) -> dict:
        return {
            "selector": asdict(self.kwargs['selector']),
            "mode": self.kwargs.get('mode'),
            "duration": self.kwargs.get('duration'),
            "action": self.action(),
            "name": name,
            "class": self.kwargs.get('targetClass'),
            "method": self.kwargs.get('method'),
            "value": self.kwargs.get('value'),
            "exception": self.kwargs.get('exception'),
            "latency": self.kwargs.get('latency'),
            "cpuCount": self.kwargs.get('cpuCount'),
            "memType": self.kwargs.get('memType'),
            "port": self.kwargs['port'],
            "ruleData": self.kwargs['ruleData'],
        }
