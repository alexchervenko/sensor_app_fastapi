from sqlmodel import create_engine, SQLModel
from sensor import models

postgres_url = "postgresql+psycopg2://postgres:postgres@localhost:5432/sensor_app_db"

engine = create_engine(postgres_url, echo=True)
