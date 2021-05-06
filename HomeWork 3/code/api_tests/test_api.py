import pytest

from api_tests.base_api import BaseApi


class TestApi(BaseApi):
    @pytest.mark.API
    def test_create_topic(self):
        new_company_id = self.api_client.post_topic()["id"]
        assert self.api_client.get_check_company(new_company_id)
        self.api_client.post_delete_compaign(new_company_id)

    @pytest.mark.API
    def test_create_segment(self):
        new_segment_id = self.api_client.post_create_segment()
        assert self.api_client.get_check_segment(new_segment_id)
        self.api_client.delete_segment(new_segment_id)

    @pytest.mark.API
    def test_delete_segment(self):
        new_segment_id = self.api_client.post_create_segment()
        self.api_client.delete_segment(new_segment_id)
        assert not self.api_client.get_check_segment(new_segment_id)
