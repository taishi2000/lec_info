from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Comment

# Create your tests here.

class CommentIndexTests(TestCase):
    def test_comment_index(self):
      response = self.client.get(reverse('lec_info:index'))
      self.assertEqual(response.status_code, 200)

    def test_comment_detail(self):
        comment = Comment.objects.create(
            title = "test title",
            text = "test text",
            created_time = timezone.now(),
            updated_time = timezone.now(),
        )
        url = reverse('lec_info:detail', args=(comment.id,))
        response = self.client.get(url)
        self.assertContains(response, "test title")
