import time

from core import auth

from core.models import action, webui

class _testFire(action._action):
    #class _properties(webui._properties):
    #    def generate(self,classObject):
    #        formData = []
    #        formData.append({"type" : "input", "schemaitem" : "name", "textbox" : classObject.name})
    #        formData.append({"type" : "input", "schemaitem" : "logicString", "textbox" : classObject.logicString})
    #        formData.append({"type" : "input", "schemaitem" : "delay", "textbox" : classObject.delay})
    #        formData.append({"type" : "checkbox", "schemaitem" : "enabled", "checked" : classObject.enabled})
    #        return formData

    delay = int()
    crash = bool()
    rc = int()
    resultBool = bool()
    password = str()

    def setAttribute(self,attr,value):
        if attr == "password" and not value.startswith("ENC "):
            self.password = "ENC {0}".format(auth.getENCFromPassword(value))
            return True
        return super(_testFire, self).setAttribute(attr,value)

    def run(self,data,persistentData,actionResult):
        print("Fire!, data={0}".format(data))
        if self.delay > 0:
            time.sleep(self.delay)
        if self.crash:
            a = int("aaa")
        if "ENC" in self.password:
            actionResult["data"] = auth.getPasswordFromENC(self.password)
        actionResult["result"] = self.resultBool 
        actionResult["rc"] = self.rc
        return actionResult 
