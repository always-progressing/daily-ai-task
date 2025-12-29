from app.core.database import SessionLocal
from app.models.user import User

db = SessionLocal()
user = User(username="test_user")
db.add(user)
db.commit()

db.query(User).all()
db.close()