# tests/test_cli.py

import click.testing
from src.cli.main import cli


def test_hello():
    runner = click.testing.CliRunner()
    result = runner.invoke(cli, ["hello"])
    assert result.exit_code == 0
    assert result.output.strip() == "Hello World!"

    result = runner.invoke(cli, ["hello", "--name", "Doge"])
    assert result.exit_code == 0
    assert result.output.strip() == "Hello Doge!"
