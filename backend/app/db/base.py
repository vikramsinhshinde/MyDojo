
# app/db/base.py

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# ⚠️ DO NOT import models directly here.
# Alembic will auto-discover models via env.py if you import all in app/db/init.py
