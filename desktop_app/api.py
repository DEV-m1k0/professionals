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


def get_sub_sub_division_by_id(id: int):

    sub_sub_divisions = get_sub_sub_divisions()

    for sub_sub_division in sub_sub_divisions:
        sub_sub_division_id = sub_sub_division["id"]
        if sub_sub_division_id==id:
            return sub_sub_division
        
    return False


def get_sub_division_by_name(name: str):
    url = f"http://127.0.0.1:8000/api/V1/subdivisions/search_name/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['id']
    return None


def get_organization_by_name(name: str):
    url = f"http://127.0.0.1:8000/api/V1/organizations/search_name/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['id']
    return None


def get_sub_sub_division_by_name(name: str):
    url = f"http://127.0.0.1:8000/api/V1/subsubdivisions/search_name/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['id']
    return None
    

def get_employees_by_department(department: str) -> list[dict]:
    url = f"http://127.0.0.1:8000/api/V1/employees/search_department/{department}"
    response = requests.get(url=url)
    return response.json()


def get_employees():
    url = "http://127.0.0.1:8000/api/V1/employees"
    response = requests.get(url)

    users = []
    for user in response.json():
        users.append(user["username"])

    return users


def get_employee_by_name(name: str):
    url = f"http://127.0.0.1:8000/api/V1/employees/search_name/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()["id"]
    else:
        return None


def get_cabinets():
    url = "http://127.0.0.1:8000/api/V1/cabinets"
    response = requests.get(url)

    cabinets = []
    for cabinet in response.json():
        cabinets.append(cabinet["title"])

    return cabinets


def get_cabinet_by_name(name: str):
    url = f"http://127.0.0.1:8000/api/V1/cabinets/{name}"
    response = requests.get(url)

    return response.json()['id']


def get_job_titles():
    url = "http://127.0.0.1:8000/api/V1/jobtitles"
    response = requests.get(url)

    job_titles = []
    for job_title in response.json():
        job_titles.append(job_title["title"])

    return job_titles


def get_job_title_by_name(name: str):
    url = f"http://127.0.0.1:8000/api/V1/jobtitles/search_name/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()["id"]
    return None