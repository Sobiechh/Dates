from sqlalchemy import Column, DateTime, Integer, String, UniqueConstraint
from sqlalchemy.sql import func

from database import Base


class DateModel(Base):
    __tablename__ = "dates"

    id = Column(Integer, primary_key=True, index=True)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    fun_fact = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Unique constraint on the combination of month and day
    __table_args__ = (UniqueConstraint("month", "day", name="_month_day_uc"),)

    # This method can be used to update the fun_fact based on the external API
    def update_fun_fact(self, new_fun_fact):
        self.fun_fact = new_fun_fact

    @staticmethod
    def get_month_display(month: int) -> str:
        months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        if 1 <= month <= 12:
            return months[month - 1]
        return "Invalid Month"
