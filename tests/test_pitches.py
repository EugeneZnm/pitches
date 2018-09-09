from app.models import Pitches, User
from app import db


def setUp(self):
    self.user_James = User(username='Eugene', password='redding', email='eugenenzioki@gmail.com')
    self.pitch = Pitches(id=1, category='promotional', pitch='', user=self.user_Eugene)


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
    self.assertEquals(self.pitch.id, 1)
    self.assertEquals(self.pitch.category, 'promotional')
    self.assertEquals(self.pitch.user, self.user_Eugene)


def test_save_pitch(self):
    self.pitch.save_pitch()
    self.assertTrue(len(Pitches.query.all()) > 0)


def test_get_pitch_by_category(self):
    self.new_review.save_pitch()
    got_pitches = Pitches.get_pitch('promotional')
    self.assertTrue(len(got_pitches) == 1)
