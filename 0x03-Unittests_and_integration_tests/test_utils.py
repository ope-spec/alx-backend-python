#!/usr/bin/env python3
"""
Test cases for the access_nested_map function.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map:
                               dict, path: tuple, expected_result: any):
        """
        Test the access_nested_map function.
        """
        self.assertEqual(access_nested_map(nested_map,
                                           path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError, "Key not found: 'a'"),
        ({"a": 1}, ("a", "b"), KeyError, "Key not found: 'b'"),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map, path,
                                         expected_exception,
                                         expected_message):
        """
        Test the access_nested_map function for raising KeyError.
        """
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase):

    @patch('utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test the get_json function with mocked requests.get.
        """
        # Create a Mock object with a json method that returns the test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Patch requests.get to return the mock_response
        with patch('utils.requests.get',
                   return_value=mock_response) as mock_get:
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):

    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        """
        Test the memoize decorator.
        """
        # Create an instance of TestClass
        test_instance = self.TestClass()

        # Call a_property twice
        result1 = test_instance.a_property()
        result2 = test_instance.a_property()

        # Assert that a_method is called only once
        mock_a_method.assert_called_once()

        # Assert that the results are correct
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)
        self.assertEqual(result1, result2)
