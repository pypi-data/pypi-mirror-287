from pydantic import BaseModel


class FastApiProjectContext(BaseModel):
    name: str

    class Config:
        use_enum_values = True
