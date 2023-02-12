from abc import ABC

from chaosmesh.experiments.k8s.jvmfault import JVMFault
from chaosmesh.k8s.selector import Selector


class GC(JVMFault, ABC):

    def __init__(self, **kwargs):
        super(GC, self).__init__(**kwargs)

    @property
    def defaults(self):
        return {
            "action": self.action(),
            "class": "",
            "cpuCount": 0,
            "duration": "",
            "exception": "",
            "latency": 0,
            "memType": "",
            "method": "",
            "mode": "all",
            "ruleData": "",
            "value": "",
        }

    def action(self) -> str:
        return "gc"

    def validate(self):
        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "invalid Selector type, should be of type k8s.selector"

        assert self.kwargs['port'] is not None, "port cannot be None"
