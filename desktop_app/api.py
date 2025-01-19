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
    organizations = get_organizations()
    for organization in organizations:
        if organization["id"] == id:
            return organization
    return None

async def async_get_organization_by_id(id: int):
    return get_organization_by_id(id=id)


def find_organization(organization_name: str):
    organizations = get_organizations()
    for organization in organizations:
        if organization["title"] == organization_name:
            return organization
    return None
    


# def get_employees(*args):

#     def __get_from_organization(organization: str):
#         organizations = get_organizations()
#         print(organizations)

#     def __get_from_sub_division(sub_division: str):
#         pass

#     def __get_from_sub_sub_division(department: str):
#         sub_sub_divisions = get_sub_sub_divisions()
        
#         sub_sub_division_founded = ""

#         for sub_sub_division in sub_sub_divisions:
#             if sub_sub_division["title"] == department:
#                 sub_sub_division_founded = sub_sub_division

#         employees_id = sub_sub_division_founded["employees"]

#         return sub_sub_division_founded

#     try:
#         if len(args) == 1:
#             department = str(args[0])
#             what_is_it = department.split(".")
#             if len(what_is_it) == 2:
#                 employees = __get_from_organization(department)
#                 return employees
#             elif len(what_is_it) == 3:
#                 employees = __get_from_sub_division(department)
#                 return employees
#             elif len(what_is_it) == 4:
#                 employees = __get_from_sub_sub_division(department)
#                 return employees
#             return None
#         return None
#     except:
#         return None
    
def get_employees_by_department(department: str):
    def __get_users():
        try:
            url = "http://127.0.0.1:8000/api/V1/employees"
            response = requests.get(url)

            return response.json()
        except:
            return None
        
    users = __get_users()

    if users is not None:
        organization = None
        sub_division_id = None
        sub_sub_division_id = None

        users_found = []

        for user in users:
            try:
                organization_id = int(user["organization"])
            except:
                pass
            try:
                sub_division_id = int(user["subdivision"])
            except:
                pass
            try:
                sub_sub_division_id = int(user["sub_sub_division"])
            except:
                pass

            organization = None
            sub_division = None
            sub_sub_division = None

            if organization_id is not None:
                organization = get_organization_by_id(organization_id)

            if sub_division_id is not None:
                sub_division = get_subdivision_by_id(sub_division_id)
                
            if sub_sub_division_id is not None:
                sub_sub_division = get_sub_sub_division_by_id(sub_sub_division_id)
            try:
                if department == organization["title"] or department == sub_division["title"] or department == sub_sub_division["title"]:
                    users_found.append(user["username"])
            except:
                pass

        return users_found
    return None