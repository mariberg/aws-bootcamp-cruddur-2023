from flask import request, g
from lib.cognito_jwt_token import jwt_required

from aws_xray_sdk.core import xray_recorder
from flask_cors import cross_origin

from services.home_activities import *
from services.notifications_activities import *
from services.create_activity import *
from services.search_activities import *
from services.show_activity import *
from services.create_reply import *

# route helpers
from lib.helpers import model_json


def load(app):
    def default_home_feed(e):
        app.logger.debug(e)
        app.logger.debug("unauthenticated")
        data = HomeActivities.run()
        return data, 200


    @app.route("/api/activities/home", methods=['GET'])
    #@xray_recorder.capture('activities_home')
    @jwt_required(on_error=default_home_feed)
    def data_home():
        data = HomeActivities.run(cognito_user_id=g.cognito_user_id)
        return data, 200

    @app.route("/api/activities/notifications", methods=['GET'])
    def data_notifications():
        data = NotificationsActivities.run()
        return data, 200

    @app.route("/api/activities/search", methods=['GET'])
    def data_search():
        term = request.args.get('term')
        model = SearchActivities.run(term)
        return model_json(model)

    @app.route("/api/activities", methods=['POST','OPTIONS'])
    @cross_origin()
    @jwt_required
    def data_activities():
        message = request.json['message']
        ttl = request.json['ttl']
        model = CreateActivity.run(message, g.cognito_user_id, ttl)
        return model_json(model)

    @app.route("/api/activities/<string:activity_uuid>", methods=['GET'])
    #@xray_recorder.capture('activities_show')
    def data_show_activity(activity_uuid):
        data = ShowActivity.run(activity_uuid=activity_uuid)
        return data, 200

    @app.route("/api/activities/<string:activity_uuid>/reply", methods=['POST','OPTIONS'])
    @cross_origin()
    def data_activities_reply(activity_uuid):
        user_handle  = 'Marik'
        message = request.json['message']
        model = CreateReply.run(message, user_handle, activity_uuid)
        return model_json(model)

    if __name__ == "__main__":
        app.run(debug=True)