import httpx
from tools.fakers import get_random_email

payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user = httpx.post("http://localhost:8000/api/v1/users", json=payload)
create_user_data = create_user.json()
print(create_user_data)

login_payload = {
    "email": create_user_data['user']['email'],
    "password": payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_data = login_response.json()
print('Login data:', login_data)

access_token = login_data['token']['accessToken']
headers = {'Authorization': f'Bearer {access_token}'}

user_id = create_user_data['user']['id']
patch_payload = {
    "email": "user@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
patch_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{user_id}",
    json=patch_payload,
    headers=headers
)
print(patch_response.json())