import marimo

__generated_with = "0.23.14"
app = marimo.App(width="full", app_title="Equipment Analysis")


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


@app.cell
def _(mo):
    def get_data_file():
        file_input = mo.ui.file(
            label="Upload Equipment Transaction Data (`.xlsx`)",
            filetypes=[".xlsx"],
            multiple=False,
        )

        return file_input

    return (get_data_file,)


@app.cell
def _(get_data_file):
    get_data_file()
    return


if __name__ == "__main__":
    app.run()
