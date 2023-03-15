import unittest


class TestFixtures01(unittest.TestCase):
    # 所有用例执行前执行
    def setUp(self) -> None:
        print("setUp开始")

    def tearDown(self) -> None:
        print("tearDown结束")

    # 每条用例执行前执行
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass开始")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass结束")

    # 测试用例
    def test_001(self):
        print("测试用例001")


class TestFixtures02(unittest.TestCase):
    def test_002(self):
        print("测试类2")


# 每个模块执行前执行
def setUpModule():
    """
    在所有测试类在调用之前会被执行一次,函数名是固定写法,会被unittest框架自动识别
    """
    print('集成测试 >>>>>>>>>>>>>>开始')


def tearDownModule():
    print("集成测试 >>>>>>>>>>>>>>结束")


if __name__ == '__main__':
    unittest.main()