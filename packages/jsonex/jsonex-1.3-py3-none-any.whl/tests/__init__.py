import unittest
from jsonex import JsonEx
import pandas as pd
import numpy as np
from flask import Response

class CustomType:
    def __init__(self):
        return

class TestJsonEx(unittest.TestCase):

    def test_dump_simple_data(self):
        """Test konwersji prostych danych do formatu JSON."""
        data = {'klucz': 'wartość'}
        result = JsonEx.dump(data)
        self.assertEqual(result, '{"klucz": "warto\\u015b\\u0107"}')

    def test_load_json_string(self):
        """Test ładowania ciągu JSON do obiektu Python."""
        json_string = '{"klucz": "wartość"}'
        result = JsonEx.load(json_string)
        self.assertEqual(result, {'klucz': 'wartość'})

    def test_dump_custom_type(self):
        """Test konwersji obiektów niestandardowych typów."""
        class CustomType:
            pass
        data = {'custom_obj': CustomType()}
        result = JsonEx.dump(data)
        self.assertIn('[custom type: CustomType]', result)

    def test_is_custom_type(self):
        """Test identyfikacji niestandardowych typów."""
        self.assertTrue(JsonEx._is_custom_type(CustomType()))

    def test_fix_data_with_set(self):
        """Test przekształcania danych zawierających set."""
        data = {'numbers_set': {1, 2, 3}}
        fixed_data = JsonEx._fix_data(data)
        self.assertEqual(fixed_data, {'numbers_set': [1, 2, 3]})

    def test_dataframe(self):
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })

        result = JsonEx.dump([df])
        self.assertEqual(result, '[{"A": {"0": 1, "1": 2, "2": 3}, "B": {"0": 4, "1": 5, "2": 6}}]')

    def test_numpy(self):
        array = np.array([[1, 2, 3], [4, 5, 6]])
        result = JsonEx.dump([array])
        self.assertEqual(result, '[[[1, 2, 3], [4, 5, 6]]]')

    def test_flask_Response(self):
        resp = Response('text')
        resp.status_code = 201
        resp.headers['Content-Length'] = '0'
        resp.headers['CustomData'] = 'abcd'
        resp.headers['Location'] = 'http://127.0.0.1:1234/'

        result = JsonEx.dump([resp])
        self.assertEqual(result, '[{"headers": [["Content-Type", "text/html; charset=utf-8"], ["Content-Length", "0"], ["CustomData", "abcd"], ["Location", "http://127.0.0.1:1234/"]], "status_code": 201, "content_length": 0, "status": "201 CREATED", "content_type": "text/html; charset=utf-8", "data": "b\'text\'"}]')

if __name__ == '__main__':
    unittest.main()
