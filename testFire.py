from core import plugin, model

class _testFire(plugin._plugin):
    version = 2.10

    def install(self):
        # Register models
        model.registerModel("testFire","_testFire","_action","plugins.testFire.models.action")
        model.registerModel("testFireTrigger","_testFireTrigger","_trigger","plugins.testFire.models.trigger")
        return True

    def uninstall(self):
        # deregister models
        model.deregisterModel("testFire","_testFire","_action","plugins.testFire.models.action")
        model.deregisterModel("testFireTrigger","_testFireTrigger","_trigger","plugins.testFire.models.trigger")
        return True

    def upgrade(self,LatestPluginVersion):
        if self.version < 1.9:
            model.registerModel("testFireTrigger","_testFireTrigger","_trigger","plugins.testFire.models.trigger")
