import pytest
from config.setting import DATA_PATH,log,proxies
from utlis.http_request import HttpRequest
from utlis.DoData import DoData
import requests
import json
import allure



cases = DoData.to_excel('cases.xls',5)

@pytest.mark.parametrize("case",cases)
def test_ai(case):
        url = case['url']
        expect_result = str(int(case['expected']))
        r = HttpRequest(url)
        result = r.get()
        status_code = result.status_code
        log.debug('下载文件的大小是%s'%status_code)
        try:
            status_code==expect_result
            DoData.write_excel('cases.xls',case['case_id'],status_code,5,'PASS')
        except AssertionError as e:
            DoData.write_excel('cases.xls', case['case_id'],status_code,5,'FAIL')
            raise e






