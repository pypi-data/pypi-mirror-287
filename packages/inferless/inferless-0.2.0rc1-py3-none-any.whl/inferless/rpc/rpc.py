import base64
import json
import os

import dill
from . import config_yaml
from inferless.auth.token import auth_header


def get_rpc_payload(func, *args, **kwargs):
    rpc_payload = {
        "func": func,
        "args": args,
        "kwargs": kwargs
    }

    serialized_rpc_payload = base64.b64encode(dill.dumps(rpc_payload)).decode("utf-8")
    configuration_yaml = config_yaml.get_config_yaml()
    payload = {
        "rpc_payload": serialized_rpc_payload,
        "configuration_yaml": configuration_yaml
    }
    return payload


def get_rpc_headers():
    token_header = auth_header()
    headers = token_header.update(
        {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    )
    return headers


def get_rpc_result(response):
    if response.status_code != 200:
        raise Exception(
            f"Failed to call rpc: status code {response.status_code} and response {response.text}")

    data = response.json()
    request_id = data.get("request_id")
    result = data.get("result")
    try:
        output = json.loads(base64.b64decode(base64.b64decode(result)))
        return output
    except Exception:
        raise Exception(f"Internal error occurred. Error message: {result}, Request ID for reference: {request_id}")


def get_rpc_url():
    if os.getenv("INFERLESS_ENV") == "dev":
        return "http://aab1b24401e6d40ee819a4a85da88501-394555867.us-east-1.elb.amazonaws.com/api/v1/rpc/start"

    return "https://serverless-region-v1.inferless.com/api/v1/rpc/start"
