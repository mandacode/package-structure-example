"""Presentation Layer"""
from fastapi import APIRouter, Depends, HTTPException, status

from .database import Session, get_session
from .dtos import CreateStudentDTO, StudentDTO
from .repositories import SQLAlchemyStudentRepository
from .services import create_student, get_student

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


@router.get(
    "/{student_id}", 
    response_model=StudentDTO,
)
def get_students_controller(
    student_id: int,
    session: Session = Depends(get_session),
):
    """Controller function for retrieving students."""
    repo = SQLAlchemyStudentRepository(session=session)

    student = get_student(repo=repo, student_id=student_id)

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return student
