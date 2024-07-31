import requests
import numpy as np
from typeguard import typechecked

from ._constant import GET_MESH_URL

@typechecked
def get_mesh():

    response = requests.get(GET_MESH_URL)

    if response.status_code == 200:

        return [np.array(i) for i in response.json()[0]]
    
    else:
        raise  requests.exceptions.HTTPError(f"Request failed with status code: {response.status_code}")