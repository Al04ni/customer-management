import reflex as rx
import os

#for database_url see `Neon Postgres Database
database_url = os.getenv("DATABASE_URL", "sqlite:///reflex.db")

config = rx.Config(
    app_name="app",
    db_url=database_url,
    )
