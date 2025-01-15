"""Presentation Layer"""
from fastapi import APIRouter, Depends

from .database import Session, get_session
from .dtos import CreateStudentDTO, StudentDTO
from .repositories import SQLAlchemyStudentRepository
from .services import create_student

router = APIRouter(prefix="/students")


@router.post(
    "", 
    response_model=StudentDTO,
)
def create_student_controller(
    dto: CreateStudentDTO, 
    session: Session = Depends(get_session),
):
    """Controller function for creating a student."""
    repo = SQLAlchemyStudentRepository(session=session)

    student = create_student(repo=repo, name=dto.name)

    return student 
