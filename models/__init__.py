#!/usr/bin/python3
"""
Instantiates a storage object.

Instantiates a database storage engine (DBStorage),
if env viriable is set to db.
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
