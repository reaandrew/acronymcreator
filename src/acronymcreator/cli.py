"""
Command line interface for AcronymCreator.
Provides JSON/YAML export functionality for acronym results.
"""

import json
import yaml
from datetime import datetime
import click
from .core import AcronymCreator, AcronymOptions


@click.command()
@click.argument("phrase", required=True)
@click.option(
    "--include-articles",
    is_flag=True,
    default=False,
    help="Include articles (a, an, the) in the acronym",
)
@click.option(
    "--min-length",
    type=int,
    default=2,
    help="Minimum word length to include (default: 2)",
)
@click.option("--max-words", type=int, help="Maximum number of words to process")
@click.option(
    "--lowercase", is_flag=True, default=False, help="Output acronym in lowercase"
)
@click.option(
    "--format",
    type=click.Choice(["text", "json", "yaml"], case_sensitive=False),
    default="text",
    help="Output format (default: text)"
)
@click.option(
    "--all-variations",
    is_flag=True,
    default=False,
    help="Export all variations from generate_multiple_options()"
)
@click.version_option(version="0.1.0", prog_name="acronymcreator")
def main(
    phrase,
    include_articles,
    min_length,
    max_words,
    lowercase,
    format,
    all_variations,
):
    """Generate acronyms from phrases.

    PHRASE: The phrase to create an acronym from

    Examples:

        acronymcreator "The Quick Brown Fox"

        acronymcreator "Application Programming Interface" --include-articles

        acronymcreator "Very Long Phrase With Many Words" --max-words 3

        acronymcreator "The Quick Brown Fox" --format json

        acronymcreator "The Quick Brown Fox" --format yaml --all-variations
    """
    creator = AcronymCreator()
    options = AcronymOptions(
        include_articles=include_articles,
        min_word_length=min_length,
        max_words=max_words,
        force_uppercase=not lowercase,
    )

    timestamp = datetime.now().isoformat()

    if all_variations:
        # Generate all variations
        variations = creator.generate_multiple_options(phrase)

        if not any(variations.values()):
            click.echo(
                "No acronyms could be generated from the given phrase.", err=True
            )
            raise click.Abort()

        if format.lower() == "text":
            # Text output for all variations
            click.echo(f"Input: {phrase}")
            click.echo(f"Generated: {timestamp}")
            click.echo("")

            for category, results in variations.items():
                if results:
                    category_title = category.replace('_', ' ').title()
                    click.echo(f"{category_title}: {', '.join(results)}")
        else:
            # JSON/YAML output for all variations
            output_data = {
                "input_phrase": phrase,
                "timestamp": timestamp,
                "variations": variations,
                "metadata": {
                    "include_articles": include_articles,
                    "min_length": min_length,
                    "max_words": max_words,
                    "lowercase": lowercase
                }
            }

            if format.lower() == "json":
                click.echo(json.dumps(output_data, indent=2))
            elif format.lower() == "yaml":
                click.echo(yaml.dump(output_data, default_flow_style=False))
    else:
        # Generate single result
        result = creator.create_basic_acronym(phrase, options)

        if not result:
            click.echo("No acronym could be generated from the given phrase.", err=True)
            raise click.Abort()

        if format.lower() == "text":
            click.echo(result)
        else:
            # JSON/YAML output for single result
            output_data = {
                "input_phrase": phrase,
                "acronym": result,
                "timestamp": timestamp,
                "options": {
                    "include_articles": include_articles,
                    "min_length": min_length,
                    "max_words": max_words,
                    "lowercase": lowercase
                }
            }

            if format.lower() == "json":
                click.echo(json.dumps(output_data, indent=2))
            elif format.lower() == "yaml":
                click.echo(yaml.dump(output_data, default_flow_style=False))


if __name__ == "__main__":
    main()
