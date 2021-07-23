import boto3

SSM_PARAMETER_NAMES = ["/cdk_bolt_hello_world/slack_bot_token", "/cdk_bolt_hello_world/slack_signing_secret"]

SLACK_BOT_TOKEN = ""
SLACK_SIGNING_SECRET = ""

ssm = boto3.client("ssm")

# CDKだと`get_parameters_by_path`非推奨っぽいので1つづつ取得する
for param_name in SSM_PARAMETER_NAMES:
    parameter = ssm.get_parameter(Name=param_name, WithDecryption=True)["Parameter"]
    if "slack_bot_token" in parameter["Name"]:
        SLACK_BOT_TOKEN = parameter["Value"]
    if "slack_signing_secret" in parameter["Name"]:
        SLACK_SIGNING_SECRET = parameter["Value"]
