from core.models import trigger


class _testFireTrigger(trigger._trigger):
    events = list()

    def check(self):
        self.result["events"] = self.events
