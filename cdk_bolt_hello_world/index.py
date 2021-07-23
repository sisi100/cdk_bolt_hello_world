import awsgi
from bolt_app import app
from flask import Flask, request
from slack_bolt.adapter.flask import SlackRequestHandler

flask_app = Flask(__name__)
slack_handler = SlackRequestHandler(app)


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return slack_handler.handle(request)


def handler(event, context):
    return awsgi.response(flask_app, event, context)
