from sqlalchemy import func
from hypothesis import given, settings
from hypothesis.strategies import characters, text

from reqherd.webservice.db.session import SessionLocal
from reqherd.webservice.models.sysreq import System_Requirement


from tests import API_ENDPOINTS, BaseCrudResponseTest


class TestSystemRequirementsEndpoint(BaseCrudResponseTest):
    @settings(deadline=None)
    @given(
        text(
            alphabet=characters(
                max_codepoint=250,
                blacklist_categories=("M", "N", "P", "S", "C", "Z"),
            )
        ),
    )
    def test_system_requirements_crud(self, t):
        record = [
            {
                "doc_prefix": t,
                "definition": t,
            },
        ]
        post_response = self.client.post(
            API_ENDPOINTS["sysreqs"],
            headers={"Content-Type": "application/json"},
            json=record,
        )
        self.assertEqual(post_response.status_code, 200)

        get_response = self.client.get(API_ENDPOINTS["sysreqs"])
        self.assertEqual(get_response.status_code, 200)

        db = SessionLocal()
        max_sysreq = db.query(func.max(System_Requirement.id)).first()[0]
        out_of_bounds_sysreq = max_sysreq + 1
        db.close()

        not_found_get_response = self.client.get(
            f'{API_ENDPOINTS["sysreqs"]}{out_of_bounds_sysreq}'
        )
        self.assertEqual(not_found_get_response.status_code, 404)
        
        get_by_id_response = self.client.get(f'{API_ENDPOINTS["sysreqs"]}{max_sysreq}')
        self.assertEqual(get_by_id_response.status_code, 200)

        put_record = {
            "doc_prefix": t,
            "definition": t,
        }

        not_found_put_response = self.client.put(
            f'{API_ENDPOINTS["sysreqs"]}{out_of_bounds_sysreq}',
            headers={"Content-Type": "application/json"},
            json=put_record,
        )
        self.assertEqual(not_found_put_response.status_code, 404)

        put_response = self.client.put(
            f'{API_ENDPOINTS["sysreqs"]}{max_sysreq}',
            headers={"Content-Type": "application/json"},
            json=put_record,
        )
        self.assertEqual(put_response.status_code, 200)

        not_found_delete_response = self.client.delete(
            f'{API_ENDPOINTS["sysreqs"]}{out_of_bounds_sysreq}'
        )
        self.assertEqual(not_found_delete_response.status_code, 404)

        delete_response = self.client.delete(
            f'{API_ENDPOINTS["sysreqs"]}{max_sysreq}',
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(delete_response.status_code, 200)
