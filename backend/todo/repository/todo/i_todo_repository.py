import abc
from typing import List

from todo.schemas.todo import Todo, TodoCreate, TodoUpdate

class ITodoRepository(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def insert(todo: TodoCreate) -> Todo:
        raise NotImplementedError()

    
    @abc.abstractmethod
    def update(todo_id: int, todo: TodoUpdate) -> Todo:
        raise NotImplementedError()
    

    @abc.abstractmethod
    def delete(todo_id: int) -> None:
        raise NotImplementedError()

    
    @abc.abstractmethod
    def selectOne(todo_id: int) -> Todo:
        raise NotImplementedError()
    
    
    @abc.abstractmethod
    def selectAll() -> List[Todo]:
        raise NotImplementedError()
