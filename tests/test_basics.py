import unittest
from app.models import Vocabulary

class BasicsTestCase(unittest.TestCase):

    def setUp(self):
        pass
        # self.app = create_app('testing')
        # self.app_context = self.app.app_context()
        # self.app_context.push()
        # db.create_all()

    def tearDown(self):
        pass
        # db.session.remove()
        # db.drop_all()
        # self.app_context.pop()

    def test_cut(self):
        sentence = "9月的东城区电信局出账用户数"
        vol = Vocabulary(sentence)
        print(vol)
        # self.assertEqual(vol.query_json,json)
    # def test_app_exists(self):
    #     self.assertFalse(current_app is None)
    #
    # def test_app_is_testing(self):
    #     self.assertTrue(current_app.config['TESTING'])

print ('hello')



