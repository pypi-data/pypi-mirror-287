from pathlib import Path
from typing import Annotated

import art
import typer

from promptarchitect.validate_engineered_prompts import (
    ValidateEngineeredPrompts,  # noqa: E402
)

app = typer.Typer()


@app.command()
def main(
    prompts: Annotated[str, typer.Option()] = "examples/prompts",
    completions: Annotated[str, typer.Option()] = "examples/completions",
    templates: Annotated[str, typer.Option()] = None,
    report: Annotated[str, typer.Option()] = "dashboard",
):
    """
     ____                                  _     ____                __  _
    |  _ \  _ __   ___   _ __ ___   _ __  | |_  / ___| _ __   __ _  / _|| |_
    | |_) || '__| / _ \ | '_ ` _ \ | '_ \ | __|| |    | '__| / _` || |_ | __|
    |  __/ | |   | (_) || | | | | || |_) || |_ | |___ | |   | (_| ||  _|| |_
    |_|    |_|    \___/ |_| |_| |_|| .__/  \__| \____||_|    \__,_||_|   \__|
                                   |_|
    By Aigency.com
    """
    # header = art.text2art("PromptCraft") + "By Aigency.com\n\n"

    # print(header)

    if templates is None:
        templates = Path(__file__).parent / "templates/reports"

    validation = ValidateEngineeredPrompts(
        prompts_location=prompts,
        html_templates_location=templates,
        completions_output=completions,
        reports_location=report,
    )

    # validation.clear_all_test_completions(completions_output=completions_output)
    validation.run()

    errors, warnings = validation.get_errors_and_warnings()

    if errors + warnings > 0:
        print(
            f"\033[91mErrors: {errors}\033[0m, \033[93mWarnings: {warnings}\033[0m, "  # noqa: E501
        )
        if validation.errors.duplicates > 0:
            print(
                f"\033[93mRemoved duplicate errors/warnings: {validation.errors.duplicates}\033[0m, please check the dashboard for more information."  # noqa: E501
            )


if __name__ == "__main__":
    main()
