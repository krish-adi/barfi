import gzip
import json
import os
from typing import Dict, List
from barfi.flow.schema.types import FlowSchema, build_flow_schema_from_dict


class SchemaManager:
    """Manages schema operations for loading, saving, and deleting schemas.

    Handles schema persistence using a schemas.barfi gzipped JSON file.
    The schema data structure maintains a list of schema names and their corresponding data.
    """

    def __init__(self, filename: str = "schemas.barfi", filepath: str = "./"):
        """Initialize SchemaManager with storage configuration.

        Args:
            filename (str): Name of the schema storage file. Defaults to "schemas.barfi".
            filepath (str): Directory path for schema storage. Defaults to "./".
        """
        self.filename = filename
        self.filepath = filepath
        self._full_file_path = os.path.abspath(os.path.join(filepath, filename))

        self._schemas = self._read_file()

    @property
    def schema_names(self) -> List[str]:
        return list(self._schemas.keys())

    def _read_file(self) -> Dict[str, FlowSchema]:
        """Load schemas from the schemas.barfi gzipped JSON storage file.

        Returns:
            Dict[str, FlowSchema]: Dictionary mapping schema names to their FlowSchema data.
                                 Returns empty dict if no file exists.

        Note:
            Creates an empty schema file if none exists.
        """
        try:
            with gzip.open(self._full_file_path, "rt", encoding="UTF-8") as handle_read:
                schemas = {
                    k: build_flow_schema_from_dict(v)
                    for k, v in json.load(handle_read).items()
                }
        except FileNotFoundError:
            schemas = {}
            with gzip.open(
                self._full_file_path, "wt", encoding="UTF-8"
            ) as handle_write:
                json.dump(schemas, handle_write)

        return schemas

    def _write_file(self):
        """Persist schemas to the schemas.barfi gzipped JSON storage file.

        Note:
            Writes the current state of schemas to storage.
        """
        with gzip.open(self._full_file_path, "wt", encoding="UTF-8") as handle_write:
            json.dump({k: v.export() for k, v in self._schemas.items()}, handle_write)

    def save_schema(self, schema_name: str, flow_schema: FlowSchema):
        """Store a schema with the given name.

        Args:
            schema_name (str): Unique identifier for the schema
            flow_schema (FlowSchema): Schema configuration to store

        Raises:
            ValueError: When schema_name already exists in storage
        """
        if schema_name in self._schemas:
            raise ValueError(
                f"FlowSchema `{schema_name}` already exists. Use update_schema() to modify existing schemas."
            )

        self._schemas[schema_name] = flow_schema
        self._write_file()

    def update_schema(self, schema_name: str, flow_schema: FlowSchema):
        """Update an existing schema with new configuration.

        Args:
            schema_name (str): Identifier of the schema to update
            flow_schema (FlowSchema): New schema configuration

        Raises:
            ValueError: When schema_name doesn't exist in storage
        """
        if schema_name not in self._schemas:
            raise ValueError(
                f"FlowSchema `{schema_name}` not found. Use save_schema() to create new schemas."
            )

        self._schemas[schema_name] = flow_schema
        self._write_file()

    def upsert_schema(self, schema_name: str, flow_schema: FlowSchema):
        """Upsert a new schema with new configuration.

        Args:
            schema_name (str): Identifier of the schema to update
            flow_schema (FlowSchema): New schema configuration

        Raises:
            ValueError: When schema_name doesn't exist in storage
        """
        if schema_name in self._schemas:
            self.update_schema(schema_name, flow_schema)
        else:
            self.save_schema(schema_name, flow_schema)

    def load_schema(self, schema_name: str) -> FlowSchema:
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

        raise ValueError(f"FlowSchema `{schema_name}` not found in the saved schemas")

    def delete_schema(self, schema_name: str):
        """Remove a schema from storage.

        Args:
            schema_name (str): Identifier of the schema to delete

        Raises:
            ValueError: When schema_name doesn't exist in storage
        """
        if schema_name not in self._schemas:
            raise ValueError(
                f"FlowSchema `{schema_name}` not found in the saved schemas"
            )

        del self._schemas[schema_name]
        self._write_file()
