"""用户登陆测试"""
import unittest
import sys
sys.path.append("..")#提升包的搜索路径到项目路径下
from config import config as cf
from lib.read_excel import get_case_data
import json
import requests

class TestUserLogin(unittest.TestCase):

    def test_user_login_normal(self):
        # 用例数据
        case_data = get_case_data("test_user_data.xlsx", "TestUserLogin", "test_user_login_normal")
        url=case_data[1]
        data = json.loads(case_data[3])#json格式的字符串==》字典
        expect_res = case_data[4]

        # 发送请求
        res = requests.post(url=url, data=data)

        # 断言
        self.assertEqual(res.text, expect_res)

if __name__=="__main__":
    unittest.main()