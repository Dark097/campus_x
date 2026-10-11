from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    zip_code:str

class Patient(BaseModel):
    name:str
    age:int
    address:Address

address_info={"city":"New York","state":"NY","zip_code":"10001"}
address=Address(**address_info)
patient_info={"name":"John Doe","age":30,"address":address}
patient1=Patient(**patient_info)
print(patient1)
print(patient1.address.city)

temp1=patient1.model_dump(exclude={'address'})  # include can also be used
print(type(temp1))
print(temp1)

temp2=patient1.model_dump_json(include={'name','address'})  # exclude can also be used
print(type(temp2))
print(temp2)