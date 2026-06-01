import httpx

post_data = {
  "email": "test@gmail.com",
  "password": "123456"
}
post_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=post_data)
print("Post response: ", post_response.status_code)
print("Token: ", post_response.json())

access_token = post_response.json()['token']['accessToken']
headers = {'Authorization': 'Bearer ' + access_token}
response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
print("Get response code: ", response.status_code)
print("User: ", response.json())
