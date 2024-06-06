import http
import os
from typing import Any, Dict, List, Optional

import yaml
from controller.context_manager import context_log_meta
from dal.test_dal import TestDAL
from logger import logger
from models.base import GenericResponseModel
from models.test import DescriptionType, TestModel
from models.test_description import BaseTestDescription, TestGroup
from models.test_equipment import TestEquipment
from utils.exceptions import AppException


class TestService:
    __ERROR_NO_TEST_FOUND: str = "Test not found"

    @staticmethod
    async def create_test(test: TestModel) -> str:
        test_id = await TestDAL.create(test)
        return test_id

    @staticmethod
    async def get_tests(
        description_type: Optional[DescriptionType] = None, id: Optional[str] = None, group: Optional[TestGroup] = None
    ) -> List[TestModel]:
        filter = TestService._build_filter(description_type, id, group)
        tests = await TestDAL.get_all(filter)
        return tests

    @staticmethod
    async def update_test(test: TestModel) -> None:
        await TestDAL.update(test)

    @staticmethod
    async def delete_test(id: str) -> None:
        await TestDAL.delete(id)

    @staticmethod
    async def execute_test(test_id: str, equipment: TestEquipment) -> TestModel:
        found_test = await TestDAL.get_all(TestService._build_filter(id=test_id))
        if not found_test:
            raise AppException(status_code=http.HTTPStatus.NOT_FOUND, message=TestService.__ERROR_NO_TEST_FOUND)
        test_json = found_test[0].model_dump(mode="json")
        test_json["test_description"]["metadata"]["equipment"] = equipment
        test_json["description_type"] = DescriptionType.EXECUTABLE
        test_model = TestModel(**test_json)  # validate model
        TestService._send_test_to_dag_factory(test_model)
        return test_model

    @staticmethod
    def _build_filter(
        description_type: Optional[DescriptionType] = None, id: Optional[str] = None, group: Optional[TestGroup] = None
    ) -> Dict[str, Any]:
        filter_dict = {}

        if id:
            filter_dict["id"] = id

        if description_type:
            filter_dict["description_type"] = description_type

        if group:
            filter_dict["group"] = group

        return filter_dict

    @staticmethod
    def _send_test_to_dag_factory(test: TestModel) -> None:
        yaml_data = yaml.dump(test.test_description.model_dump(mode="json"), sort_keys=False)
        folder_path = os.path.join(os.getcwd(), "executable_tests")
        filename: str = (
            f"{test.test_description.metadata.test_group}_{test.test_description.metadata.test_number}_{test.test_description.metadata.test_name}_{test.id[:8]}"
        )
        file_path = os.path.join(folder_path, filename + ".yaml")
        with open(file_path, "w") as file:
            file.write(yaml_data)
