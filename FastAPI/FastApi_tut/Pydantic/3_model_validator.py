from pydantic import BaseModel,Field,EmailStr,AnyUrl,field_validator,model_validator
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


#  model validators
    @model_validator(mode='after')
    @classmethod
    def validate_emergency_contacts(cls,model):
        if model.age>60 and 'emergency_contact' not in model.contact_details:
            raise ValueError("Emergency contact is required for patients above 60 years old")
        return model
     
def insert_patient(patient:Patient):

    print(patient.name)
    print(patient.age) 
    print(patient.weight) 
    print(patient.email)
    print(patient.linkedin)
    print('inserted into database')

patient_info={"name":"nitish","age":70,'weight':70.5,'married':True,'email':'nitish@hdfc.com','linkedin':'https://www.linkedin.com/in/nitish-kumar-123456789/','contact_details':{'phone':'123-456-7890', 'emergency_contact': 'John Doe'},'allergis':['peanuts']}
patient1=Patient(**patient_info)
insert_patient(patient1)
