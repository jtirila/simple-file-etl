import pandas as pd


def read_file(path, delimiter, header=None):
    """Read a CSV file. TODO: We are enforcing a little bit stricter syntax for delimiter,
    and a bit looser for header, than Pandas does. Consider these requirements. Also consider stuff
    like receiving a DataFrame index as a parameter etc.

    :param path: the path of the file to read
    :param delimiter: the character that separates the fields in the CSV
    :param header: bool, true for header in the first line and None for no header
    :return: a Pandas DataFrame
    """
    assert delimiter is not None
    if header:
        header = 0
    else:
        header = None
    return pd.read_csv(path, delimiter=delimiter, header=header)




