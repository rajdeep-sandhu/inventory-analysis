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
    def file_upload_element():
        """Return a file upload element for Euipment Transaction Data"""
        file_input = mo.ui.file(
            label="Upload Equipment Transaction Data (`.xlsx`)",
            filetypes=[".xlsx"],
            multiple=False,
        )

        return file_input

    return (file_upload_element,)


@app.function
def file_to_df(file_input) -> dict:
    """
    Returns the filename and a polars dataframe from a .xlsx file uploaded via mo.ui.file.

    params:
    file_input: The file input element.
    """

    # Get first result for single file upload
    result = file_input.value[0]
    filename: str = result.name
    content: bytes = result.contents
    df: pl.DataFrame = pl.read_excel(source=BytesIO(content))

    return {"filename": filename, "data": df}


@app.cell
def _(file_upload_element):
    file_input = file_upload_element()
    file_input
    return (file_input,)


@app.cell
def _(file_input):
    upload_result: dict | None = None

    if file_input.value:
        upload_result = file_to_df(file_input)
        ux_trans_filename: str = upload_result["filename"]
        ux_trans: pl.DataFrame = upload_result["data"]
        ux_trans = ux_trans.sort(by="ID")
    return


if __name__ == "__main__":
    app.run()
