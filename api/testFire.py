from flask import Blueprint, render_template
from flask import current_app as app

from pathlib import Path
import time

from core import api

pluginPages = Blueprint('testFirePages', __name__, template_folder="templates")

@pluginPages.route("/testFire/")
def mainPage():
    return { "result" : "Hello World" }, 200
