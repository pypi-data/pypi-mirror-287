import uuid
import json

from orchestra_sdk.http.http import simpleHTTP


class orcHTTP(simpleHTTP):
    def __init__(self, creds):
        baseUrl = "http://localhost:8000"
        super().__init__(baseUrl)
        self.add_default_headers({"Authorization": f"Basic {creds['apikey']}"})
        self.add_parameters({"clientid": f"{creds['clientid']}"})
        self.clientid = creds["clientid"]

    def send_message(self, correlation_id, data):
        data["correlation_id"] = correlation_id
        data["logid"] = str(uuid.uuid4())
        response = self.base_request(
            method="POST",
            endpoint="jobs/sdk/sdk_receive",
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        return response
