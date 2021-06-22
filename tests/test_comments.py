from app.models import Blog, Comment ,User
from app import db
import unittest

class TestBlogs(unittest.TestCase):

    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_blog = Blog(title='this is a blog',blog='this is a blog being tested',user = self.user_James )
        self.new_comment = Comment(comment='this is a blog being tested',user = self.user_James, blog = self.new_blog )

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals (self.new_comment.comment,'this is a blog')
        self.assertEquals(self.new_comment.blog,self.new_blog)
        self.assertEquals(self.new_comment.user,self.user_James)

    def test_save_comment(self):
            self.new_comment.save_comment()
            self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):

            self.new_comment.save_comment()
            get_comments = Comment.get_comments(12345)
            self.assertTrue(len(get_comments) == 1)

if __name__ == '__main__':
    unittest.main().run()