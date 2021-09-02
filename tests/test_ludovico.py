"""
Test module for Ludovico, the opinionated DataFrame-to-TeX table generator.
"""

import pandas as pd

from ludovico import generate_simple_table


def test_generate_single_table() -> None:
    input_data = pd.DataFrame(
        columns=["Column A", "Column B", "Column C"],
        data=[
            (
                "entry 1",
                10,
                15.5,
            ),
            (
                "entry 2",
                15,
                20.5,
            ),
            (
                "entry 3",
                20,
                21.5,
            ),
            (
                "entry 4",
                12,
                0.5,
            ),
        ],
    )

    assert (
        generate_simple_table(input_data)
        == """
        \\begin{table}
            \\begin{center}
            \\caption[Table A]{Table A}
            \\label{tbl:table_a}
                \\begin{tabular}{rcl}
                \\hline
                Column A & Column B & Column C\\\\
                \\hline
        entry 1 & 10 & 15.5 \\\\
        entry 2 & 15 & 20.5 \\\\
        entry 3 & 20 & 21.5 \\\\
        entry 4 & 12 & 0.5 \\\\
                \\hline
                \\end{tabular}
            \\end{center}
        \\end{table}
        """
    )


def test_generate_single_table_with_custom_args() -> None:
    input_data = pd.DataFrame(
        columns=["Column A", "Column B", "Column C"],
        data=[
            (
                "entry 1",
                10,
                15.5,
            ),
            (
                "entry 2",
                15,
                20.5,
            ),
            (
                "entry 3",
                20,
                21.5,
            ),
            (
                "entry 4",
                12,
                0.5,
            ),
        ],
    )

    assert (
        generate_simple_table(
            input_data,
            table_name="Short Name",
            table_long_name="This is a long table name",
            table_label="label_1234",
        )
        == """
        \\begin{table}
            \\begin{center}
            \\caption[Short Name]{This is a long table name}
            \\label{tbl:label_1234}
                \\begin{tabular}{rcl}
                \\hline
                Column A & Column B & Column C\\\\
                \\hline
        entry 1 & 10 & 15.5 \\\\
        entry 2 & 15 & 20.5 \\\\
        entry 3 & 20 & 21.5 \\\\
        entry 4 & 12 & 0.5 \\\\
                \\hline
                \\end{tabular}
            \\end{center}
        \\end{table}
        """
    )
