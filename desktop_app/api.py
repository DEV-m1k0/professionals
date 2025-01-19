import requests


def get_organizations():
    try:
        url = "http://127.0.0.1:8000/api/V1/organizations"
        response = requests.get(url)

        return response.json()
    except:
        return []
    

def get_subdivisions():
    try:
        url = "http://127.0.0.1:8000/api/V1/subdivisions"
        response = requests.get(url)

        return response.json()
    except:
        return []
    

def get_sub_sub_divisions():
    try:
        url = "http://127.0.0.1:8000/api/V1/subsubdivions"
        response = requests.get(url)

        return response.json()
    except:
        return []
    

def get_subdivision_by_id(id: int):

    subdivisions = get_subdivisions()

    for subdivision in subdivisions:
        subdivision_id = subdivision["id"]
        if subdivision_id==id:
            return subdivision
        
    return None
    

async def async_get_subdivision_by_id(id: int):
    return get_subdivision_by_id(id)


def get_sub_sub_division_by_id(id: int):

    sub_sub_divisions = get_sub_sub_divisions()

    for sub_sub_division in sub_sub_divisions:
        sub_sub_division_id = sub_sub_division["id"]
        if sub_sub_division_id==id:
            return sub_sub_division
        
    return False


async def async_get_sub_sub_division_by_id(id: int):
    return get_sub_sub_division_by_id(id)


def get_organization_by_id(id: int):
    url = f"http://127.0.0.1:8000/api/V1/organizations/{id}"
    response = requests.get(url)

    print(response.json())

    return None

async def async_get_organization_by_id(id: int):
    return get_organization_by_id(id=id)


def find_organization(organization_name: str):
    organizations = get_organizations()
    for organization in organizations:
        if organization["title"] == organization_name:
            return organization
    return None
    

    
def get_employees_by_department(department: str) -> list[dict]:
    url = f"http://127.0.0.1:8000/api/V1/employees/search/{department}"
    response = requests.get(url=url)
    return response.json()