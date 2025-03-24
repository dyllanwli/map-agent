from pydantic import BaseModel
from typing import Optional

class Location(BaseModel):
    location_name: str
    location_address: str
    location_latitude: Optional[float] = None
    location_longitude: Optional[float] = None
    location_type: Optional[str] = None
    location_rating: Optional[float] = None
    location_reviews: Optional[list[str]] = None