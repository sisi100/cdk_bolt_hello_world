import json
import pytest

from aws_cdk import core
from cdk_bolt_hello_world.cdk_bolt_hello_world_stack import CdkBoltHelloWorldStack


def get_template():
    app = core.App()
    CdkBoltHelloWorldStack(app, "cdk-bolt-hello-world")
    return json.dumps(app.synth().get_stack("cdk-bolt-hello-world").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
