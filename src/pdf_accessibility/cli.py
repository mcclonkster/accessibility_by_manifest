from __future__ import annotations

from pathlib import Path

import typer

from pdf_accessibility.graph.build_graph import build_workflow, langgraph_available
from pdf_accessibility.persistence.runs import create_run, initial_document_state

app = typer.Typer(help="Run the v0.1.0 PDF accessibility workflow scaffold.")


@app.command()
def run(
    input_pdf: Path = typer.Argument(..., exists=True, file_okay=True, dir_okay=False),
    output_dir: Path = typer.Option(Path("runs"), "--output-dir", "-o"),
) -> None:
    context = create_run(input_pdf, output_dir)
    document = initial_document_state(context)
    result = build_workflow().invoke({"document": document})
    final_document = result["document"]
    typer.echo(f"run_dir: {context.run_dir}")
    typer.echo(f"langgraph_available: {langgraph_available()}")
    typer.echo(f"document_status: {final_document.document_status.value}")
    typer.echo(f"finalization_state: {final_document.finalization_state.value}")


def main() -> None:
    app()


if __name__ == "__main__":
    main()

