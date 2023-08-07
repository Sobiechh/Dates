from itertools import count

from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session

from api.dates.models import DateModel
from api.dates.schemas import DateCreate, DateResponse, PopularMonth
from api.dates.utils import fetch_fun_fact
from config import settings
from database import engine, get_db
from typing import List

# Create tables
DateModel.metadata.create_all(bind=engine)
router = APIRouter()

SECRET_API_KEY = settings.SECRET_API_KEY


@router.post("/dates", response_model=DateResponse)
async def create_date(date: DateCreate, db: Session = Depends(get_db)):
    # Validate month and day
    if date.month < 1 or date.month > 12 or date.day < 1 or date.day > 31:
        raise HTTPException(status_code=400, detail="Invalid month or day")

    # Check if the date already exists in the database
    existing_date = (
        db.query(DateModel).filter_by(month=date.month, day=date.day).first()
    )

    if existing_date:
        # Date exists, update the fun fact using the external API
        fun_fact = await fetch_fun_fact(date.month, date.day)
        existing_date.fun_fact = fun_fact
        db.commit()
        return DateResponse(
            id=existing_date.id,
            month=existing_date.get_month_display(month=existing_date.month),
            day=existing_date.day,
            fact=fun_fact,
        )

    # Date doesn't exist, fetch fun fact and create a new record
    fun_fact = await fetch_fun_fact(date.month, date.day)
    new_date = DateModel(month=date.month, day=date.day, fun_fact=fun_fact)
    db.add(new_date)
    db.commit()
    db.refresh(new_date)

    return DateResponse(
        id=new_date.id,
        month=new_date.get_month_display(month=new_date.month),
        day=new_date.day,
        fact=fun_fact,
    )


@router.get("/dates", response_model=List[DateResponse])
async def get_dates(db: Session = Depends(get_db)):
    dates = db.query(DateModel).all()
    date_responses = []
    for date in dates:
        fun_fact = await fetch_fun_fact(date.month, date.day)
        date_response = DateResponse(
            id=date.id,
            month=date.get_month_display(month=date.month),
            day=date.day,
            fact=fun_fact,
        )
        date_responses.append(date_response)
    return date_responses


@router.delete("/dates/{date_id}", status_code=204)
def delete_date(
    date_id: int, x_api_key: str = Header(None), db: Session = Depends(get_db)
):
    if x_api_key != SECRET_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    date = db.query(DateModel).get(date_id)
    if not date:
        raise HTTPException(status_code=404, detail="Date not found")

    db.delete(date)
    db.commit()

    return None


popular_id_counter = count(1)


@router.get("/popular", response_model=List[PopularMonth])
def get_popular_months(db: Session = Depends(get_db)):
    query = db.query(DateModel.month, DateModel.day).distinct(
        DateModel.month, DateModel.day
    )
    month_counts = {}
    for month, _ in query:
        month_counts[month] = month_counts.get(month, 0) + 1

    popular_months = []
    for month, days_checked in month_counts.items():
        unique_id = next(popular_id_counter)
        popular_month = PopularMonth(
            id=unique_id,
            month=DateModel.get_month_display(month=month),
            days_checked=days_checked,
        )
        popular_months.append(popular_month)

    sorted_popular_months = sorted(
        popular_months, key=lambda x: x.days_checked, reverse=True
    )
    return sorted_popular_months
