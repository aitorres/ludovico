"""
Main module for Ludovico, the opinionated DataFrame-to-TeX table generator.
"""

from typing import Union

import pandas as pd


def generate_simple_table(dataframe: pd.DataFrame, **options: str) -> str:
    table_name = options.get("table_name", "Table A")
    table_long_name = options.get("table_long_name", "Table A")
    table_label = options.get("table_label", "table_a")

    columns = dataframe.columns
    data = dataframe.to_dict(orient="records")

    table_header = " & ".join(columns)
    table_data = " \\\\\n        ".join(
        [" & ".join(str(row[column]) for column in columns) for row in data],
    )

    return f"""
        \\begin{{table}}
            \\begin{{center}}
            \\caption[{ table_name }]{{{ table_long_name }}}
            \\label{{tbl:{ table_label }}}
                \\begin{{tabular}}{{{ 'c' * len(columns)}}}
                \\hline
                { table_header }\\\\
                \\hline
        { table_data } \\\\
                \\hline
                \\end{{tabular}}
            \\end{{center}}
        \\end{{table}}
        """


def generate_comparison_for_two_columns(
    dataframe: pd.DataFrame,
    vertical_column: str,
    horizontal_column: str,
    data_columns: Union[str, list[str]],
    **options: str,
) -> str:
    table_name = options.get("table_name", "Table A")
    table_long_name = options.get("table_long_name", "Table A")
    table_label = options.get("table_label", "table_a")

    if isinstance(data_columns, str):
        data_columns = [data_columns]

    columns = dataframe.columns
    missing_columns = set(data_columns).union(
        {vertical_column, horizontal_column}
    ) - set(columns)

    if missing_columns:
        err = f"Column parameters not found in dataframe: {missing_columns}"
        raise ValueError(err)

    vertical_values = dataframe[vertical_column].unique().tolist()
    horizontal_values = dataframe[horizontal_column].unique().tolist()

    table_header = " & ".join([horizontal_column] + vertical_values)
    amount_data_columns = len(data_columns)

    # TODO: this works but makes no sense
    table_data = ""
    for hval in horizontal_values:
        table_row = f" \\multirow{{{amount_data_columns}}}{{*}}{{{hval}}}"

        for data_column in data_columns:
            for vval in vertical_values:
                table_row += " & " + str(
                    dataframe.loc[dataframe[horizontal_column] == hval]
                    .loc[dataframe[vertical_column] == vval]
                    .iloc[0][data_column]
                )
            table_row += " \\\\\n       "

        table_data += f"{table_row}"
    table_data = table_data[:-8]

    return f"""
        \\begin{{table}}
            \\begin{{center}}
            \\caption[{ table_name }]{{{ table_long_name }}}
            \\label{{tbl:{ table_label }}}
                \\begin{{tabular}}{{{"c" * (len(vertical_values) + 1)}}}
                \\hline
                { table_header }\\\\
                \\hline
       { table_data }
                \\hline
                \\end{{tabular}}
            \\end{{center}}
        \\end{{table}}
        """
