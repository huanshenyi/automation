import unittest


class FirstCase01(unittest.TestCase):

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
    def testfirst01(self):
        print('1-case')

    def testfirst02(self):
        print('2-case')

    def testfirst03(self):
        print('3-case')


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01('testfirst02'))
    suite.addTest(FirstCase01('testfirst01'))
    suite.addTest(FirstCase01('testfirst3'))
    unittest.TextTestRunner().run(suite)