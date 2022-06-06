from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session
from todo.repository.todo.todo_repository import TodoRepository
from todo.usecase.todo import TodoUseCase

from core.db.database import get_db
from todo.usecase.todo import TodoUseCase
from todo.schemas.todo import Todo, TodoCreate, TodoUpdate


router = APIRouter()


def todo_usecase(session: Session = Depends(get_db)) -> TodoUseCase:
    todo_repository = TodoRepository(session)
    return TodoUseCase(todo_repository)


@router.get("/{todo_id}", response_model=Todo)
def read_todo(
    todo_id: int,
    todo_usecase: TodoUseCase = Depends(todo_usecase)
):
    db_todo = todo_usecase.get_todo(todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


@router.get("/", response_model=List[Todo])
def read_todos(
    limit: int = 100,
    todo_usecase: TodoUseCase = Depends(todo_usecase)
):
    return todo_usecase.get_todos(limit)


@router.post("/", response_model=Todo)
def create_todo(
    todo: TodoCreate,
    todo_usecase: TodoUseCase = Depends(todo_usecase)
):
    return todo_usecase.create_todo(todo)


@router.put("/{todo_id}", response_model=Todo)
def update_todo(
    todo_id: int,
    todo: TodoUpdate,
    todo_usecase: TodoUseCase = Depends(todo_usecase)
):
    return todo_usecase.update_todo(todo_id, todo)


@router.delete("/{todo_id}", response_model=Todo)
def delete_todo(
    todo_id: int,
    todo_usecase: TodoUseCase = Depends(todo_usecase)
):
    return todo_usecase.delete_todo(todo_id)
