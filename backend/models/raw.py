# backend/models/raw.py
from sqlalchemy import Column, Integer, String, Date, Float, DateTime
from datetime import datetime
from database import Base

class RawSalesOrder(Base):
    __tablename__ = "raw_sales_orders"

    id = Column(Integer, primary_key=True, index=True)
    source_system = Column(String, nullable=False)
    document_type = Column(String, nullable=True)
    document_number = Column(String, nullable=False)
    item_number = Column(String, nullable=False)
    material_code = Column(String, nullable=False)
    plant_code = Column(String, nullable=False)
    customer_code = Column(String, nullable=True)
    posting_date = Column(Date, nullable=False)
    order_qty = Column(Float, nullable=False)
    order_uom = Column(String, nullable=False)
    order_value = Column(Float, nullable=True)
    currency = Column(String, nullable=True)
    load_batch_id = Column(String, nullable=False)
    load_ts = Column(DateTime, default=datetime.utcnow)


class RawInventory(Base):
    __tablename__ = "raw_inventory"

    id = Column(Integer, primary_key=True, index=True)
    source_system = Column(String, nullable=False)
    material_code = Column(String, nullable=False)
    plant_code = Column(String, nullable=False)
    stock_category = Column(String, nullable=True)
    quantity = Column(Float, nullable=False)
    uom = Column(String, nullable=False)
    snapshot_date = Column(Date, nullable=False)
    load_batch_id = Column(String, nullable=False)
    load_ts = Column(DateTime, default=datetime.utcnow)