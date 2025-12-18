# backend/models/master.py
from sqlalchemy import Column, Integer, String, Date, Float
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)
    uom = Column(String, nullable=False, default="EA")
    family = Column(String, nullable=True)
    group = Column(String, nullable=True)
    lifecycle_status = Column(String, nullable=False, default="Active")


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=True)
    location_type = Column(String, nullable=True)  # PLANT, DC, etc.
    country = Column(String, nullable=True)
    region = Column(String, nullable=True)


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=True)
    segment = Column(String, nullable=True)
    channel = Column(String, nullable=True)
    region = Column(String, nullable=True)


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=True)
    location_id = Column(Integer, nullable=True)
    resource_type = Column(String, nullable=True)  # MACHINE, LINE
    available_hours_per_week = Column(Float, nullable=True)


class CalendarWeek(Base):
    __tablename__ = "calendar_weeks"

    id = Column(Integer, primary_key=True, index=True)
    calendar_week = Column(String, unique=True, index=True, nullable=False)  # e.g. 2025-W01
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    fiscal_period = Column(String, nullable=True)
    fiscal_year = Column(String, nullable=True)