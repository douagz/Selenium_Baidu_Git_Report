import pytest
from common.load_baidu_search_data import load_baidu_search_data


class TestBaiduSearch:
    baidu_search_data = load_baidu_search_data()

    @pytest.mark.parametrize("search_data", baidu_search_data)
    def test_baidu_search_01(self, baidu_search_page, baidu_result_page, search_data):
        baidu_search_page.load()
      
        baidu_search_page.search(search_data['phrase'])
      
        assert baidu_result_page.get_title() == search_data['expected_title']
        assert baidu_result_page.result_link_titles_contain_phrase(search_data['phrase'])
