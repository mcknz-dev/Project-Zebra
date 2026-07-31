from app.database.database import SessionLocal
from app.models.receipt import Receipt


def create_receipt(storage_path: str):

    db = SessionLocal()

    try:
        new_receipt = Receipt(
            storage_path=storage_path,
            merchant="Unknown",
            total=0.00,
            currency="CAD"
        )

        db.add(new_receipt)
        db.commit()

        return new_receipt

    finally:
        db.close()