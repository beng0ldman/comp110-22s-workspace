"""Dictionary related utility functions."""

__author__ = "730359525"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file.
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV, rather than just strings.
    csv_reader = DictReader(file_handle)
    
    # Read each row of CSV file line by line.
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column_name: str) -> list[str]:
    """Makes a list of all values in a single column (column_name)."""
    result: list[str] = []
    for row in table:
        item: str = row[column_name]
        result.append(item)
    return result


def columnar(tablename: list[dict[str, str]]) -> dict[str, list[str]]:
    """Changing a table from list of rows into dict of columns."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = tablename[0]
    for column in first_row:
        result[column] = column_values(tablename, column)
    return result


def head(data: dict[str, list[str]], head_count: int) -> dict[str, list[str]]:
    """Evaluates the first head_count lines of data to check that your coding is good."""
    resulting_dict: dict[str, list[str]] = {}
    for column in data:
        first_list: list[str] = []
        i: int = 0
        for item in data[column]:
            if i < head_count:
                first_list.append(item)
                i = i + 1
        resulting_dict[column] = first_list
    return resulting_dict


def select(data: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Makes a column-based table with only specific columns taken from the original data (identified by key names)."""
    result: dict[str, list[str]] = {}
    for column in data:
        if column in columns:
            result[column] = data[column]
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two-column based tables into one."""
    result: dict[str, list[str]] = {}
    for column in table_one:
        result[column] = table_one[column]
    for column_2 in table_two:
        if column_2 in result:
            result[column_2] = result[column_2] + table_two[column_2]
        else:
            result[column_2] = table_two[column_2]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Determines the frequency of str values within a list."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] = result[item] + 1
        else:
            result[item] = 1
    return result
