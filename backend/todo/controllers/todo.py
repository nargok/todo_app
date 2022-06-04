from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

import todo.cruds.todo as cruds
from core.db.database import get_db
from todo.schemas.todo import Todo, TodoCreate, TodoUpdate


router = APIRouter()

@router.get("/{todo_id}", response_model=Todo)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = cruds.get_todo(db=db, todo_id=todo_id)
    if not db_todo:
        raise HTTPException(status=404, detail="Todo not found")
    return db_todo


@router.get("/", response_model=List[Todo])
def read_todos(limit: int = 100, db: Session = Depends(get_db)):
    return cruds.get_todos(db=db, limit=limit)


@router.post("/", response_model=Todo)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return cruds.create_todo(db=db, todo=todo)


@router.put("/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    return cruds.update_todo(db=db, todo_id=todo_id, todo=todo)


@router.delete("/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    return cruds.delete_todo(db=db, todo_id=todo_id)
