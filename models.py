# models.py
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_login import UserMixin
from bson import ObjectId

mongo = PyMongo()
bcrypt = Bcrypt()


def init_app(app):
    mongo.init_app(app)
    bcrypt.init_app(app)


class User(UserMixin):
    def __init__(self, user_dict):
        self.id = str(user_dict['_id'])
        self.username = user_dict['username']
        self.email = user_dict['email']
        self.password = user_dict['password']
        self.followers = user_dict.get('followers', [])
        self.following = user_dict.get('following', [])
        self.active = user_dict.get('active', True)
        self.is_confirmed = user_dict.get('is_confirmed', False)  # Yeni attribute

    @property
    def is_active(self):
        return self.active

    @staticmethod
    def create_user(username, email, password, confirmation_code):
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        user_id = mongo.db.users.insert_one({
            'username': username,
            'email': email,
            'password': password_hash,
            'is_confirmed': False,
            'confirmation_code': confirmation_code,
            'followers': [],
            'following': [],
            'active': True
        }).inserted_id
        return user_id

    @staticmethod
    def get_user_by_email(email):
        user_dict = mongo.db.users.find_one({'email': email})
        if user_dict:
            return User(user_dict)
        return None

    @staticmethod
    def get_user_by_id(user_id):
        user_dict = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        if user_dict:
            return User(user_dict)
        return None

    @staticmethod
    def follow_user(current_user_id, to_follow_user_id):
        mongo.db.users.update_one({'_id': ObjectId(current_user_id)}, {'$addToSet': {'following': to_follow_user_id}})
        mongo.db.users.update_one({'_id': ObjectId(to_follow_user_id)}, {'$addToSet': {'followers': current_user_id}})

    @staticmethod
    def unfollow_user(current_user_id, to_unfollow_user_id):
        mongo.db.users.update_one({'_id': ObjectId(current_user_id)}, {'$pull': {'following': to_unfollow_user_id}})
        mongo.db.users.update_one({'_id': ObjectId(to_unfollow_user_id)}, {'$pull': {'followers': current_user_id}})


