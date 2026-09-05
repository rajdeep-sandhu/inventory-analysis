import marimo

__generated_with = "0.24.0"
app = marimo.App(width="full", app_title="Equipment Analysis")

with app.setup:
    import polars as pl

    from inventory_analysis.equipment import dataprep


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
    ux_trans_filename, ux_trans = dataprep.file_element_to_df(
        trans_file_element
    )
    return (ux_trans,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Data Quality and Pre-processing
    """)
    return


@app.cell
def _(mo):
    def describe_raw_data(data: pl.DataFrame):
        data_quality_tabs: dict = {
            "ux_trans_pre": mo.ui.table(data, pagination=True, selection=None, freeze_columns_left=["ID"]),
            "describe": mo.ui.table(
                data.describe(), pagination=False, selection=None, freeze_columns_left=["statistic"]
            ),
            "schema": mo.ui.table(
                data.schema, pagination=False, selection=None
            ),
        }

        return mo.ui.tabs(data_quality_tabs)

    return


@app.cell
def _(ux_trans):
    # Highlight if input file column structure has changed
    dataprep.has_expected_columns(ux_trans)
    return


if __name__ == "__main__":
    app.run()
