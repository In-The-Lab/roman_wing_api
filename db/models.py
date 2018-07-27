import json

class User:

    def __init__(self, id_, first_name, last_name,
                 email, is_admin, date_created):
        self.id = id_
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.date_created = date_created

    def to_json(self):
        features = {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "date_created": str(self.date_created)
        }
        return json.dumps(features)

    def __str__(self):
        return (
            "{} {}:\n"
            "\temail: {}\n"
            "\tcreated on: {}"
            .format(self.first_name,
                    self.last_name,
                    self.email,
                    self.date_created)
        )

class Post:

    def __init__(self, id_, creator_id, body, date_created):
        self.id = id_
        self.creator_id = creator_id
        self.body = body
        self.date_created = date_created

    def to_json(self):
        features = {
            "id": self.id,
            "creator_id": creator_id,
            "body": self.body,
            "date_created": self.date_created
        }
        return json.dumps(features)

    def __str__(self):
        return self.body
