# GenAI Chat Library

Caber's GenAI Chat Library provides a convenient way to pass user sessions for GenAI applications to Caber for inspection.  
The library handles each request and associated response as a single event, similar to an API requat and response. 

After initialization, you start each request by calling the `new_request` method with the appropriate parameters.  When 
the response is received, you can then pass the response body and parameters to the `handle_response` method to complete the request.

Once the request and response have been input, call the post_event method to send the event to Caber for inspection.

## Installation

You can install the GenAI Chat Library using pip:

```bash
pip install csi-genai-chat
```

## Usage

To use the GenAI Chat Library in your code, you need to import the `MainHandler` class from the `genai_chat_lib.main` module:

```python
import csi_genai_lib as csi
```

## Creating a New Request

To create a new request, you can instantiate the MainHandler class and call the new_request method with the appropriate parameters:

```python
csi.new_request(
    context="Hello, how can I assist you today?",
    base64=False,
    hostname="chatbot.com",
    user_id="user123",
    user_type="basic",
    user_hostname_or_ip="192.168.0.1",
    user_session="session123",
    api_name="chat-api",
    query="q=hello"
)
```

The following variable parameters can be passed to the new_request method:

* context (str, bytes, bytearray  default: ''): The context or content of the request. It represents the data, message, or prompt being sent in the request.
* base64 (bool default: False): A boolean flag indicating whether the context data has been base64 encoded.
* hostname (str default: gethostname()): The hostname or IP address of the service on which the library is running.  This is used to identify the service or agent handling the user's request to Caber.
* user_id (str default: "noAuth"): The user ID associated with the request. It represents the identity of the user making the request.
* user_type (str default: "basic"): The type of user authentication used for the request.
* user_hostname_or_ip (str default: ""): The hostname or IP address the user making the request is coming from.  This is not the hostname of the service handling the request.
* user_session (str default: None): An identifier that connects multiple user request/response pairs together into a session.
* api_name (str default: 'chat-post'): If there are multiple functions or API endpoints being used on the service 'hostname', this parameter can be used to identify the specific function or endpoint being called.
* mime_type (str default: 'application/json; charset=utf-8'): The MIME type of the request and response data.
* query (str default: None): The query string parameters to be included with the user's requects if any.

## Updating the Response

After processing the request, you can update the response using the update_response method:

```python
csi.update_response(
    response="I'm here to help! How can I assist you?",
    mime_type="application/json"
)
```

The following variable parameters can be passed to the update_response method:

* response (str, bytes, bytearray  default: ''): The context or content of the request. It represents the data, message, or prompt being sent in the request.
* base64 (bool default: False): A boolean flag indicating whether the context data has been base64 encoded.
* mime_type (str default: 'application/json; charset=utf-8'): The MIME type of the request and response data.

## Posting the Event

Once the request and response have been set, you can post the event to Caber for inspection using the post_event method:

```python
csi.post_event()
```

## Configuration

The GenAI Chat Library relies on certain configuration parameters, such as the SQS queue name and other settings. Make sure to properly configure these parameters based on your environment and requirements.

## Example

Here's a complete example of using the GenAI Chat Library:

```python
from genai_chat_lib.main import MainHandler

handler = MainHandler()

handler.new_request(
    context="Hello, how can I assist you today?",
    user_id="user123",
    user_session="session123",
    api_name="chat-api"
)

# Process the request and generate a response
response = "I'm here to help! How can I assist you?"

handler.update_response(
    response=response,
    mime_type="application/json"
)

handler.post_event()
```

