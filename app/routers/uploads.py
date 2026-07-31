import uuid
from pathlib import Path
from app.services.receipt_service import create_receipt
from fastapi import APIRouter, File, UploadFile

from app.database.database import SessionLocal
from app.models.receipt import Receipt

router = APIRouter()


@router.post("/upload")
async def upload_receipt(
    receipt: UploadFile = File(...)
):
    upload_dir = Path("uploads")
    upload_dir.mkdir(exist_ok=True)

    extension = Path(receipt.filename).suffix
    unique_filename = f"{uuid.uuid4()}{extension}"

    file_path = upload_dir / unique_filename

    with open(file_path, "wb") as buffer:
        buffer.write(await receipt.read())

    create_receipt(str(file_path))

    return {
        "saved_as": str(file_path)
    }