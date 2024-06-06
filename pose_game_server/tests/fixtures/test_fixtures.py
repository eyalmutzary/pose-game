import pytest
from models.test import DescriptionType, TestModel
from models.test_equipment import TestEquipment


@pytest.fixture
def example_fixture() -> TestEquipment:
    return ExampleFixture(
        **{
            "example": "example"
        }
    )
