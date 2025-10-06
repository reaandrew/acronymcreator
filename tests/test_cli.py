"""
Tests for the CLI module.
"""

import json
from click.testing import CliRunner
from src.acronymcreator.cli import main


class TestCLI:
    """Test cases for the CLI interface."""

    def setup_method(self):
        """Set up test fixtures."""
        self.runner = CliRunner()

    def test_cli_basic_acronym(self):
        """Test basic CLI functionality."""
        result = self.runner.invoke(main, ["Hello World"])
        assert result.exit_code == 0
        assert result.output.strip() == "HW"

    def test_cli_with_articles_excluded(self):
        """Test CLI with articles excluded by default."""
        result = self.runner.invoke(main, ["The Quick Brown Fox"])
        assert result.exit_code == 0
        assert result.output.strip() == "QBF"

    def test_cli_with_articles_included(self):
        """Test CLI with articles included."""
        result = self.runner.invoke(main, ["The Quick Brown Fox", "--include-articles"])
        assert result.exit_code == 0
        assert result.output.strip() == "TQBF"

    def test_cli_lowercase_output(self):
        """Test CLI with lowercase output."""
        result = self.runner.invoke(main, ["hello world", "--lowercase"])
        assert result.exit_code == 0
        assert result.output.strip() == "hw"

    def test_cli_empty_phrase(self):
        """Test CLI with empty phrase that produces no result."""
        result = self.runner.invoke(main, [""])
        assert result.exit_code == 1
        assert "No acronym could be generated" in result.output

    def test_cli_help(self):
        """Test CLI help output."""
        result = self.runner.invoke(main, ["--help"])
        assert result.exit_code == 0
        assert "Generate acronyms from phrases" in result.output
        assert "PHRASE" in result.output

    def test_cli_version(self):
        """Test CLI version output."""
        result = self.runner.invoke(main, ["--version"])
        assert result.exit_code == 0
        assert "0.1.0" in result.output

    def test_cli_json_output(self):
        """Test CLI with JSON output format."""
        result = self.runner.invoke(main, ["Hello World", "--format", "json"])
        assert result.exit_code == 0
        output = json.loads(result.output)
        assert output["phrase"] == "Hello World"
        assert output["acronym"] == "HW"
        assert "options" in output

    def test_cli_json_output_with_options(self):
        """Test CLI with JSON output and various options."""
        result = self.runner.invoke(
            main,
            [
                "The Quick Brown Fox",
                "--format",
                "json",
                "--include-articles",
                "--min-length",
                "1",
            ],
        )
        assert result.exit_code == 0
        output = json.loads(result.output)
        assert output["phrase"] == "The Quick Brown Fox"
        assert output["acronym"] == "TQBF"
        assert output["options"]["include_articles"] is True
        assert output["options"]["min_word_length"] == 1

    def test_cli_yaml_output(self):
        """Test CLI with YAML output format."""
        result = self.runner.invoke(main, ["Hello World", "--format", "yaml"])
        assert result.exit_code == 0
        assert "phrase: Hello World" in result.output
        assert "acronym: HW" in result.output
        assert "options:" in result.output

    def test_cli_yaml_output_with_options(self):
        """Test CLI with YAML output and various options."""
        result = self.runner.invoke(
            main,
            [
                "The Quick Brown Fox",
                "--format",
                "yaml",
                "--include-articles",
                "--lowercase",
            ],
        )
        assert result.exit_code == 0
        assert "phrase: The Quick Brown Fox" in result.output
        assert "acronym: tqbf" in result.output
        assert "include_articles: true" in result.output
        assert "lowercase: true" in result.output
