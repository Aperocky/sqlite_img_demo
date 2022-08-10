# Creating mock data by injecting random data

from src.dao import Image, User, UserImage, get_dao, create_tables
import uuid
import os
import random

MOCK_IMG_DIR = "assets/static/images"


def inject_mock_data():
    create_tables()
    dao = get_dao()
    if dao.get_row_count(User.TABLE_NAME) > 0:
        print("Data already populated, delete data.db if you want fresh data")
        return
    # 10 random users
    random_user_ids = [str(uuid.uuid4()) for e in range(10)]
    users = [User(user_id=user_id, completed=False) for user_id in random_user_ids]
    dao.insert_items(users)
    insert_mock_images(dao)
    insert_mock_user_images(dao, random_user_ids)


def insert_mock_images(dao):
    imgs = os.listdir(MOCK_IMG_DIR)
    images = []
    for img in imgs:
        images.append(Image(ref=img))
    dao.insert_items(images)


def insert_mock_user_images(dao, user_ids):
    imgs = os.listdir(MOCK_IMG_DIR)
    # Generate random pairing of 5 images to user-ids
    user_images = []
    for user_id in user_ids:
        chosen_images = random.sample(imgs, 5)
        for image in chosen_images:
            user_images.append(UserImage(pair_id=str(uuid.uuid4()), user_id=user_id, ref=image))
    dao.insert_items(user_images)

