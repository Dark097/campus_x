from pydantic import BaseModel,Field,EmailStr,AnyUrl,field_validator
from typing import Dict,List,Optional
class Patient (BaseModel):

    name:str
    age:int
    weight:Optional[float]=None
    married:bool
    contact_details:Dict[str,str]
    email:EmailStr
    linkedin:AnyUrl
    allergis:List[str]


# field validators 
    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        valid_domain=['hdfc.com','icici.com']

        domain=value.split('@')[-1]

        if domain in valid_domain:
            return value
        raise ValueError(f"Invalid email domain. Must be one of {valid_domain}")


    @field_validator('name')
    @classmethod
    def transform(cls,value):
        return value.upper()



     
def insert_patient(patient:Patient):

    print(patient.name)
    print(patient.age) 
    print(patient.weight) 
    print(patient.email)
    print(patient.linkedin)
    print('inserted into database')

patient_info={"name":"nitish","age":30,'weight':70.5,'married':True,'email':'nitish@hdfc.com','linkedin':'https://www.linkedin.com/in/nitish-kumar-123456789/','contact_details':{'phone':'123-456-7890'},'allergis':['peanuts']}
patient1=Patient(**patient_info)
insert_patient(patient1)
