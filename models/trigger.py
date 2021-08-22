from core.models import trigger


class _testFireTrigger(trigger._trigger):
    events = [1]

    def check(self):
        self.result["events"] = self.events
