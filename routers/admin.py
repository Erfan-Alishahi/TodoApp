from fastapi import APIRouter, Depends, HTTPException, Path
from database import engine, Sessionlocal
from pydantic import BaseModel, Field
from .auth import get_current_user
from sqlalchemy.orm import session
from typing import Annotated
from starlette import status
from models import Todos


router = APIRouter(
    prefix='/admin',
    tags=['admin']
)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get('/todo', status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail="Authentication Failed!")
    return db.query(Todos).all()

@router.delete('/todo/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed!')
    todo_model = db.query(Todos).filter(todo_id == Todos.id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found!")
    db.query(Todos).filter(todo_id == Todos.id).delete()

    db.commit()
    