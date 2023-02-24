from ..models import Note
from .. import schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response


class NoteService:
    def __init__(self, db: Session):
        self.db = db

    async def get_notes(self, limit: int = 10, page: int = 1, search: str = ''):
        skip = (page - 1) * limit
        notes = self.db.query(Note.Note).filter(
            Note.Note.title.contains(search)).limit(limit).offset(skip).all()
        return {'status': 'success', 'totals': len(notes), 'notes': notes}

    async def create_note(self, payload: schemas.NoteBaseSchema):
        note = self.db.query(Note.Note).filter(
            Note.Note.id == payload.id).first()
        if note:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                detail=f"UNPROCESSABLE_ENTITY")

        new_note = Note.Note(**payload.dict())
        self.db.add(new_note)
        self.db.commit()
        self.db.refresh(new_note)
        return {"status": "success", "note": new_note}

    async def update_note(self, noteId: str, payload: schemas.NoteBaseSchema):
        note_query = self.db.query(Note.Note).filter(
            Note.Note.id == noteId)
        db_note = note_query.first()
        if not db_note:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'No note with this id: {noteId} found')
        update_data = payload.dict(exclude_unset=True)
        note_query.filter(Note.Note.id == noteId).update(update_data,
                                                         synchronize_session=False)
        self.db.commit()
        self.db.refresh(db_note)
        return {"status": "success", "note": db_note}

    async def get_post(self, noteId: str):
        note = self.db.query(Note.Note).filter(
            Note.Note.id == noteId).first()
        if not note:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"No note with this id: {noteId} found")
        return {"status": "success", "note": note}

    async def delete_post(self, noteId: str):
        note_query = self.db.query(Note.Note).filter(
            Note.Note.id == noteId)
        note = note_query.first()
        if not note:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'No note with this id: {id} found')
        note_query.delete(synchronize_session=False)
        self.db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
