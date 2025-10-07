"""
Tests for the CLI module.
"""

import csv
import io
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

    def test_cli_csv_output_basic(self):
        """Test CLI with CSV output format."""
        result = self.runner.invoke(main, ["Hello World", "--format", "csv"])
        assert result.exit_code == 0

        # Parse CSV output
        csv_reader = csv.DictReader(io.StringIO(result.output))
        rows = list(csv_reader)

        assert len(rows) == 1
        assert rows[0]["phrase"] == "Hello World"
        assert rows[0]["acronym"] == "HW"
        assert rows[0]["include_articles"] == "false"
        assert rows[0]["min_word_length"] == "2"
        assert rows[0]["max_words"] == ""
        assert rows[0]["lowercase"] == "false"

    def test_cli_csv_output_with_articles(self):
        """Test CLI with CSV output and include-articles option."""
        result = self.runner.invoke(
            main, ["The Quick Brown Fox", "--format", "csv", "--include-articles"]
        )
        assert result.exit_code == 0

        # Parse CSV output
        csv_reader = csv.DictReader(io.StringIO(result.output))
        rows = list(csv_reader)

        assert len(rows) == 1
        assert rows[0]["phrase"] == "The Quick Brown Fox"
        assert rows[0]["acronym"] == "TQBF"
        assert rows[0]["include_articles"] == "true"
        assert rows[0]["min_word_length"] == "2"
        assert rows[0]["lowercase"] == "false"

    def test_cli_csv_output_lowercase(self):
        """Test CLI with CSV output and lowercase option."""
        result = self.runner.invoke(
            main, ["Hello World", "--format", "csv", "--lowercase"]
        )
        assert result.exit_code == 0

        # Parse CSV output
        csv_reader = csv.DictReader(io.StringIO(result.output))
        rows = list(csv_reader)

        assert len(rows) == 1
        assert rows[0]["acronym"] == "hw"
        assert rows[0]["lowercase"] == "true"

    def test_cli_csv_output_all_options(self):
        """Test CLI with CSV output and all options."""
        result = self.runner.invoke(
            main,
            [
                "The Quick Brown Fox Jumps",
                "--format",
                "csv",
                "--include-articles",
                "--lowercase",
                "--min-length",
                "3",
                "--max-words",
                "3",
            ],
        )
        assert result.exit_code == 0

        # Parse CSV output
        csv_reader = csv.DictReader(io.StringIO(result.output))
        rows = list(csv_reader)

        assert len(rows) == 1
        assert rows[0]["phrase"] == "The Quick Brown Fox Jumps"
        assert rows[0]["include_articles"] == "true"
        assert rows[0]["min_word_length"] == "3"
        assert rows[0]["max_words"] == "3"
        assert rows[0]["lowercase"] == "true"

    def test_cli_csv_output_special_characters(self):
        """Test CLI with CSV output handling special characters."""
        result = self.runner.invoke(main, ['Hello, World! "Test"', "--format", "csv"])
        assert result.exit_code == 0

        # Parse CSV output - CSV library should handle special characters
        csv_reader = csv.DictReader(io.StringIO(result.output))
        rows = list(csv_reader)

        assert len(rows) == 1
        assert rows[0]["acronym"] == "HWT"

    def test_cli_csv_output_header_structure(self):
        """Test CSV header structure matches expected columns."""
        result = self.runner.invoke(main, ["Test Phrase", "--format", "csv"])
        assert result.exit_code == 0

        lines = result.output.strip().split("\n")
        header = lines[0]

        # Check that header contains all expected columns
        expected_columns = [
            "phrase",
            "acronym",
            "include_articles",
            "min_word_length",
            "max_words",
            "lowercase",
        ]
        for column in expected_columns:
            assert column in header
