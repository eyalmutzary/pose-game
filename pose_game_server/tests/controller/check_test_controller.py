from http import HTTPStatus
from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient
from models.test import DescriptionType, TestModel
from server.app import app
from services.test_service import TestService
from models.test_equipment import TestEquipment
from config.constants import TEST_SCHEMA_VERSION

client = TestClient(app)


def check_create_test_success(test_model_template: TestModel):
    with patch.object(TestService, "create_test", new_callable=AsyncMock) as mock:
        mock.return_value = "test_id"
        response = client.post(
            f"/tests/create/{DescriptionType.TEMPLATE.value}",
            json=test_model_template.model_dump(mode="json"),
            timeout=3,
        )
    assert response.status_code == HTTPStatus.CREATED


def check_create_test_invalid_schema_version(test_model_template: TestModel):
    with patch.object(TestService, "create_test", new_callable=AsyncMock) as mock:
        mock.return_value = "test_id"
        req_body = test_model_template.model_dump(mode="json")
        req_body["test_description"]["metadata"]["schema_version"] = "invalid_schema_version"
        response = client.post(
            f"/tests/create/{DescriptionType.TEMPLATE.value}",
            json=req_body,
            timeout=3,
        )
    assert response.status_code == HTTPStatus.NOT_ACCEPTABLE  # TODO: set different status code


def check_get_tests():
    with patch.object(TestService, "get_tests", new_callable=AsyncMock) as mock:
        mock.return_value = []
        response = client.get("/tests/")
    assert response.status_code == HTTPStatus.OK


def check_update_test(test_model_template: TestModel):
    with patch.object(TestService, "get_tests", new_callable=AsyncMock) as mock_get, patch.object(
        TestService, "update_test", new_callable=AsyncMock
    ) as mock_update:
        mock_get.return_value = [test_model_template]
        mock_update.return_value = None
        response = client.put("/tests/update/test_id", json=test_model_template.model_dump(mode="json"))
    assert response.status_code == HTTPStatus.OK


def check_delete_test():
    with patch.object(TestService, "delete_test", new_callable=AsyncMock) as mock:
        mock.return_value = None
        response = client.delete("/tests/delete/test_id")
    assert response.status_code == HTTPStatus.OK


def check_execute_test(test_equipment: TestEquipment, test_model_executable):
    with patch.object(TestService, "execute_test", new_callable=AsyncMock) as mock:
        mock.return_value = test_model_executable
        response = client.post("/tests/execute/test_id", json={"test_equipment":test_equipment.model_dump(mode="json")})
    assert response.status_code == HTTPStatus.OK
    

def check_get_schema_version():
    response = client.get("/tests/schema_version")
    assert response.status_code == HTTPStatus.OK
    assert response.json()["data"] == {"schema_version": TEST_SCHEMA_VERSION}
