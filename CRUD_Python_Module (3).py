from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter:
    """CRUD class for the AAC animals collection."""

    def __init__(self, username, password):
        """Initialize the MongoDB connection using the AAC user account."""
        self.client = MongoClient(
            "mongodb://localhost:27017/",
            username=username,
            password=password,
            authSource="admin"
        )

        self.database = self.client["aac"]
        self.collection = self.database["animals"]

        # Verify that the connection and authentication work.
        self.client.admin.command("ping")

    def create(self, data):
        """Insert a document into the animals collection."""
        if not isinstance(data, dict) or not data:
            return False

        try:
            result = self.collection.insert_one(data)
            return result.inserted_id is not None

        except PyMongoError as error:
            print("Create operation failed:", error)
            return False

    def read(self, query):
        """Return documents matching the supplied query."""
        if not isinstance(query, dict):
            return []

        try:
            # find() returns a cursor, so convert it into a list.
            return list(self.collection.find(query))

        except PyMongoError as error:
            print("Read operation failed:", error)
            return []

    def update(self, query, update_data):
        """Update matching documents and return the number modified."""
        if not isinstance(query, dict) or not isinstance(update_data, dict):
            return 0

        try:
            result = self.collection.update_many(
                query,
                {"$set": update_data}
            )
            return result.modified_count

        except PyMongoError as error:
            print("Update operation failed:", error)
            return 0

    def delete(self, query):
        """Delete matching documents and return the number removed."""
        if not isinstance(query, dict):
            return 0

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count

        except PyMongoError as error:
            print("Delete operation failed:", error)
            return 0