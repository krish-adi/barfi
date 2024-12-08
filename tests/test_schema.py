import pytest
import tempfile
from contextlib import contextmanager
from typing import Generator
from pathlib import Path
from barfi.st_flow.schema.manage import SchemaManager
from barfi.st_flow.flow.types import FlowSchema, FlowViewport, SCHEMA_VERSION


@contextmanager
def temp_schema_setup() -> Generator[Path, None, None]:
    """Create a temporary directory and yield the path for schema testing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        schema_dir = Path(temp_dir) / "schema_test"
        schema_dir.mkdir()
        yield schema_dir


@pytest.fixture
def schema_manager():
    """Create a SchemaManager instance with temporary directory."""
    with temp_schema_setup() as schema_dir:
        yield SchemaManager(filename="schemas.barfi", filepath=str(schema_dir))


@pytest.fixture
def sample_flow_schema():
    """Create a sample FlowSchema for testing."""
    return FlowSchema(
        version=SCHEMA_VERSION,
        nodes=[],
        connections=[],
        viewport=FlowViewport(x=0, y=0, zoom=1),
    )


def test_init_creates_empty_schema_file():
    """Test that initializing SchemaManager creates an empty schema file."""
    with temp_schema_setup() as schema_dir:
        manager = SchemaManager(filepath=str(schema_dir))
        schema_file = schema_dir / "schemas.barfi"
        assert schema_file.exists()
        assert manager.schema_names == []


def test_save_and_load_schema(schema_manager, sample_flow_schema):
    """Test saving and loading a schema."""
    schema_name = "test_schema"
    schema_manager.save_schema(schema_name, sample_flow_schema)

    # Test loading
    loaded_schema = schema_manager.load_schema(schema_name)
    assert loaded_schema == sample_flow_schema
    assert schema_name in schema_manager.schema_names


def test_save_existing_schema_raises_error(schema_manager, sample_flow_schema):
    """Test that saving a schema with existing name raises ValueError."""
    schema_name = "test_schema"
    schema_manager.save_schema(schema_name, sample_flow_schema)

    with pytest.raises(ValueError, match=r".*already exists.*"):
        schema_manager.save_schema(schema_name, sample_flow_schema)


def test_update_schema(schema_manager, sample_flow_schema):
    """Test updating an existing schema."""
    schema_name = "test_schema"
    schema_manager.save_schema(schema_name, sample_flow_schema)

    updated_schema = FlowSchema(
        version=SCHEMA_VERSION,
        nodes=[],
        connections=[],
        viewport=FlowViewport(x=100, y=100, zoom=2),
    )
    schema_manager.update_schema(schema_name, updated_schema)

    loaded_schema = schema_manager.load_schema(schema_name)
    assert loaded_schema == updated_schema


def test_update_nonexistent_schema_raises_error(schema_manager, sample_flow_schema):
    """Test that updating a non-existent schema raises ValueError."""
    with pytest.raises(ValueError, match=r".*not found.*"):
        schema_manager.update_schema("nonexistent", sample_flow_schema)


def test_upsert_schema(schema_manager, sample_flow_schema):
    """Test upserting schemas (both new and existing)."""
    schema_name = "test_schema"

    # Test insert
    schema_manager.upsert_schema(schema_name, sample_flow_schema)
    assert schema_manager.load_schema(schema_name) == sample_flow_schema

    # Test update
    updated_schema = FlowSchema(
        version=SCHEMA_VERSION,
        nodes=[],
        connections=[],
        viewport=FlowViewport(x=200, y=200, zoom=3),
    )
    schema_manager.upsert_schema(schema_name, updated_schema)
    assert schema_manager.load_schema(schema_name) == updated_schema


def test_delete_schema(schema_manager, sample_flow_schema):
    """Test deleting a schema."""
    schema_name = "test_schema"
    schema_manager.save_schema(schema_name, sample_flow_schema)

    schema_manager.delete_schema(schema_name)
    assert schema_name not in schema_manager.schema_names

    with pytest.raises(ValueError, match=r".*not found.*"):
        schema_manager.load_schema(schema_name)


def test_delete_nonexistent_schema_raises_error(schema_manager):
    """Test that deleting a non-existent schema raises ValueError."""
    with pytest.raises(ValueError, match=r".*not found.*"):
        schema_manager.delete_schema("nonexistent")


def test_schema_persistence(sample_flow_schema):
    """Test that schemas persist between SchemaManager instances."""
    schema_name = "test_schema"

    with temp_schema_setup() as schema_dir:
        # First manager instance
        manager1 = SchemaManager(filepath=str(schema_dir))
        manager1.save_schema(schema_name, sample_flow_schema)

        # Second manager instance
        manager2 = SchemaManager(filepath=str(schema_dir))
        loaded_schema = manager2.load_schema(schema_name)

        assert schema_name in manager2.schema_names
        assert loaded_schema == sample_flow_schema
