from fastapi import APIRouter
from app.schemas.creature import CreatureRead

router = APIRouter()


@router.get("", response_model=list[CreatureRead])
def list_creatures():
    return []
