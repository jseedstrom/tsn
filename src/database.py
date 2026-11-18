
from datetime import datetime
from typing import List, Literal, Optional
from pydantic import BaseModel, Field


class Performance(BaseModel):
    """Grundmodell för en föreställning i TeaterSkiftnyckeln 3.0.
    Följer strikt tillståndsmaskinen: DRAFT -> PENDING_APPROVAL -> BOOKED -> PUBLISHED
    """
    id: str = Field(..., description="Unikt ID för föreställningen")
    title: str = Field(..., description="Föreställningens namn / titel")
    producer: str = Field(..., description="Producent eller turnébolag")
    venue: str = Field(..., description="Spelplats (t.ex. Joar Blå, Litslena bygdegård)")
    event_date: datetime = Field(..., description="Datum och tid för föreställningen")
    
    # Tillståndsmaskin (State Machine Logic)
    status: Literal["DRAFT", "PENDING_APPROVAL", "BOOKED", "PUBLISHED"] = "DRAFT"
    
    # Biljetter och ekonomi
    ticket_quota: int = Field(default=0, description="Totala antal tillgängliga biljetter")
    ticket_price: float = Field(default=0.0, description="Biljettpris i SEK")
    
    # Extra fält
    notes: Optional[str] = Field(default=None, description="Interna anteckningar för funktionärer")
    created_at: datetime = Field(default_factory=datetime.now)


class AssociationConfig(BaseModel):
    """Grundläggande inställningar för föreningen (t.ex. Enköpings Riksteaterförening)."""
    association_name: str = "Enköpings Riksteaterförening"
    org_number: Optional[str] = None
    fortnox_connected: bool = False