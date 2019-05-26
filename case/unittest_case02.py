import unittest


class FirstCase02(unittest.TestCase):

    # 全てのケース実行する前のもの
    @classmethod
    def setUpClass(cls):
        print("これは全てcase実行前")

    # 全て終了後に実行するやつ
    @classmethod
    def tearDownClass(cls):
        print("これは全てcase実行後")

    # 前置き
    def setUp(self):
        print("caseのsetup")

    # 後置き
    def tearDown(self):
        print("caseのdown")

    # caseをスキップする
    @unittest.skip("case_1実行しない")
    def testfirst001(self):
        print('01-case')

    def testfirst002(self):
        print('02-case')

    def testfirst003(self):
        print('03-case')


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase02('testfirst002'))
    suite.addTest(FirstCase02('testfirst001'))
    suite.addTest(FirstCase02('testfirst003'))
    unittest.TextTestRunner().run(suite)