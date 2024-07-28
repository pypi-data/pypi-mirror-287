from pandas import DataFrame


def transform_dataframe_to_latex_ready(data: DataFrame, **kwargs) -> DataFrame:
    r"""Iterates through the column names and tries to find the corresponding error column.
    If it is found, both columns will be put together into a new column. It uses the LaTeX `SIUnitx`
    package to format the numbers with uncertainties correctly inside the table.

    :param data: DataFrame to be transformed into other data that can be made into a string to work with LaTeX tables.
    :param error_marker: Defines a list of all string suffixes that mark a column of uncertainties. The default value
    is ["err", "error", "fehler", "Err", "Error", "Fehler"].
    :param columns: If a Key corresponds to a column of the data, that column will be renamed to the given value.
    :param ignore_rest: If set to true, every column of the data that is not a key in the `columns` keyword argument
    will be dropped in the resulting DataFrame. The default value is `False`.
    :param is_table_num: If false, numbers will not be inserted in the tablenum macro but the num macro instead.
    Default value is `True`.
    :param siunitx_column_option: For every column that is a key in the given dictionary,
    the value is inserted as an option for the tablenum macro.

    :return: Formatted DataFrame
    """
    ...
