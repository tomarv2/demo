from click.testing import CliRunner

import os
import boto3
from moto import mock_iam
import pytest


@pytest.fixture(scope='module')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'
    os.environ['AWS_DEFAULT_REGION'] = 'us-west-2'


@pytest.fixture(scope='module')
def iam(aws_credentials):
    with mock_iam():
        yield boto3.client('iam')


def test_get_mock_iam(iam):
    # We need to create the iam entry first since this is all in Moto's 'virtual' AWS account
    iam.create_role(
        RoleName='demo_parameter',
        Description='name',
        AssumeRolePolicyDocument='/Users/varun.tomar/Documents/databricks_github/prism/app/support/data/demo-role.json'
    )
    from src.demo.cli import entrypoint
    runner = CliRunner()
    response = runner.invoke(entrypoint, ["get", "--name", "demo_parameter"])
    assert response.output == "hello world\n"

