from app.db.base import Base
from app.db.session import engine

# ⬇️ make sure your model is imported so it's registered with Base
from app.models.user import User

print("Creating all tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully.")
