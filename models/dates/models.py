from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class DateModel(Base):
    __tablename__ = "dates"

    id = Column(Integer, primary_key=True, index=True)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    fun_fact = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Unique constraint on the combination of month and day
    __table_args__ = (UniqueConstraint('month', 'day', name='_month_day_uc'),)

    # This method can be used to update the fun_fact based on the external API
    def update_fun_fact(self, new_fun_fact):
        self.fun_fact = new_fun_fact
