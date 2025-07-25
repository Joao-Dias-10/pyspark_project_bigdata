from sqlalchemy import Column, Integer, Float, String, Date, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class YellowTrip(Base):
    __tablename__ = "yellow_tripdata"

    id = Column(Integer, primary_key=True, autoincrement=True)  
    vendor_id = Column(Integer)
    pickup_datetime = Column(TIMESTAMP)
    dropoff_datetime = Column(TIMESTAMP)
    passenger_count = Column(Integer)
    trip_distance = Column(Float)
    ratecode_id = Column(Integer)
    pu_location_id = Column(Integer)
    do_location_id = Column(Integer)
    payment_type = Column(Integer)
    fare_amount = Column(Float)
    extra = Column(Float)
    mta_tax = Column(Float)
    tip_amount = Column(Float)
    tolls_amount = Column(Float)
    improvement_surcharge = Column(Float)
    total_amount = Column(Float)
    congestion_surcharge = Column(Float)
    trip_duration = Column(Float)
    last_updated = Column(TIMESTAMP)
    pickup_date = Column(Date)
