#!/usr/bin/env python3

from aws_cdk import core

from cdk_bolt_hello_world.cdk_bolt_hello_world_stack import CdkBoltHelloWorldStack


app = core.App()
CdkBoltHelloWorldStack(app, "cdk-bolt-hello-world", env={'region': 'us-west-2'})

app.synth()
