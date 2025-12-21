# backend/models/planning.py
from sqlalchemy import Column, Integer, Float, ForeignKey, String
from database import Base

class DemandHistory(Base):
    __tablename__ = "demand_history"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, nullable=False)
    location_id = Column(Integer, nullable=False)
    calendar_week_id = Column(Integer, nullable=False)
    qty = Column(Float, nullable=False)
    value = Column(Float, nullable=True)
    source = Column(String, nullable=True)  # SHIPMENTS, ORDERS, etc.
    load_batch_id = Column(String, nullable=True)


class InventoryPosition(Base):
    __tablename__ = "inventory_positions"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, nullable=False)
    location_id = Column(Integer, nullable=False)
    calendar_week_id = Column(Integer, nullable=False)
    on_hand_qty = Column(Float, nullable=False)
    in_transit_qty = Column(Float, nullable=True)
    safety_stock_qty = Column(Float, nullable=True)