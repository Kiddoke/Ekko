import os
from dotenv import load_dotenv
import httpx

load_dotenv()

cerebrum_api_key = os.getenv("CEREBRUM_API_KEY")

client = httpx.Client(
    base_url="https://gw-uio.intark.uh-it.no/cerebrum/v1",
    headers={"X-Gravitee-Api-Key": cerebrum_api_key}
)

def get_person_id(username):
    response = client.get(f'/accounts/{username}')
    response.raise_for_status()

    return response.json()["owner"]["id"]

def get_group_members(group_name):

    response = client.get(f'/groups/{group_name}/members/')
    response.raise_for_status()

    group_members = response.json()["members"]

    persons = dict()

    for member in group_members:
        username = member["name"]
        persons[username] = get_person_id(username)

    return persons
    

def get_contactinfo_list(group_name):
    persons = get_group_members(group_name)
    contact_info = dict()
    
    for username, person_id in persons.items():
        response = client.get(f'/persons/{person_id}/contacts')
        response.raise_for_status()

        contacts = response.json()["contacts"]

        phone = next((contact["value"] for contact in contacts if contact["type"] in ("MOBILE", "PRIVATEMOBILE")), None)

        contact_info[username] = phone
    
    return contact_info