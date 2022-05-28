from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
import json
from news.models import Post, PostLike

from api.news.serializers import ListPostSerializer
from django.db import models




class BlogTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="Hamel")

        Post.objects.create(author=user,
                            title="Test post",
                            trans_title="Test post",
                            short_description="Short_description",
                            content="Text",
                            preview='test_image.jpg')
        PostLike.objects.create(
            ip='127.0.0.1',
            post=Post.objects.get(title='Test post'),
            value=1,
        )

    def test_post(self):
        """Есть ли post в бд"""
        post = Post.objects.get(title="Test post")
        self.assertEqual(post.short_description, "Short_description")

