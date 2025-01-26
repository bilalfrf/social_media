# update_comments.py
from pymongo import MongoClient
from bson import ObjectId

# MongoDB bağlantısı
client = MongoClient('mongodb://localhost:27017/')
db = client['social_media_app']
stories_collection = db['stories']

# Tüm belgeleri güncelle
for story in stories_collection.find():
    comments = story.get('comments', [])
    for comment in comments:
        if '_id' not in comment:
            comment['_id'] = ObjectId()
            stories_collection.update_one(
                {'_id': story['_id'], 'comments.content': comment['content']},
                {'$set': {'comments.$._id': comment['_id']}}
            )

print("Veritabanı güncelleme tamamlandı.")


