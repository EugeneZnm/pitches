import unittest
from app.models import Pitches, User


class PostModelTest(unittest.TestCase):

    def setUp(self):
        self.user_eugene = User(username='eugene', email='eugenenzioki@gmail.com',password='redding', )
        self.new_pitch = Pitches(title='a', post='b', category='d', posts=self.user_eugene)

    def test_instance(self):
        self.assertEqual(self.new_pitch.title, 'a')
        self.assertEqual(self.new_pitch, 'b')
        self.assertEqual(self.new_pitch.category, 'd')

    def test_save_post(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitches.query.all()) > 0)

    def test_get_post_by_id(self):
        self.new_pitch.save_pitch()
        got_pitch = Pitches.get_pitch(1)
        self.assertTrue(len(got_pitch) > 0)


if __name__ == '__main__':
    unittest.main()