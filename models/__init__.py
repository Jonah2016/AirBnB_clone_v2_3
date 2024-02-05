#!/usr/bin/python3
"""
initializes the models package
"""

from os import getenv


storage_tbl = getenv("HBNB_TYPE_STORAGE")

if storage_tbl == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
