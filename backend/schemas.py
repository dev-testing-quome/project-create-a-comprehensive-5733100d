from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class PatientCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    dob: datetime

class PatientRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    dob: datetime
    
    class Config:
        orm_mode = True

class AppointmentCreate(BaseModel):
    patient_id: int
    date_time: datetime
    doctor: str

class AppointmentRead(BaseModel):
    id: int
    patient_id: int
    date_time: datetime
    doctor: str

    class Config:
        orm_mode = True

# Add other schemas as needed