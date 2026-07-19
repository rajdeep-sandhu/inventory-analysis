# equipment.py
from io import BytesIO

import marimo as mo
import polars as pl


def file_element():
    """Return a file element for Equipment Transaction Data"""
    element = mo.ui.file(
        label="Upload Equipment Transaction Data (`.xlsx`)",
        filetypes=[".xlsx"],
        multiple=False,
    )

    return element


def file_element_to_stream(file_element) -> dict:
    """
    Returns the filename and a BytesIO stream from a mo.ui.file element.

    params:
    file_input: mo.ui.file element.
    """

    # Get first result for single file upload
    result = file_element.value[0]
    filename: str = result.name
    content: bytes = result.contents
    file_stream = BytesIO(content)

    return {"filename": filename, "file_stream": file_stream}


def file_element_to_df(file_element) -> tuple[str | None, pl.DataFrame | None]:
    """
    Return ux_trans DataFrame from mo.ui.file element
    """
    upload_result: dict | None = None
    filename: str | None = None
    df: pl.DataFrame | None = None

    if file_element.value:
        upload_result = file_element_to_stream(file_element)
        filename = upload_result["filename"]
        file_stream = upload_result["file_stream"]
        df = pl.read_excel(source=file_stream)

    message: str = (
        f"File: `{filename}` uploaded."
        if filename
        else "No file uploaded."
    )
    mo.output.replace(mo.md(message))

    return filename, df
