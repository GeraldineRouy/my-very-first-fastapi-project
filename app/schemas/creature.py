from enum import Enum
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict


class EvolutionStage(str, Enum):
    egg = "egg"
    baby = "baby"
    teen = "teen"
    adult = "adult"

class CreatureBase(BaseModel):
    model_config = ConfigDict(extra="forbid")  # refuse les champs inconnus

    name: str = Field(min_length=1, max_length=40)
    species: str = Field(min_length=1, max_length=40)
    stage: EvolutionStage = EvolutionStage.egg

    traits: list[str] = Field(default_factory=list, max_length=3)
    hunger: int = Field(default=50, ge=0, le=100)
    happiness: int = Field(default=50, ge=0, le=100)

class CreatureCreate(CreatureBase):
    pass


class CreatureUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str | None = Field(default=None, min_length=1, max_length=40)
    species: str | None = Field(default=None, min_length=1, max_length=40)
    stage: EvolutionStage | None = None

    traits: list[str] | None = Field(default=None, max_length=3)
    hunger: int | None = Field(default=None, ge=0, le=100)
    happiness: int | None = Field(default=None, ge=0, le=100)


class CreatureRead(CreatureBase):
    id: UUID

