# coding=utf-

from appdir import db
from appdir.models import InvitationCode, User
from datetime import datetime


# add codes
# code = InvitationCode(
#     invitation_code="admin123",
#     create_time=datetime.now(),
#     is_valid=1
#     )
# db.session.add(code)
# db.session.commit()

# list all invitation codes
for code in InvitationCode.query.filter(InvitationCode.id == 1).all():
    print(code)


if __name__ == "__main__":
    pass
