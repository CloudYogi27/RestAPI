from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_eamil_successful(self):
        email = 'test1@example.com'
        password = 'pass123'
        user = get_user_model().objects.create_user(email = email, password = password,)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_emails = [
            ['test1@EXAMPLE.COM', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@ExAmple.com', 'TEST3@example.com'],
            ['test4@EXample.com', 'test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)


    def test_new_user_without_error_raise_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','pass1234')


    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            'admin@example.com', 'admin123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
