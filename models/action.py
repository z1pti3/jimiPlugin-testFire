import json
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
    dontSaveResult = bool()
    password = str()
    lastResult = str()

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "password" and not value.startswith("ENC "):
            if fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.password = "ENC {0}".format(auth.getENCFromPassword(value))
                return True
            return False
        return super(_testFire, self).setAttribute(attr,value,sessionData=sessionData)

    def run(self,data,persistentData,actionResult):
        if not self.dontSaveResult:
            self.lastResult = json.dumps(data)
            self.update(["lastResult"])
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
