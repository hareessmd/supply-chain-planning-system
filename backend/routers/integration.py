# backend/routers/integration.py
from fastapi import APIRouter, UploadFile, File, HTTPException
import csv
from io import TextIOWrapper
from database import SessionLocal
from models.raw import RawSalesOrder
from datetime import datetime

router = APIRouter(prefix="/integration", tags=["integration"])

@router.post("/sales-orders/upload")
async def upload_sales_orders(file: UploadFile = File(...), source_system: str = "SAP"):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported")

    db = SessionLocal()
    load_batch_id = f"SO_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"

    reader = csv.DictReader(TextIOWrapper(file.file, encoding="utf-8"))
    count = 0

    try:
        for row in reader:
            # Expect CSV columns: document_type,document_number,item_number,material_code,...
            so = RawSalesOrder(
                source_system=source_system,
                document_type=row.get("document_type") or "",
                document_number=row["document_number"],
                item_number=row["item_number"],
                material_code=row["material_code"],
                plant_code=row["plant_code"],
                customer_code=row.get("customer_code") or "",
                posting_date=datetime.strptime(row["posting_date"], "%Y-%m-%d").date(),
                order_qty=float(row["order_qty"]),
                order_uom=row["order_uom"],
                order_value=float(row["order_value"]) if row.get("order_value") else None,
                currency=row.get("currency") or "",
                load_batch_id=load_batch_id,
            )
            db.add(so)
            count += 1
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error processing CSV: {e}")
    finally:
        db.close()

    return {"status": "ok", "rows_inserted": count, "load_batch_id": load_batch_id}