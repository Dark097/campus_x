from pydantic import BaseModel,Field,EmailStr,AnyUrl,field_validator,model_validator,computed_field
from typing import Dict,List,Optional
class Patient (BaseModel):

    name:str
    age:int
    height:float
    weight:Optional[float]=None
    married:bool
    contact_details:Dict[str,str]
    email:EmailStr
    linkedin:AnyUrl
    allergis:List[str]


# computed fields
    @computed_field
    @property
    def bmi(self)-> float:
        bmi=round(self.weight/(self.height**2), 2)
        return bmi
     
def insert_patient(patient:Patient):

    print(patient.name)
    print(patient.age) 
    print(patient.weight) 
    print(patient.email)
    print(patient.linkedin)
    print(patient.bmi)
    print('inserted into database')

patient_info={"name":"nitish","height":1.75,"age":70,'weight':70.5,'married':True,'email':'nitish@hdfc.com','linkedin':'https://www.linkedin.com/in/nitish-kumar-123456789/','contact_details':{'phone':'123-456-7890', 'emergency_contact': 'John Doe'},'allergis':['peanuts']}
patient1=Patient(**patient_info)
insert_patient(patient1)
