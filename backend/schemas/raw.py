# backend/schemas/raw.py
from pydantic import BaseModel
from datetime import date

class RawSalesOrderIn(BaseModel):
    source_system: str
    document_type: str | None = None
    document_number: str
    item_number: str
    material_code: str
    plant_code: str
    customer_code: str | None = None
    posting_date: date
    order_qty: float
    order_uom: str
    order_value: float | None = None
    currency: str | None = None
    load_batch_id: str