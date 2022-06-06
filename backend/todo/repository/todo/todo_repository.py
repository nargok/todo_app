
from typing import List
from sqlalchemy.orm import Session
from todo.models.todo import Todo
from todo.repository.todo.i_todo_repository import ITodoRepository
from todo.schemas.todo import TodoCreate, TodoUpdate


class TodoRepository(ITodoRepository):

    def __init__(self, session):
        self.session = session


    def insert(self, todo: TodoCreate) -> Todo:
        db_todo = Todo(title=todo.title, text=todo.text)
        self.session.add(db_todo)
        self.session.commit()
        self.session.refresh(db_todo)
        return db_todo

    
    def update(self, todo_id: int, todo: TodoUpdate) -> Todo:
        db_todo = self.session.query(Todo).filter(Todo.id == todo_id).first()
        db_todo.title = todo.title
        db_todo.text = todo.text
        self.session.commit()
        return db_todo


    def delete(self, todo_id: int) -> None:
        db_todo = self.session.query(Todo).filter(Todo.id == todo_id).first()
        self.session.delete(db_todo)
        self.session.commit()

    
    def selectOne(self, todo_id: int) -> Todo:
        return self.session.query(Todo).filter(Todo.id == todo_id).first()
    
    
    def selectAll(self, limit: int) -> List[Todo]:
        return self.session.query(Todo).limit(limit).all()
