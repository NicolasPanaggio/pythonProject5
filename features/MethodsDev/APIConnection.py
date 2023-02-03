import requests
import json
import jsonpath

# API URL
url = "https://gorest.co.in/public/v2/users"

# GET Request
response = requests.get(url)

# Transform
response_content = response.content

# Parse response to Json format
json_response = json.loads(response.text)

# Fetch value using Json Path
name_for_assert_letter = jsonpath.jsonpath(json_response, 'name')

# Format to assert
format_json = json.dumps(response.text)
