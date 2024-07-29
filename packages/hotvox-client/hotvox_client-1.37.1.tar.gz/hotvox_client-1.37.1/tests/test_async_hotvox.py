'''
Tests for the HotvoxAsync class
'''

from openai import AsyncOpenAI
from hotvox_client import AsyncHotvox

def test_inheritance():
    '''
    Test that HotvoxAsync inherits from OpenAIAsync
    '''
    assert issubclass(AsyncHotvox, AsyncOpenAI)

def test_init():
    '''
    Test that the HotvoxAsync class can be initialized
    Even without a connection this should not raise an error
    '''
    hv = AsyncHotvox()
    assert hv is not None

def test_base_url():
    '''
    Test that the base URL is set correctly
    '''
    hv = AsyncHotvox()
    assert str(hv.base_url) == "http://openai.hotvox.local/v1/"
