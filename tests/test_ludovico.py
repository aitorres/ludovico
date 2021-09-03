"""
Test module for Ludovico, the opinionated DataFrame-to-TeX table generator.
"""

import pandas as pd

from ludovico import generate_simple_table, generate_comparison_for_two_columns


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
                \\begin{tabular}{ccc}
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
                \\begin{tabular}{ccc}
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


def test_generate_comparison_for_two_columns() -> None:
    input_data = pd.DataFrame(
        columns=["Vertical Name", "Horizontal Attribute", "Data 1", "Data 2"],
        data=[
            (
                "entry 1",
                "attribute 1",
                10,
                15.5,
            ),
            (
                "entry 1",
                "attribute 2",
                10,
                15.5,
            ),
            (
                "entry 2",
                "attribute 1",
                15,
                20.5,
            ),
            (
                "entry 2",
                "attribute 2",
                5,
                20.5,
            ),
            (
                "entry 3",
                "attribute 1",
                20,
                21.5,
            ),
            (
                "entry 3",
                "attribute 2",
                20,
                22.5,
            ),
        ],
    )

    assert (
        generate_comparison_for_two_columns(
            input_data,
            "Vertical Name",
            "Horizontal Attribute",
            ["Data 1", "Data 2"],
        )
        == """
        \\begin{table}
            \\begin{center}
            \\caption[Table A]{Table A}
            \\label{tbl:table_a}
                \\resizebox{1.0\\columnwidth}{!}{%
                \\begin{tabular}{cccc}
                \\hline
                Horizontal Attribute & entry 1 & entry 2 & entry 3\\\\
                \\hline
        \\multirow{2}{*}{attribute 1} & 10 & 15 & 20 \\\\
        & 15.5 & 20.5 & 21.5 \\\\
        \\multirow{2}{*}{attribute 2} & 10 & 5 & 20 \\\\
        & 15.5 & 20.5 & 22.5 \\\\
                \\hline
                \\end{tabular}%
                }
            \\end{center}
        \\end{table}
        """
    )


def test_generate_comparison_for_two_columns_with_highlights() -> None:
    input_data = pd.DataFrame(
        columns=["Vertical Name", "Horizontal Attribute", "Data 1", "Data 2"],
        data=[
            (
                "entry 1",
                "attribute 1",
                450,
                15.5,
            ),
            (
                "entry 1",
                "attribute 2",
                10,
                14.5,
            ),
            (
                "entry 2",
                "attribute 1",
                15,
                20.5,
            ),
            (
                "entry 2",
                "attribute 2",
                5,
                20.5,
            ),
            (
                "entry 3",
                "attribute 1",
                20,
                21.5,
            ),
            (
                "entry 3",
                "attribute 2",
                20,
                22.5,
            ),
        ],
    )

    assert (
        generate_comparison_for_two_columns(
            input_data,
            "Vertical Name",
            "Horizontal Attribute",
            ["Data 1", "Data 2"],
            data_highlight={
                "Data 1": "max",
                "Data 2": "min",
            },
        )
        == """
        \\begin{table}
            \\begin{center}
            \\caption[Table A]{Table A}
            \\label{tbl:table_a}
                \\resizebox{1.0\\columnwidth}{!}{%
                \\begin{tabular}{cccc}
                \\hline
                Horizontal Attribute & entry 1 & entry 2 & entry 3\\\\
                \\hline
        \\multirow{2}{*}{attribute 1} & \\textbf{450} & 15 & 20 \\\\
        & 15.5 & 20.5 & 21.5 \\\\
        \\multirow{2}{*}{attribute 2} & 10 & 5 & 20 \\\\
        & \\textbf{14.5} & 20.5 & 22.5 \\\\
                \\hline
                \\end{tabular}%
                }
            \\end{center}
        \\end{table}
        """
    )


def test_generate_comparison_for_two_columns_with_hlines() -> None:
    input_data = pd.DataFrame(
        columns=["Vertical Name", "Horizontal Attribute", "Data 1", "Data 2"],
        data=[
            (
                "entry 1",
                "attribute 1",
                450,
                15.5,
            ),
            (
                "entry 1",
                "attribute 2",
                10,
                14.5,
            ),
            (
                "entry 2",
                "attribute 1",
                15,
                20.5,
            ),
            (
                "entry 2",
                "attribute 2",
                5,
                20.5,
            ),
            (
                "entry 3",
                "attribute 1",
                20,
                21.5,
            ),
            (
                "entry 3",
                "attribute 2",
                20,
                22.5,
            ),
        ],
    )

    assert (
        generate_comparison_for_two_columns(
            input_data,
            "Vertical Name",
            "Horizontal Attribute",
            ["Data 1", "Data 2"],
            data_highlight={
                "Data 1": "max",
                "Data 2": "min",
            },
            add_hlines=True,
            table_width=0.55,
        )
        == """
        \\begin{table}
            \\begin{center}
            \\caption[Table A]{Table A}
            \\label{tbl:table_a}
                \\resizebox{0.55\\columnwidth}{!}{%
                \\begin{tabular}{cccc}
                \\hline
                Horizontal Attribute & entry 1 & entry 2 & entry 3\\\\
                \\hline
        \\multirow{2}{*}{attribute 1} & \\textbf{450} & 15 & 20 \\\\
        & 15.5 & 20.5 & 21.5 \\\\
        \\hline\\\\
        \\multirow{2}{*}{attribute 2} & 10 & 5 & 20 \\\\
        & \\textbf{14.5} & 20.5 & 22.5 \\\\
                \\hline
                \\end{tabular}%
                }
            \\end{center}
        \\end{table}
        """
    )
