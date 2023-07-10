import os

#flask
from flask import Flask
from flask import request, g

from lib.rollbar import init_rollbar
from lib.xray import init_xray
from lib.honeycomb import init_honeycomb
from lib.cors import init_cors
from lib.cloudwatch import init_cloudwatch
from lib.helpers import model_json


from time import strftime

import routes.general
import routes.users
import routes.messages
import routes.activities

app = Flask(__name__)

# initialization -----
init_xray(app)
init_honeycomb(app)
init_cors(app)
with app.app_context():
  g.rollbar = init_rollbar(app)
  
# load routes ------
routes.general.load(app)
routes.activities.load(app)
routes.users.load(app)
routes.messages.load(app)


if __name__ == "__main__":
  app.run(debug=True)