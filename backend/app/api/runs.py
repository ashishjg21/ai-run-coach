from fastapi import APIRouter
from backend.app import crud

router = APIRouter(prefix="/runs", tags=["runs"])

@router.get("/")
def get_all_runs():
    runs = crud.get_runs()
    return [{"id": r.id, "distance": r.distance, "pace": r.pace, "rpe": r.rpe, "notes": r.notes, "created_at": r.created_at} for r in runs]
