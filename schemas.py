from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class EnrichRequest(BaseModel):
    marketplace: str = Field(example="ozon")
    id_type: str = Field(example="posting_number")
    id_value: str = Field(example="12345-001")

class EnrichResponse(BaseModel):
    data: Dict[str, Any]
    meta: Optional[Dict[str, Any]] = None
