from db import Session, create_tables, drop_tables, start_mappers
from student import Student


def create_student(session: Session, name: str) -> Student: # type: ignore
    student = Student(name=name)

    session.add(student)
    session.commit()

    return student 

if __name__ == "__main__":
    
    drop_tables()
    create_tables()
    session = Session()

    student = create_student(session=session, name="Pietrek")
    print(student)