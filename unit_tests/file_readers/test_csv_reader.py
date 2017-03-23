import unittest
import os
import pandas as pd
from simple_file_etl.file_readers.csv_reader import read_file as read_csv_file
from unit_tests.file_readers.test_files import TEST_FILES_DIR


class TestCsvReaderSimpleValidCases(unittest.TestCase):

    # TODO: these test cases are too crude, we need to set better expectations: check that the data is as in the
    # TODO: test files.

    def test_comma_separated_file_no_header(self):
        df = read_csv_file(os.path.join(TEST_FILES_DIR, 'comma_separated_no_header.csv'), delimiter=",", header=False)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), 2)

    def test_comma_separated_file_no_header_incorrect_header(self):
        df = read_csv_file(os.path.join(TEST_FILES_DIR, 'comma_separated_no_header.csv'), delimiter=",", header=True)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), 1)

    def test_semicolon_separated_file(self):
        df = read_csv_file(os.path.join(TEST_FILES_DIR, 'semicolon_separated_no_header.csv'), delimiter=";", header=False)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), 2)

    def test_semicolon_separated_file_no_header(self):
        df = read_csv_file(os.path.join(TEST_FILES_DIR, 'semicolon_separated_no_header.csv'), delimiter=";", header=False)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), 2)

    def test_semicolon_separated_file_no_header_incorrect_header(self):
        df = read_csv_file(os.path.join(TEST_FILES_DIR, 'semicolon_separated_no_header.csv'), delimiter=";", header=True)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), 1)

