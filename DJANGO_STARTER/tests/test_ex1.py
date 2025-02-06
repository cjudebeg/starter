# import pytest
# from django.contrib.auth.models import User


def test_check_username2(user_1):
    print("create-user1")
    assert user_1.username == "test-user"


def test_check_username(user_1):
    print("create-user2")
    assert user_1.username == "test-user"
    assert user_1.is_superuser == 0


def test_new_user(new_user):
    print(new_user.first_name)
    assert new_user.first_name == "MyName"


def test_new_user2(new_user2):
    print(new_user2.username)
    assert new_user2.username == "test_user"
