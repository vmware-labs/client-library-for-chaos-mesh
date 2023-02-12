from chaosmesh.experiments.hosts.stress import StressTest


class HostsStressMemory(StressTest):

    def __init__(self, **kwargs):
        super(HostsStressMemory, self).__init__(**kwargs)

    def action(self) -> str:
        return "stress-mem"

    def validate(self):
        assert self.kwargs['address'] is not None, "address cannot be None"
        assert self.kwargs['size'] is not None, "size cannot be None"

    def spec(self, namespace, name):
        return {
            "action": self.action(),
            "address": self.kwargs['address'],
            "mode": self.kwargs.get('mode'),
            "stress-mem": {
                "size": self.kwargs['size']
            },
            "duration": self.kwargs['duration']
        }
