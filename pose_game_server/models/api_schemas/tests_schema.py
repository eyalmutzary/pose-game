from models.test_description import BaseTestDescription
from models.test_equipment import TestEquipment
from pydantic import BaseModel


class CreateTestBodySchema(BaseModel):
    test_description: BaseTestDescription


class UpdateTestBodySchema(BaseModel):
    test_description: BaseTestDescription


class ExecuteTestBodySchema(BaseModel):
    test_equipment: TestEquipment
