from app.database.database import SessionLocal
from app.models.receipt import Receipt


def get_receipts():

    db = SessionLocal()

    try:
        return db.query(Receipt).order_by(Receipt.id.desc()).all()

    finally:
        db.close()