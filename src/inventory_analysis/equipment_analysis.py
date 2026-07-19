import marimo

__generated_with = "0.23.14"
app = marimo.App(width="full", app_title="Equipment Analysis")

with app.setup:
    from io import BytesIO

    import polars as pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Equipment Transaction Analysis
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Load Equipment Transactions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Use Polars to read the data due to better `.xlsx` support than DuckDB.
    """)
    return


@app.cell
def _(mo):
    def file_element():
        """Return a file element for Equipment Transaction Data"""
        element = mo.ui.file(
            label="Upload Equipment Transaction Data (`.xlsx`)",
            filetypes=[".xlsx"],
            multiple=False,
        )

        return element

    return (file_element,)


@app.function
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


@app.cell
def _(file_element):
    (trans_file_element := file_element())
    return (trans_file_element,)


@app.cell
def _(mo):
    def file_element_to_df(file_element) -> pl.DataFrame | None:
        """
        Return ux_trans DataFrame from mo.ui.file element
        """
        upload_result: dict | None = None
        filename: str | None = None
        df: pl.DataFrame | None = None

        if file_element.value:
            upload_result = file_element_to_stream(file_element)
            filename: str = upload_result["filename"]
            file_stream = upload_result["file_stream"]
            df: pl.DataFrame = pl.read_excel(source=file_stream)

        message: str = (
            f"File: `{filename}` uploaded."
            if filename
            else "No file uploaded."
        )
        mo.output.replace(mo.md(message))

        return df

    return (file_element_to_df,)


@app.cell
def _(file_element_to_df, trans_file_element):
    ux_trans: pl.DataFrame = file_element_to_df(trans_file_element)
    return


if __name__ == "__main__":
    app.run()
