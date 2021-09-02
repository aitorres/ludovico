"""
Main module for Ludovico, the opinionated DataFrame-to-TeX table generator.
"""

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
