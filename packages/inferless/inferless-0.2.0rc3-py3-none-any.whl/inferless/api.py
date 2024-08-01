import os
from typing import Optional, Any
import json
import threading
import requests
from functools import wraps
from .utils import create_data
from .rpc import get_rpc_payload, get_rpc_headers, get_rpc_result, get_rpc_url


def call(url: str, workspace_api_key: Optional[str] = None, data: Optional[dict] = None, callback: Optional[Any] = None,
         inputs: Optional[dict] = None, is_batch: Optional[bool] = False):
    """
    Call Inferless API
    :param url: Inferless Model API URL
    :param workspace_api_key: Inferless Workspace API Key
    :param data: Model Input Data as a dictionary, example: {"question": "What is the capital of France?", "context": "Paris is the capital of France."}
    :param callback: Callback function to be called after the response is received
    :param inputs: Model Input Data in inferless format
    :param is_batch: Whether the input is a batch of inputs, default is False
    :return: Response from the API call
    """
    try:
        if inputs is not None and data is not None:
            raise Exception("Cannot provide both data and inputs")

        if data is not None:
            inputs = create_data(data, is_batch)

        import requests
        if workspace_api_key is None:
            workspace_api_key = os.environ.get("INFERLESS_API_KEY")
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {workspace_api_key}"}
        if inputs is None:
            inputs = {}
        response = requests.post(url, data=json.dumps(inputs), headers=headers)
        if response.status_code != 200:
            raise Exception(
                f"Failed to call {url} with status code {response.status_code} and response {response.text}")
        if callback is not None:
            callback(None, response.json())
        return response.json()
    except Exception as e:
        if callback is not None:
            callback(e, None)
        else:
            raise e


def call_async(url: str, workspace_api_key: Optional[str] = None, data: Optional[dict] = None,
               callback: Any = None, inputs: Optional[dict] = None, is_batch: Optional[bool] = False):
    """
    Call Inferless API
    :param url: Inferless Model API URL
    :param workspace_api_key: Inferless Workspace API Key
    :param data: Model Input Data as a dictionary, example: {"question": "What is the capital of France?", "context": "Paris is the capital of France."}
    :param callback: Callback function to be called after the response is received
    :param inputs: Model Input Data in inferless format
    :param is_batch: Whether the input is a batch of inputs, default is False
    :return: Response from the API call
    """
    thread = threading.Thread(target=call, args=(url, workspace_api_key, data, callback, inputs, is_batch))
    thread.start()
    return thread


def method(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        payload = get_rpc_payload(func, *args, **kwargs)
        headers = get_rpc_headers()
        url = get_rpc_url()
        response = requests.post(url, headers=headers, json=payload)
        return get_rpc_result(response)

    return wrapper
