import pytest
from my_cli_tool.cli import greet

def test_greet(capsys):
    greet("John")
    captured = capsys.readouterr()
    assert captured.out == "Hello, John!\n"

def test_greet_with_bytes(capsys):
    greet(b"John")
    captured = capsys.readouterr()
    assert captured.out == "Hello, John!\n"