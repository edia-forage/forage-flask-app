from app.models import User
from app import db

user1 = User(id=10001, first_name="Atom", last_name="Molecule", username="atomic",
             company="ANZ", contact_no="9901234101", email="atomic@anz.com")

user2 = User(id=10002, first_name="Bhaskar", last_name="Paskar", username="tusker",
             company="None", contact_no="4017341019", email="tusker@none.com")

user3 = User(id=10003, first_name="Azure", last_name="Zigure", username="azoor",
             company="ANZ", contact_no="9001002345", email="azoor@nature.com")

for user in [user1, user2, user3]:
    db.session.add(user)
    db.session.commit()
