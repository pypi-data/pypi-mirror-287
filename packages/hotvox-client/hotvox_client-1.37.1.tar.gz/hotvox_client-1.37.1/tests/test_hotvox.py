'''
Tests for the Hotvox class
'''

from openai import OpenAI
from hotvox_client import Hotvox

def test_inheritance():
    '''
    Test that Hotvox inherits from OpenAI
    '''
    assert issubclass(Hotvox, OpenAI)

def test_init():
    '''
    Test that the Hotvox class can be initialized
    Even without a connection this should not raise an error
    '''
    hv = Hotvox()
    assert hv is not None

def test_base_url():
    '''
    Test that the base URL is set correctly
    '''
    hv = Hotvox()
    assert str(hv.base_url) == "http://openai.hotvox.local/v1/"
