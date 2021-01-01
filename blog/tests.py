from django.test import TestCase
from .models import Post, Category
# Create your tests here.

class Test(TestCase):
    def setUp(self):
        cat = Category.objects.create(name="Loki", body="Body")
        Post.objects.create(category = cat, title ="Post1" )

    def test_if_title_equals_post1(self):
        post = Post.objects.get(title = "Post1")
        self.assertEqual(post.title, "Post2")
