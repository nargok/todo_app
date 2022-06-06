from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session

from core.db.database import get_db
from todo.repository.todo.todo_repository import TodoRepository
from todo.models.todo import Todo
from todo.schemas.todo import TodoCreate, TodoUpdate



# これがリポジトリimplかな
class TodoUseCase:
    def __init__(self, repository):
        # sessoin = Depends(get_db)
        # self.repository = TodoRepository(sessoin)
        # self.session = session
        self.repository = repository


    def get_todo(self, todo_id: int) -> Todo:
        print("===== debug ====")
        # print(self.session)
        return self.repository.selectOne(todo_id)


    def get_todos(self, limit: int = 100) -> List[Todo]:
        return self.repository.selectAll(limit)


    def create_todo(self, todo: TodoCreate) -> Todo:
        result = self.repository.insert(todo)
        return result


    def update_todo(self, todo_id: int, todo: TodoUpdate) -> Todo:
        result = self.repository.update(todo_id, todo)
        return result


    def delete_todo(self, todo_id: int):
        return self.repository.delete(todo_id)
