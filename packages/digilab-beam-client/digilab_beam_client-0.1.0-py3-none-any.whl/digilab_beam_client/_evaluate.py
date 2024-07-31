import requests
import numpy as np
from typeguard import typechecked

from ._constant import EVALUATE_URL

@typechecked
def evaluate(e : float, p : float):

    payload = {
        "e": e,
        "p": p
    }

    response = requests.post(EVALUATE_URL, json=payload)

    if response.status_code == 200:

        return [np.array(i) for i in response.json()[0]]
    
    else:
        raise  requests.exceptions.HTTPError(f"Request failed with status code: {response.status_code}")