'''
Test the version of hotvox_client.
'''

import io
import os
import openai

# Copied from ../setup.py
def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("hotvox_client", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content

def test_exists():
    """
    Check that the version exists and is not empty
    """
    assert read("..", "hotvox_client", "VERSION") != ""


def test_pep440():
    """
    Check that the version is PEP 440 compliant
    """
    string = read("..", "hotvox_client", "VERSION")
    parts = string.split(".")
    assert len(parts) == 3
    assert parts[0].isdigit()
    assert parts[1].isdigit()
    assert parts[2].isdigit()
    print("passed test_pep440")

def test_same_as_openai():
    """
    Check that the version is the same as the installed OpenAI version
    """
    assert read("..", "hotvox_client", "VERSION") == openai.__version__
