from sqlalchemy import func
from hypothesis import given, settings
from hypothesis.strategies import characters, text

from reqherd.webservice.db.session import SessionLocal
from reqherd.webservice.models.hardreq import Hardware_Requirement


from tests import API_ENDPOINTS, BaseCrudResponseTest, SystemRequirementSetupMixin


class TestHardwareRequirementsEndpoint(
    BaseCrudResponseTest, SystemRequirementSetupMixin
):
    @settings(deadline=None)
    @given(
        text(
            alphabet=characters(
                max_codepoint=250,
                blacklist_categories=("M", "N", "P", "S", "C", "Z"),
            )
        ),
    )
    def test_hardware_requirements_crud(self, t):
        self.kwargs["text"] = t
        related_system_requirement_id = self.setup_and_test_related_system_requirement()

        record = [
            {
                "doc_prefix": t,
                "definition": t,
                "system_requirement_id": related_system_requirement_id,
            },
        ]
        post_response = self.client.post(
            API_ENDPOINTS["hardreqs"],
            headers={"Content-Type": "application/json"},
            json=record,
        )
        self.assertEqual(post_response.status_code, 200)

        get_response = self.client.get(API_ENDPOINTS["hardreqs"])
        self.assertEqual(get_response.status_code, 200)

        db = SessionLocal()
        max_hardreq = db.query(func.max(Hardware_Requirement.id)).first()[0]
        out_of_bounds_hardreq = max_hardreq + 1
        db.close()

        not_found_get_response = self.client.get(
            f'{API_ENDPOINTS["hardreqs"]}{out_of_bounds_hardreq}'
        )
        self.assertEqual(not_found_get_response.status_code, 404)

        get_by_id_response = self.client.get(
            f'{API_ENDPOINTS["hardreqs"]}{max_hardreq}'
        )
        self.assertEqual(get_by_id_response.status_code, 200)

        put_record = {
            "doc_prefix": t,
            "definition": t,
            "system_requirement_id": related_system_requirement_id,
        }

        not_found_put_response = self.client.put(
            f'{API_ENDPOINTS["hardreqs"]}{out_of_bounds_hardreq}',
            headers={"Content-Type": "application/json"},
            json=put_record,
        )
        self.assertEqual(not_found_put_response.status_code, 404)

        put_response = self.client.put(
            f'{API_ENDPOINTS["hardreqs"]}{max_hardreq}',
            headers={"Content-Type": "application/json"},
            json=put_record,
        )
        self.assertEqual(put_response.status_code, 200)

        # not_found_delete_response = self.client.delete(
        #     f'{API_ENDPOINTS["hardreqs"]}{out_of_bounds_hardreq}'
        # )
        # self.assertEqual(not_found_delete_response.status_code, 404)

        delete_response = self.client.delete(
            f'{API_ENDPOINTS["hardreqs"]}{max_hardreq}',
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(delete_response.status_code, 200)
