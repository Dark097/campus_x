from fastapi import FastAPI , Path , HTTPException,Query
import json
app=FastAPI()

def load_data():
    with open("patients.json",'r') as f:
        return json.load(f)

@app.get("/")
def hello():
    return {"message":"Patient management system api "}

@app.get("/about")
def about():
    return {"message":"This is a patient management system api created using FastAPI framework. It allows you to manage patient records, including adding new patients, retrieving existing patient information, updating patient details, and deleting patient records. The API provides endpoints for various operations related to patient management."}

@app.get("/view")
def view():
    data=load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id:str=Path(..., description="The ID of the patient to retrieve", example="P001")):
    # load all the patients
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail=f"Patient with ID {patient_id} not found")

@app.get("/sort")
def sort_data(sort_by:str=Query(...,description='sort on basis of height,weight,age'),order:str=Query('asc',description='order of sorting, can be asc or desc')):
    valid_fields=['height','weight','age']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort_by value. Must be one of 'height', 'weight', or 'age'.")
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail=f"Invalid order value. Must be 'asc' or 'desc'.")
    data=load_data()
    reverse_order=True if order=='desc' else False
    sorted_data=sorted(data.values(), key=lambda x: x.get(sort_by), reverse=reverse_order)
    return sorted_data


