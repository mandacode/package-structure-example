"""Presentation Layer/Validation Layer"""
import datetime

from pydantic import BaseModel


class CreateStudentDTO(BaseModel):
    """DTO class for creating students."""
    name: str 


class StudentDTO(BaseModel):
    """DTO class for retrieving students."""

    id: int 
    name: str 
    created_at: datetime.datetime
