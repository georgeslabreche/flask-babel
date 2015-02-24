from flask import render_template
from flask.views import View
from flask.ext.babel import gettext


class Hello(View):
    def dispatch_request(self):
    	message = gettext('Bonjour')
        return message
