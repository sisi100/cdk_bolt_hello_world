from settings import SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET
from slack_bolt import App

app = App(signing_secret=SLACK_SIGNING_SECRET, token=SLACK_BOT_TOKEN, process_before_response=True)


@app.message("hello")
def message_hello(message, say):
    say(f"Hey there <@{message['user']}>!")
