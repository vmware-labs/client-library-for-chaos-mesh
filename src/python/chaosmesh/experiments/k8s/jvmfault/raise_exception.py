from chaosmesh.experiments.k8s.jvmfault import JVMFault
from chaosmesh.k8s.selector import Selector


class RaiseException(JVMFault):

    def __init__(self, **kwargs):
        super(RaiseException, self).__init__(**kwargs)

    @property
    def defaults(self):
        return {
            "action": self.action(),
            "cpuCount": 0,
            "duration": "",
            "latency": 0,
            "memType": "",
            "mode": "all",
            "ruleData": "",
            "value": ""
        }

    def action(self) -> str:
        return "exception"

    def validate(self):
        assert self.kwargs['targetClass'] is not None, "`targetClass` cannot be None"
        assert self.kwargs['method'] is not None, "method cannot be None"
        assert self.kwargs['exception'] is not None, "exception cannot be None"
        assert self.kwargs['port'] is not None, "port cannot be None"

        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "invalid Selector type, should be of type k8s.selector"
