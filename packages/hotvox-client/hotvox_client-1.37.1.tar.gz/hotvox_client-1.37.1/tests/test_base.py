"""
Test the base module
"""
from hotvox_client.base import NAME


def test_base():
    """
    Test that the base module is correctly configured
    """
    assert NAME == "hotvox_client"
