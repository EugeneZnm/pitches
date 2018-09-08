import unittest
from app.models import User


class UserModelsTest(unittest.TestCase):

    def setUp(self):
        """
        creating instance of user class
        :return:
        """
        self.__new__user = User(password = 'emancipation')

    def test_password_setter(self):
        """
        test case password setter ascertaining when password os being hashed
        :return:
        """
        self.assertTrue(self.__new__user.pass_secure is not None)

    def test_no_access(self):
        """
        confirming application raises attribute error attempt to access password property is made
        :return:
        """
        with self.assertRaises(AttributeError):
            self.__new__user.password

    def test_password_verification(self):
        """
        confirming password verification
        :return:
        """
        self.assertTrue(self.__new__user.verify_password('emancipation'))