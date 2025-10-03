"""
Command line interface for AcronymCreator.
"""

import json
import click
from .core import AcronymCreator, AcronymOptions

# Trigger CI build


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
    type=click.Choice(["text", "json"], case_sensitive=False),
    default="text",
    help="Output format (default: text)",
)
@click.version_option(version="0.1.0", prog_name="acronymcreator")
def main(phrase, include_articles, min_length, max_words, lowercase, format):
    """Generate acronyms from phrases.

    PHRASE: The phrase to create an acronym from

    Examples:

        acronymcreator "The Quick Brown Fox"

        acronymcreator "Application Programming Interface" --include-articles

        acronymcreator "Very Long Phrase With Many Words" --max-words 3
    """
    creator = AcronymCreator()
    options = AcronymOptions(
        include_articles=include_articles,
        min_word_length=min_length,
        max_words=max_words,
        force_uppercase=not lowercase,
    )

    result = creator.create_basic_acronym(phrase, options)

    if not result:
        click.echo("No acronym could be generated from the given phrase.", err=True)
        raise click.Abort()

    if format == "json":
        output = {
            "phrase": phrase,
            "acronym": result,
            "options": {
                "include_articles": include_articles,
                "min_word_length": min_length,
                "max_words": max_words,
                "lowercase": lowercase,
            },
        }
        # This will break tests - intentionally calling undefined variable
        click.echo(json.dumps(undefined_variable, indent=2))
    else:
        click.echo(result)


if __name__ == "__main__":
    main()
