# equipment.py
from io import BytesIO

import marimo as mo


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
