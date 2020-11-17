import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = "http://705c87cd-80d7-4bb5-bb7a-f75c1571806a.eastus.azurecontainer.io/score"

# If the service is authenticated, set the key or token
key = "kVYjbPnfB3SicMbbyJoIqP5PcKZ1yGxd"

# Two sets of data to score, so we get two results back
data = {
    "data": [
       {
      "age": 42,
      "job": "technician",
      "marital": "divorced",
      "education": "university.degree",
      "default": "no",
      "housing": "yes",
      "loan": "no",
      "contact": "cellular",
      "month": "aug",
      "day_of_week": "tue",
      "duration": 141,
      "campaign": 2,
      "pdays": 999,
      "previous": 0,
      "poutcome": "nonexistent",
      "emp.var.rate": 1.4,
      "cons.price.idx": 93.444,
      "cons.conf.idx": -36.1,
      "euribor3m": 4.968,
      "nr.employed": 5228.1
     },
    ]
}
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {"Content-Type": "application/json"}
# If authentication is enabled, set the authorization header
headers["Authorization"] = f"Bearer {key}"

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
