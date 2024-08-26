from app import db
from models import User  # Adjust the import based on your file structure

# Find the user you want to set as admin
user = User.query.filter_by(phone='01729311549').first()  # Use appropriate filter
if user:
    user.role = 'admin'
    db.session.commit()
    print(f"User {user.name} is now an admin.")
else:
    print("User not found.")
