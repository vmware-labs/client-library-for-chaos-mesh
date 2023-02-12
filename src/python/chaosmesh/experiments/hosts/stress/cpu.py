from chaosmesh.experiments.hosts.stress import StressTest


class HostsStressCPU(StressTest):

    def __init__(self, **kwargs):
        super(HostsStressCPU, self).__init__(**kwargs)

    def action(self) -> str:
        return "stress-cpu"

    def validate(self):
        assert self.kwargs['address'] is not None, "address cannot be None"

        assert self.kwargs['load'] is not None, "load cannot be None"
        assert isinstance(self.kwargs['load'], int), "load type should be int"

        assert self.kwargs['workers'] is not None, "workers cannot be None"

    def spec(self, namespace, name):
        return {
            "action": self.action(),
            "address": self.kwargs['address'],
            "mode": self.kwargs.get('mode'),
            "stress-cpu": {
                "load": self.kwargs['load'],
                "workers": self.kwargs['workers']
            },
            "duration": self.kwargs['duration']
        }
