# update_likes_dislikes.py
from pymongo import MongoClient

# MongoDB bağlantısı
client = MongoClient('mongodb://localhost:27017/')
db = client['social_media_app']
stories_collection = db['stories']

# Tüm belgeleri güncelle
for story in stories_collection.find():
    # likes ve dislikes alanlarını sayısal değerlere çevirin
    if isinstance(story.get('likes'), list):
        stories_collection.update_one({'_id': story['_id']}, {'$set': {'likes': len(story['likes'])}})
    if isinstance(story.get('dislikes'), list):
        stories_collection.update_one({'_id': story['_id']}, {'$set': {'dislikes': len(story['dislikes'])}})
    for comment in story.get('comments', []):
        if isinstance(comment.get('likes'), list):
            stories_collection.update_one(
                {'_id': story['_id'], 'comments._id': comment['_id']},
                {'$set': {'comments.$.likes': len(comment['likes'])}}
            )
        if isinstance(comment.get('dislikes'), list):
            stories_collection.update_one(
                {'_id': story['_id'], 'comments._id': comment['_id']},
                {'$set': {'comments.$.dislikes': len(comment['dislikes'])}}
            )


