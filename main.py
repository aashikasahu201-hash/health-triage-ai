from fastapi import FastAPI
from pydantic import BaseModel
from triage import get_triage

app = FastAPI()

class SymptomRequest(BaseModel):
    symptoms: list[str]

@app.post("/get-triage")
def triage_endpoint(req: SymptomRequest):
    return get_triage(req.symptoms)
