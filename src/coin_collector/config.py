import json
from typing import List
from pydantic import BaseModel, Field

class Vec2(BaseModel):
    x: int
    y: int

class Coin(BaseModel):
    x: int
    y: int
    r: int = Field(ge=3, le=30)

class Wall(BaseModel):
    x: int
    y: int
    w: int = Field(gt=0)
    h: int = Field(gt=0)

class Level(BaseModel):
    width: int = Field(default=800, ge=320, le=1920)
    height: int = Field(default=600, ge=240, le=1080)
    player_start: Vec2 = Field(default_factory=lambda: Vec2(x=50, y=50))
    speed: int = Field(default=5, ge=1, le=20) # NEU: Individuelle Geschwindigkeit
    coins: List[Coin]
    walls: List[Wall] = []

def load_level(path: str) -> Level:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return Level.model_validate(data)