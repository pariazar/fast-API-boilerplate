from datetime import datetime

from .. import schemas
from ..services import note
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from ..database import get_db

router = APIRouter()


@router.get('/')
async def get_notes(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    note_service = note.NoteService(db)
    note_result = await note_service.get_notes(limit, page, search)
    return note_result


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_note(payload: schemas.NoteBaseSchema, db: Session = Depends(get_db)):
    note_service = note.NoteService(db)
    note_result = await note_service.create_note(payload)
    return note_result


@router.patch('/{noteId}')
async def update_note(noteId: str, payload: schemas.NoteBaseSchema, db: Session = Depends(get_db)):
    note_service = note.NoteService(db)
    note_result = await note_service.update_note(noteId, payload)
    return note_result


@router.get('/{noteId}')
async def get_post(noteId: str, db: Session = Depends(get_db)):
    note_service = note.NoteService(db)
    note_result = await note_service.get_post(noteId)
    return note_result


@router.delete('/{noteId}')
async def delete_post(noteId: str, db: Session = Depends(get_db)):
    note_service = note.NoteService(db)
    note_result = await note_service.delete_post(noteId)
    return note_result
