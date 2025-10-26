# CRUD_Python_Module.py
# CS-340 Project One — CRUD for AAC animals collection
# Author: Brianna Reed

from typing import Optional, List, Dict
from pymongo import MongoClient, errors
from urllib.parse import quote_plus
import os


class AnimalShelter:
    """
    CRUD operations for the 'aac.animals' collection.

    Implemented methods:
      - create(document: dict) -> bool
      - read(query: dict, projection: Optional[dict] = None) -> List[dict]
      - update(query: dict, new_values: dict, many: bool = False) -> int
      - delete(query: dict, many: bool = False) -> int

    Notes:
      * Uses find() (not find_one) per assignment requirement.
      * Authenticates against the 'admin' database (authSource=admin),
        because the assignment has you create the user in admin.
    """

    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        host: str = "127.0.0.1",
        port: int = 27017,
        db_name: str = "aac",
        col_name: str = "animals",
        auth_db: Optional[str] = "admin",     # <<-- IMPORTANT: default to admin
        connect_timeout_ms: int = 5000,
    ):
        self.username = username or os.getenv("MONGO_USERNAME") or "aacuser"
        self.password = password or os.getenv("MONGO_PASSWORD")  # may be None
        self.db_name = db_name
        self.col_name = col_name
        self.auth_db = auth_db or "admin"

        if self.password:
            u = quote_plus(self.username)
            p = quote_plus(self.password)
            # Use authSource=admin; we don't need to include the db path segment
            uri = f"mongodb://{u}:{p}@{host}:{port}/?authSource={self.auth_db}"
        else:
            # local no-auth fallback (not used for the assignment, but harmless)
            uri = f"mongodb://{host}:{port}/"

        try:
            self.client = MongoClient(uri, serverSelectionTimeoutMS=connect_timeout_ms)
            # Fail fast on bad creds/connection
            self.client.admin.command("ping")
        except errors.ServerSelectionTimeoutError as e:
            raise ConnectionError(f"Could not connect to MongoDB: {e}") from e
        except errors.PyMongoError as e:
            # Includes AuthenticationFailed and other auth issues
            raise ConnectionError(f"Mongo error during connect/auth: {e}") from e

        self.database = self.client[self.db_name]
        self.collection = self.database[self.col_name]

    # --------------- C — CREATE ---------------
    def create(self, document: Dict) -> bool:
        if not isinstance(document, dict) or not document:
            raise ValueError("create() requires a non-empty dict")
        try:
            result = self.collection.insert_one(document)
            return bool(result.acknowledged)
        except errors.PyMongoError as e:
            print(f"[CREATE] Insert failed: {e}")
            return False

    # --------------- R — READ ---------------
    def read(self, query: Dict, projection: Optional[Dict] = None) -> List[Dict]:
        if not isinstance(query, dict):
            raise ValueError("read() requires a dict query")
        try:
            cursor = self.collection.find(query, projection)
            return list(cursor)
        except errors.PyMongoError as e:
            print(f"[READ] Query failed: {e}")
            return []

    # --------------- U — UPDATE ---------------
    def update(self, query: Dict, new_values: Dict, many: bool = False) -> int:
        if not isinstance(query, dict):
            raise ValueError("update() requires a dict query")
        if not isinstance(new_values, dict) or not new_values:
            raise ValueError("update() requires a non-empty dict of new_values")
        try:
            update_doc = {"$set": new_values}
            if many:
                result = self.collection.update_many(query, update_doc)
            else:
                result = self.collection.update_one(query, update_doc)
            return int(result.modified_count)
        except errors.PyMongoError as e:
            print(f"[UPDATE] Failed: {e}")
            return 0

    # --------------- D — DELETE ---------------
    def delete(self, query: Dict, many: bool = False) -> int:
        if not isinstance(query, dict) or not query:
            raise ValueError("delete() requires a non-empty dict query")
        try:
            if many:
                result = self.collection.delete_many(query)
            else:
                result = self.collection.delete_one(query)
            return int(result.deleted_count)
        except errors.PyMongoError as e:
            print(f"[DELETE] Failed: {e}")
            return 0
