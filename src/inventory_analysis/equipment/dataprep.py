# equipment.py
import marimo as mo


def file_element():
    """Return a file element for Equipment Transaction Data"""
    element = mo.ui.file(
        label="Upload Equipment Transaction Data (`.xlsx`)",
        filetypes=[".xlsx"],
        multiple=False,
    )

    return element
