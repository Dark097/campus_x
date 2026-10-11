
#  manual type validation and data validation------------------------
# def insert_patient_data(name: str, age: int):

#     if type(name) == str and type(age) == int:
#         if age < 0:
#             raise ValueError('Age cannot be negative')
#         print(name)
#         print(age)
#         print('inserted into database')

#     else:
#         raise TypeError('Incorrect data type')

# insert_patient_data('nitish', -1)


# type validation using pydantic--------------------------

# from pydantic import BaseModel
# from typing import Dict,List,Optional
# class Patient (BaseModel):

#     name:str
#     age:int
#     weight:Optional[float]=None
#     married:bool=None
#     contact_details:Dict[str,str]
#     allergis:List[str]

# def insert_patient(patient:Patient):

#     print(patient.name)
#     print(patient.age) 
#     print(patient.weight) 
#     print('inserted into database')

# patient_info={"name":"nitish","age":30,'weight':70.5,'married':True,'contact_details':{'email':'nitish@example.com','phone':'123-456-7890'},'allergis':['peanuts']}
# patient1=Patient(**patient_info)
# insert_patient(patient1)


# type validation and data validation  using pydantic--------------------------

from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import Dict,List,Optional,Annotated
class Patient (BaseModel):

    name:Annotated[str,Field(max_length=100, description='name of person',examples=['nitish','john'])]
    age:Annotated[int,Field(gt=0,description='age of person',examples=[30,25])]
    weight:Annotated[Optional[float],Field(default=None,strict=True,gt=0,description='weight of person',examples=[70.5,65.2])]
    married:bool=None
    linkedin:Annotated[AnyUrl,Field(description='linkedin profile url',examples=['https://www.linkedin.com/in/nitish-kumar-123456789/'])]
    email:Annotated[EmailStr,Field(description='email of person',examples=['nitish@example.com'])]
    contact_details:Dict[str,str]
    allergis:Annotated[List[str],Field(max_length=5,description='list of allergis',examples=[['peanuts','dust']])]

def insert_patient(patient:Patient):

    print(patient.name)
    print(patient.age) 
    print(patient.weight) 
    print(patient.linkedin)
    print(patient.email)
    print(patient.contact_details)
    print(patient.allergis)
    print('inserted into database')

patient_info={"name":"nitish","age":30,'weight':70.5,'married':True,'email':'nitish@example.com','contact_details':{'phone':'123-456-7890'},'allergis':['peanuts'],'linkedin':'https://www.linkedin.com/in/nitish-kumar-123456789/'}
patient1=Patient(**patient_info)
insert_patient(patient1)
