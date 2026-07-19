import marimo

__generated_with = "0.23.14"
app = marimo.App(width="full", app_title="Equipment Analysis")

with app.setup:
    from inventory_analysis.equipment import dataprep

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
def _():
    (trans_file_element := dataprep.file_element())
    return (trans_file_element,)


@app.cell
def _(trans_file_element):
    ux_trans_filename, ux_trans = dataprep.file_element_to_df(trans_file_element)
    return


if __name__ == "__main__":
    app.run()
