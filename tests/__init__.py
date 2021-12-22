from unittest import TestCase
from fastapi.testclient import TestClient

from main import reqherd
from reqherd.webservice.db.base import Base
from reqherd.webservice.db.session import engine


API_ENDPOINTS = {
    "sysreqs": "reqherd/api/v1/system-requirements/",
    "softreqs": "reqherd/api/v1/software-requirements/",
    "hardreqs": "reqherd/api/v1/hardware-requirements/",
}


class BaseCrudResponseTest(TestCase):
    def setUp(self) -> None:
        self.client = TestClient(reqherd)
        self.kwargs = dict()
        return super().setUp()

    def tearDown(self) -> None:
        metadata = Base.metadata
        for table in reversed(metadata.sorted_tables):
            engine.execute(table.delete())


class SystemRequirementSetupMixin:
    def setup_and_test_related_system_requirement(self):
        record = [
            {
                "doc_prefix": self.kwargs["text"],
                "definition": self.kwargs["text"],
            },
        ]
        post_response = self.client.post(
            API_ENDPOINTS["sysreqs"],
            headers={"Content-Type": "application/json"},
            json=record,
        )
        self.assertEqual(post_response.status_code, 200)
        return post_response.json()[0]["id"]
