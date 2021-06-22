from app.models import Blog, Comment ,User
from app import db
import unittest

class TestBlogs(unittest.TestCase):

    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_blog = Blog(title='this is a blog',blog='this is a blog being tested',user = self.user_James )
        self.new_comment = Comment(comment='this is a blog being tested',user = self.user_James, blog = self.new_blog )

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals (self.new_blog.title,'this is a blog')
        self.assertEquals (self.new_blog.blog,'this is a blog being tested')
        self.assertEquals(self.new_blog.user,self.user_James)

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)

    def test_get_blog_by_id(self):

        self.new_blog.save_blog()
        get_blogs = Blog.get_blogs(12345)
        self.assertTrue(len(get_blogs) == 1)

if __name__ == '__main__':
    unittest.main().run()