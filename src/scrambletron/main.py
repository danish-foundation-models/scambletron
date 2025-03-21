"""Main entry point for anonymization methods."""

import warnings
from pathlib import Path

import typer

from scrambletron.utils import create_analyzer, create_anonymizer

warnings.simplefilter(action="ignore", category=FutureWarning)


app = typer.Typer(name="PII-Removal CLI")


@app.command()
def anonymize(text: str, output: Path, language: str = "da"):
    """Anonymize a piece of text in a given language.

    Args:
        text (str): The text to be anonymized.
        output (Path): Path to save the output
        language (str, optional): Language of the text. Used for selecting relevant models. Defaults to "da".
    """
    analyzer = create_analyzer()
    analysis_result = analyzer.analyze(text, language=language)

    anonymizer = create_anonymizer()
    result = anonymizer.anonymize(
        text=text,
        analyzer_results=analysis_result,
        # operators={
        #     "DEFAULT": OperatorConfig(
        #         "entity_replacer", {"entity_mapping": entity_mapping}
        #     )
        # },
    )
    output.open(mode="w").write(result.text)


@app.command()
def anonymize_file(file: Path, output: Path, language: str = "da"):
    """Anonymize a piece of text in a given language.

    Args:
        file (Path): The text to be anonymized.
        output (Path): Path to save the output
        language (str, optional): Language of the text. Used for selecting relevant models. Defaults to "da".
    """
    text = file.open().read()

    analyzer = create_analyzer()
    analysis_result = analyzer.analyze(text, language=language)

    anonymizer = create_anonymizer()
    result = anonymizer.anonymize(
        text=text,
        analyzer_results=analysis_result,
        # operators={
        #     "DEFAULT": OperatorConfig(
        #         "entity_replacer", {"entity_mapping": entity_mapping}
        #     )
        # },
    )
    output.open(mode="w").write(result.text)
