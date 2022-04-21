import secrets
import string
import uuid

for i in range(25):
    with open(str(uuid.uuid4()) + ".txt", "w") as f:
        f.write(''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(200)))
