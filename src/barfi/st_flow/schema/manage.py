import gzip
import json
import os
from typing import Dict


class SchemaManager:
    """Manages schema operations for loading, saving, and deleting schemas.

    Handles schema persistence using a gzipped JSON file at the specified location.
    The schema data structure maintains a list of schema names and their corresponding data.
    """

    def __init__(self, filename: str = "v1_schemas.json.gz", filepath: str = "./"):
        """Initialize SchemaManager with storage configuration.

        Args:
            filename (str): Name of the schema storage file. Defaults to "schemas.json.gz".
            filepath (str): Directory path for schema storage. Defaults to "./".
        """
        self.filename = filename
        self.filepath = filepath
        self._full_file_path = os.path.abspath(os.path.join(filepath, filename))

        self._schemas = self._read_file()

    @property
    def schema_names(self):
        return list(self._schemas.keys())

    @property
    def schemas(self):
        return self._schemas

    def _read_file(self) -> Dict:
        """Load schemas from the gzipped JSON storage file.

        Returns:
            Dict: Schema storage containing:
                - schema_names (List[str]): Available schema identifiers
                - schemas (Dict): Schema data mapped by schema names

        Note:
            Creates an empty schema file if none exists.
        """
        try:
            with gzip.open(self._full_file_path, "rt", encoding="UTF-8") as handle_read:
                schemas = json.load(handle_read)
        except FileNotFoundError:
            schemas = {}
            with gzip.open(
                self._full_file_path, "wt", encoding="UTF-8"
            ) as handle_write:
                json.dump(schemas, handle_write)

        return schemas

    def _write_file(self):
        """Persist schemas to the gzipped JSON storage file.

        Note:
            Writes the current state of self._schemas to storage.
        """
        with gzip.open(self._full_file_path, "wt", encoding="UTF-8") as handle_write:
            json.dump(self._schemas, handle_write)

    def save_schema(self, schema_name: str, schema_data: Dict):
        """Store a schema with the given name.

        Args:
            schema_name (str): Unique identifier for the schema
            schema_data (Dict): Schema configuration to store
        """
        self._schemas[schema_name] = schema_data
        self._write_file()

    def load_schema(self, schema_name: str) -> Dict:
        """Retrieve a schema by its name.

        Args:
            schema_name (str): Identifier of the schema to load

        Returns:
            Dict: Schema configuration data

        Raises:
            ValueError: When schema_name doesn't exist in storage
        """
        if schema_name in self._schemas:
            return self._schemas[schema_name]

        raise ValueError(f"Schema :{schema_name}: not found in the saved schemas")

    def delete_schema(self, schema_name: str):
        """Remove a schema from storage.

        Args:
            schema_name (str): Identifier of the schema to delete

        Raises:
            ValueError: When schema_name doesn't exist in storage
        """
        if schema_name in self._schemas:
            del self._schemas[schema_name]
        else:
            raise ValueError(f"Schema :{schema_name}: not found in the saved schemas")

        self._write_file()
