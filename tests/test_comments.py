import unittest
from app.models import Comment, User
from app import db


class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_eugene = User(username='eugene', password='emancipation')
        self.new_comment = Comment(pitch_id=555)

    # def tearDown(self):
    #         Review.query.delete()
    #         User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.pitch_id, 555)

        # self.assertEquals(self.new_comment.user,self.user_naiyoma)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()) > 0)

    def test_get_comment_by_id(self):
        self.new_comment.save_comment()
        got_comments = Comment.get_comments(555)
        self.assertTrue(len(got_comments) == 1)