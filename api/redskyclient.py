import requests
import time


class RedSkyClient:
    URL = "https://redsky-uat.perf.target.com/redsky_aggregations/v1/redsky/case_study_v1?key=3yUxt7WltYG7MFKPp7uyELi1K40ad2ys&"

    def __init__(self) -> None:
        self.session = requests.Session()
        self.url = self.URL

    def get_product(self, id, retry=0):
        response = self.session.get(self.url+"&tcin="+str(id))
        if response.status_code in range(200, 300):
            return response.json()
        elif response.status_code in range(400, 500):
            return {}
        elif response.status_code in range(500, 600):
            if retry >= 5:
                return {}
            retry += 1
            time.sleep(2**retry)
            self.get_product(self, id, retry=retry)
