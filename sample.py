import requests

main_url = "http://localhost:8000"

# # Testing /get_session_id
# url = main_url + "/get_session_id"
# headers = {
#     "Content-Type": "application/json"
# }
# response = requests.post(url, headers=headers)
# print(response.json())

# # Testing /ask
# url = main_url + "/ask"
# session_id = response.json().get('session_id')
# params = {"session_id": str(session_id)} 
# request_body = {"message": "tell me more how I can save money on energy?"}
# response = requests.post(url, params=params, json=request_body)
# print(response.json())

# # Testing /retrieve_contexts
# url = main_url + "/retrieve_contexts"
# params = {"session_id":"000-000"}
# headers = {
#     "Content-Type": "application/json"
# }
# response = requests.post(url, params=params, headers=headers)
# print(f"Response Status: {response.status_code}")
# print(f"Response text: {response.text}")
# print(response.json())

# # Testing /generate_summary and authorization
# url = main_url + "/generate_summary"
# headers = {
#     "Authorization": 'admin'
# }

# payload = {'session_id': '000-000',
#            'message_history': ['tell me more how I can save money on energy?']}
# response = requests.post(url, json=payload, headers=headers)
# print(response.json())

# Test for Semantic Caching 
from chain_config import get_graph

lc_graph = get_graph()

question = "What should I do to save money on my bills?"
res = lc_graph.invoke({'question': question})

print(res.get("answer"))