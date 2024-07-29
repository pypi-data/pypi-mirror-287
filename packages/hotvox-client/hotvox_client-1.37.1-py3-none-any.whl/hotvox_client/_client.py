'''
This module contains the client classes to interact with Hotvox's OpenAI-conformant API.
'''
from openai import OpenAI, AsyncOpenAI

OPENAI_BASE_URL = "http://openai.hotvox.local/v1/"
OPENAI_API_KEY = "hotvox-api-key" # Dummy API key

class Hotvox(OpenAI):
    '''
    Instantiates an OpenAI client to interact with a local Hotvox server.
    '''
    def __init__(self):
        super().__init__(base_url=OPENAI_BASE_URL, api_key=OPENAI_API_KEY)


class AsyncHotvox(AsyncOpenAI):
    '''
    Instantiates an AsyncOpenAI client to interact with a local Hotvox server.
    '''
    def __init__(self):
        super().__init__(base_url=OPENAI_BASE_URL, api_key=OPENAI_API_KEY)
