# backend/scripts/seed_data.py
import datetime
from database import SessionLocal, Base, engine
from models.master import Product, Location, CalendarWeek
from models.planning import DemandHistory

def create_calendar_weeks(start_date, weeks):
    session = SessionLocal()
    for i in range(weeks):
        week_start = start_date + datetime.timedelta(weeks=i)
        week_end = week_start + datetime.timedelta(days=6)
        cw = f"{week_start.isocalendar().year}-W{week_start.isocalendar().week:02d}"
        cw_obj = CalendarWeek(
            calendar_week=cw,
            start_date=week_start,
            end_date=week_end,
            fiscal_period=str(week_start.month),
            fiscal_year=str(week_start.year),
        )
        session.add(cw_obj)
    session.commit()
    session.close()

def seed():
    session = SessionLocal()

    # Simple products
    p1 = Product(code="P001", description="Product 1", uom="EA")
    p2 = Product(code="P002", description="Product 2", uom="EA")

    # Locations
    l1 = Location(code="PLANT1", name="Plant 1", location_type="PLANT")
    l2 = Location(code="DC1", name="DC 1", location_type="DC")

    session.add_all([p1, p2, l1, l2])
    session.commit()

    # Fetch with IDs
    products = session.query(Product).all()
    locations = session.query(Location).all()
    weeks = session.query(CalendarWeek).all()

    # Create fake demand: random-ish pattern
    import random
    for prod in products:
        for loc in locations:
            for cw in weeks:
                qty = random.randint(50, 150)
                dh = DemandHistory(
                    product_id=prod.id,
                    location_id=loc.id,
                    calendar_week_id=cw.id,
                    qty=qty,
                    source="SEED",
                    load_batch_id="SEED_RUN_1",
                )
                session.add(dh)
    session.commit()
    session.close()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    start_date = datetime.date(2024, 1, 1)
    create_calendar_weeks(start_date, 52)
    seed()