"""
Tests for the CLI module.
"""

import json
import yaml
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

    def test_cli_json_format_single_result(self):
        """Test CLI with JSON format for single result."""
        result = self.runner.invoke(main, ["Hello World", "--format", "json"])
        assert result.exit_code == 0

        data = json.loads(result.output)
        assert data["input_phrase"] == "Hello World"
        assert data["acronym"] == "HW"
        assert "timestamp" in data
        assert data["options"]["include_articles"] is False
        assert data["options"]["min_length"] == 2

    def test_cli_yaml_format_single_result(self):
        """Test CLI with YAML format for single result."""
        result = self.runner.invoke(main, ["Hello World", "--format", "yaml"])
        assert result.exit_code == 0

        data = yaml.safe_load(result.output)
        assert data["input_phrase"] == "Hello World"
        assert data["acronym"] == "HW"
        assert "timestamp" in data
        assert data["options"]["include_articles"] is False

    def test_cli_json_format_all_variations(self):
        """Test CLI with JSON format for all variations."""
        result = self.runner.invoke(
            main, ["The Quick Brown Fox", "--format", "json", "--all-variations"]
        )
        assert result.exit_code == 0

        data = json.loads(result.output)
        assert data["input_phrase"] == "The Quick Brown Fox"
        assert "timestamp" in data
        assert "variations" in data
        assert "basic" in data["variations"]
        assert "with_articles" in data["variations"]
        assert "creative" in data["variations"]
        assert "syllable" in data["variations"]
        assert "metadata" in data
        assert data["metadata"]["include_articles"] is False

    def test_cli_yaml_format_all_variations(self):
        """Test CLI with YAML format for all variations."""
        result = self.runner.invoke(
            main, ["The Quick Brown Fox", "--format", "yaml", "--all-variations"]
        )
        assert result.exit_code == 0

        data = yaml.safe_load(result.output)
        assert data["input_phrase"] == "The Quick Brown Fox"
        assert "variations" in data
        assert len(data["variations"]) == 4  # basic, with_articles, creative, syllable

    def test_cli_text_format_all_variations(self):
        """Test CLI with text format for all variations."""
        result = self.runner.invoke(main, ["The Quick Brown Fox", "--all-variations"])
        assert result.exit_code == 0
        assert "Input: The Quick Brown Fox" in result.output
        assert "Generated:" in result.output
        assert "Basic:" in result.output or "With Articles:" in result.output

    def test_cli_json_with_options(self):
        """Test CLI JSON output with various options."""
        result = self.runner.invoke(main, [
            "The Quick Brown Fox",
            "--format", "json",
            "--include-articles",
            "--min-length", "3",
            "--lowercase"
        ])
        assert result.exit_code == 0

        data = json.loads(result.output)
        assert data["options"]["include_articles"] is True
        assert data["options"]["min_length"] == 3
        assert data["options"]["lowercase"] is True

    def test_cli_yaml_with_max_words(self):
        """Test CLI YAML output with max words option."""
        result = self.runner.invoke(main, [
            "The Quick Brown Fox Jumps",
            "--format", "yaml",
            "--max-words", "3"
        ])
        assert result.exit_code == 0

        data = yaml.safe_load(result.output)
        assert data["options"]["max_words"] == 3

    def test_cli_empty_phrase_json(self):
        """Test CLI with empty phrase in JSON format."""
        result = self.runner.invoke(main, ["", "--format", "json"])
        assert result.exit_code == 1
        assert "No acronym could be generated" in result.output

    def test_cli_empty_phrase_all_variations(self):
        """Test CLI with empty phrase and all variations."""
        result = self.runner.invoke(main, ["", "--all-variations"])
        assert result.exit_code == 1
        assert "No acronyms could be generated" in result.output

    def test_cli_format_case_insensitive(self):
        """Test that format option is case insensitive."""
        result = self.runner.invoke(main, ["Hello", "--format", "JSON"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert data["acronym"] == "H"

    def test_cli_all_variations_text_output_structure(self):
        """Test that all variations text output has proper structure."""
        result = self.runner.invoke(main, ["Hello World", "--all-variations"])
        assert result.exit_code == 0
        lines = result.output.strip().split('\n')
        assert any("Input:" in line for line in lines)
        assert any("Generated:" in line for line in lines)

    def test_cli_json_variations_structure(self):
        """Test JSON variations output structure matches requirements."""
        result = self.runner.invoke(
            main, ["Test Phrase", "--format", "json", "--all-variations"]
        )
        assert result.exit_code == 0

        data = json.loads(result.output)
        # Check required top-level keys
        assert "input_phrase" in data
        assert "timestamp" in data
        assert "variations" in data
        assert "metadata" in data

        # Check variations structure
        variations = data["variations"]
        assert "basic" in variations
        assert "with_articles" in variations
        assert "creative" in variations
        assert "syllable" in variations

        # Check metadata structure
        metadata = data["metadata"]
        assert "include_articles" in metadata
        assert "min_length" in metadata
        assert "max_words" in metadata
        assert "lowercase" in metadata
