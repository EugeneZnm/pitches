from app.models import Pitches,User
from app import db


def setUp(self):
    self.user_James = User(username='Eugene', password='redding', email='eugenenzioki@gmail.com')
    self.new_pitches = Pitches(id=1, category='promotional', pitch='', user=self.user_Eugene)


def tearDown(self):
    """
    tear down method
    """
    Pitches.query.delete()
    """
    delete all pitches from database
    """
    User.query.delete()
    """
    delete all users from database
    """


def test_check_instance_variables(self):
    self.assertEquals(self.new_pitches.id, 1)
    self.assertEquals(self.new_pitches.category, 'promotional')
    self.assertEquals(self.new_review.user, self.user_Eugene)