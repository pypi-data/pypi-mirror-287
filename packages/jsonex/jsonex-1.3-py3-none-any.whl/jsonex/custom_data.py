def convert_dataframe_to_dict(obj):
    try:
        import pandas as pd

        if isinstance(obj, pd.DataFrame):
            return obj.to_dict()

        return obj
    except ImportError:
        return obj


def convert_numpy_to_list(obj):
    try:
        import numpy as np

        if isinstance(obj, np.ndarray):
            return obj.tolist()

        return obj
    except ImportError:
        return obj

def convert_flask_response(obj):
    try:
        from flask import Response

        if isinstance(obj, Response):
            obj = {
                'headers': obj.headers.to_wsgi_list(),
                'status_code': obj.status_code,
                'content_length': obj.content_length,
                'status': obj.status,
                'content_type': obj.content_type,
                'data': obj.data.__str__()
            }

        return obj
    except ImportError:
        return obj