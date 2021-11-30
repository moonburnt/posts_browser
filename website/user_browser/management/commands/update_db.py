import logging

import requests

from django.core.management.base import BaseCommand, CommandError

from user_browser.models import UsersModel, PostsModel
from urllib.parse import urljoin as join

log = logging.getLogger(__name__)

URL = "https://jsonplaceholder.typicode.com"
USERS_URL = join(URL, "users")
POSTS_URL = join(URL, "posts")

SESSION = None

def get_session() -> requests.Session:
    # #TODO: django probably has some dict-like shared storage similar to flask,
    # so this can be done with that thing, without involving globals
    global SESSION
    if SESSION is None:
        SESSION = requests.Session()

    return SESSION

def get_users(timeout:int = 30) -> list:
    """Retrieve list of users from api."""

    s = get_session()

    return s.get(USERS_URL, timeout=timeout).json()

def get_posts(timeout:int = 30) -> list:
    """Retrieve list of posts from api."""

    s = get_session()

    return s.get(POSTS_URL, timeout=timeout).json()

class Command(BaseCommand):
    help="Populate database with user data"

    def handle(self, *args, **kwargs):
        log.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            fmt='[%(asctime)s][%(name)s][%(levelname)s] %(message)s',
            datefmt='%H:%M:%S',
        )
        handler.setFormatter(formatter)
        log.addHandler(handler)

        log.info("Retrieving actual users")
        for user in get_users():
            record = UsersModel(
                _id = user["id"],
                name=user["name"],
                username=user["username"],
                email=user["email"],
                phone=user.get("phone", ""),
                website=user.get("website", ""),
            )
            record.save()


        log.info("Retrieving actual posts")
        for post in get_posts():
            record = PostsModel(
                _id = post["id"],
                user=UsersModel.objects.get(pk=post["userId"]),
                title=post["title"],
                body=post["body"],  
            )
            record.save()

        log.info("Done")
