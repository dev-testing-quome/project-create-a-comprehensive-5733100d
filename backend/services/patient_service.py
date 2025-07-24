from sqlalchemy.orm import Session
from schemas import PatientCreate, PatientRead
from models import Patient

def create_patient(db: Session, patient: PatientCreate) -> PatientRead:
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return PatientRead.from_orm(db_patient)

def get_patient(db: Session, patient_id: int) -> PatientRead | None:
    return db.query(Patient).filter(Patient.id == patient_id).first()

# Add other patient service functions (update, delete, list) as needed
