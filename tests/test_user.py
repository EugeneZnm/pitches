import unittest
from app.models import User
from app import db


class UserModelsTest(unittest.TestCase):

    def setUp(self):
        """
        creating instance of user class
        :return:
        """
        self.new__user = User(email='x418087@gmail.com')

    def test_password_setter(self):
        """
        test case password setter ascertaining when password os being hashed
        :return:
        """
        self.assertTrue(self.new__user.pass_secure is not None)

    def test_no_access(self):
        """
        confirming application raises attribute error attempt to access password property is made
        :return:
        """
        with self.assertRaises(AttributeError):
            self.new__user.email

    def test_password_verification(self):
        """
        confirming password verification
        :return:
        """
        self.assertTrue(self.new__user.verify_email('x418087@gmail.com'))

    def save_account(self):
        db.session.add(self.new_user)
        db.session.commit()
        self.asserTrue(len(user.id) > 0)


if __name__ == '__main__':
    unittest.main()