# main/routes.py
from bson import ObjectId
from flask import render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
from . import main
from models import mongo


@main.route('/edit_story/<story_id>', methods=['GET', 'POST'])
@login_required
def edit_story(story_id):
    story = mongo.db.stories.find_one({'_id': ObjectId(story_id)})
    if not story or story['user_id'] != current_user.id:
        flash('You are not authorized to edit this story.', 'danger')
        return redirect(url_for('main.stories'))

    if request.method == 'POST':
        content = request.form.get('story_content')
        media = request.files.get('story_media')

        if content:
            mongo.db.stories.update_one({'_id': ObjectId(story_id)}, {'$set': {'content': content}})

        if media:
            filename = secure_filename(media.filename)
            upload_path = os.path.join('static/uploads', filename)
            os.makedirs(os.path.dirname(upload_path), exist_ok=True)
            media.save(upload_path)
            if media.mimetype.startswith('image/'):
                media_type = 'image'
            elif media.mimetype.startswith('video/'):
                media_type = 'video'
            else:
                flash('Unsupported media type', 'danger')
                return redirect(url_for('main.stories'))

            mongo.db.stories.update_one({'_id': ObjectId(story_id)}, {'$set': {'media': filename, 'media_type': media_type}})

        flash('Story updated successfully!', 'success')
        return redirect(url_for('main.stories'))

    return render_template('edit_story.html', story=story)

@main.route('/edit_comment/<comment_id>', methods=['GET', 'POST'])
@login_required
def edit_comment(comment_id):
    story = mongo.db.stories.find_one({'comments._id': ObjectId(comment_id)})
    if not story:
        flash('Comment not found.', 'danger')
        return redirect(url_for('main.stories'))

    comment = next((c for c in story['comments'] if c['_id'] == ObjectId(comment_id)), None)
    if not comment or comment['user_id'] != current_user.id:
        flash('You are not authorized to edit this comment.', 'danger')
        return redirect(url_for('main.stories'))

    if request.method == 'POST':
        content = request.form.get('comment_content')
        if content:
            mongo.db.stories.update_one(
                {'comments._id': ObjectId(comment_id)},
                {'$set': {'comments.$.content': content}}
            )
            flash('Comment updated successfully!', 'success')
            return redirect(url_for('main.stories'))

    return render_template('edit_comment.html', comment=comment)


@main.route('/stories', methods=['GET'])
@login_required
def stories():
    stories = mongo.db.stories.find()
    return render_template('story.html', stories=stories)


@main.route('/add_story', methods=['GET', 'POST'])
@login_required
def add_story():
    if request.method == 'POST':
        content = request.form.get('story_content')
        media = request.files.get('story_media')

        if not content:
            flash('Story content is required', 'danger')
            return redirect(url_for('main.add_story'))

        story_data = {
            'user_id': current_user.id,
            'username': current_user.username,
            'content': content,
            'likes': 0,
            'dislikes': 0,
            'comments': []
        }

        if media:
            filename = secure_filename(media.filename)
            upload_path = os.path.join('static/uploads', filename)

            # Ensure the upload directory exists
            os.makedirs(os.path.dirname(upload_path), exist_ok=True)

            media.save(upload_path)
            story_data['media'] = filename
            if media.mimetype.startswith('image/'):
                story_data['media_type'] = 'image'
            elif media.mimetype.startswith('video/'):
                story_data['media_type'] = 'video'
            else:
                flash('Unsupported media type', 'danger')
                return redirect(url_for('main.add_story'))

        mongo.db.stories.insert_one(story_data)
        flash('Story added successfully!', 'success')
        return redirect(url_for('main.stories'))

    return render_template('add_story.html')


@main.route('/story/<story_id>/like', methods=['POST'])
@login_required
def like_story(story_id):
    story = mongo.db.stories.find_one({'_id': ObjectId(story_id)})
    if story:
        user_id = current_user.id
        if user_id not in story.get('user_likes', []):
            mongo.db.stories.update_one({'_id': ObjectId(story_id)}, {'$inc': {'likes': 1}, '$addToSet': {'user_likes': user_id}})
            if user_id in story.get('user_dislikes', []):
                mongo.db.stories.update_one({'_id': ObjectId(story_id)}, {'$inc': {'dislikes': -1}, '$pull': {'user_dislikes': user_id}})
            flash('Story liked!', 'success')
        else:
            mongo.db.stories.update_one({'_id': ObjectId(story_id)}, {'$inc': {'likes': -1}, '$pull': {'user_likes': user_id}})
            flash('Like removed!', 'success')

        story = mongo.db.stories.find_one({'_id': ObjectId(story_id)})
        return jsonify(success=True, likes=story['likes'], dislikes=story['dislikes'])


@main.route('/story/<story_id>/dislike', methods=['POST'])
@login_required
def dislike_story(story_id):
    story = mongo.db.stories.find_one({'_id': ObjectId(story_id)})
    if story:
        user_id = current_user.id
        if user_id not in story.get('user_dislikes', []):
            mongo.db.stories.update_one({'_id': ObjectId(story_id)}, {'$inc': {'dislikes': 1}, '$addToSet': {'user_dislikes': user_id}})
            if user_id in story.get('user_likes', []):
                mongo.db.stories.update_one({'_id': ObjectId(story_id)}, {'$inc': {'likes': -1}, '$pull': {'user_likes': user_id}})
            flash('Story disliked!', 'success')
        else:
            mongo.db.stories.update_one({'_id': ObjectId(story_id)}, {'$inc': {'dislikes': -1}, '$pull': {'user_dislikes': user_id}})
            flash('Dislike removed!', 'success')

        story = mongo.db.stories.find_one({'_id': ObjectId(story_id)})
        return jsonify(success=True, likes=story['likes'], dislikes=story['dislikes'])



@main.route('/story/<story_id>/comment', methods=['POST'])
@login_required
def add_comment(story_id):
    content = request.form.get('comment_content')
    if not content:
        flash('Comment content is required', 'danger')
        return redirect(url_for('main.stories'))

    comment_data = {
        '_id': ObjectId(),  # Benzersiz bir comment_id oluşturuyoruz
        'user_id': current_user.id,
        'username': current_user.username,
        'content': content,
        'likes': 0,
        'dislikes': 0,
        'user_likes': [],
        'user_dislikes': []
    }

    mongo.db.stories.update_one({'_id': ObjectId(story_id)}, {'$push': {'comments': comment_data}})
    flash('Comment added!', 'success')
    return redirect(url_for('main.stories'))


@main.route('/comment/<comment_id>/like', methods=['POST'])
@login_required
def like_comment(comment_id):
    print(f"Received like request for comment ID: {comment_id}")
    story = mongo.db.stories.find_one({'comments._id': ObjectId(comment_id)})
    if story:
        user_id = current_user.id
        for comment in story['comments']:
            if comment['_id'] == ObjectId(comment_id):
                if user_id not in comment.get('user_likes', []):
                    mongo.db.stories.update_one(
                        {'comments._id': ObjectId(comment_id)},
                        {
                            '$inc': {'comments.$.likes': 1},
                            '$addToSet': {'comments.$.user_likes': user_id}
                        }
                    )
                    if user_id in comment.get('user_dislikes', []):
                        mongo.db.stories.update_one(
                            {'comments._id': ObjectId(comment_id)},
                            {
                                '$inc': {'comments.$.dislikes': -1},
                                '$pull': {'comments.$.user_dislikes': user_id}
                            }
                        )
                else:
                    mongo.db.stories.update_one(
                        {'comments._id': ObjectId(comment_id)},
                        {
                            '$inc': {'comments.$.likes': -1},
                            '$pull': {'comments.$.user_likes': user_id}
                        }
                    )
                break

        story = mongo.db.stories.find_one({'comments._id': ObjectId(comment_id)})
        for comment in story['comments']:
            if comment['_id'] == ObjectId(comment_id):
                return jsonify(success=True, likes=comment['likes'], dislikes=comment['dislikes'])


@main.route('/comment/<comment_id>/dislike', methods=['POST'])
@login_required
def dislike_comment(comment_id):
    print(f"Received dislike request for comment ID: {comment_id}")
    story = mongo.db.stories.find_one({'comments._id': ObjectId(comment_id)})
    if story:
        user_id = current_user.id
        for comment in story['comments']:
            if comment['_id'] == ObjectId(comment_id):
                if user_id not in comment.get('user_dislikes', []):
                    mongo.db.stories.update_one(
                        {'comments._id': ObjectId(comment_id)},
                        {
                            '$inc': {'comments.$.dislikes': 1},
                            '$addToSet': {'comments.$.user_dislikes': user_id}
                        }
                    )
                    if user_id in comment.get('user_likes', []):
                        mongo.db.stories.update_one(
                            {'comments._id': ObjectId(comment_id)},
                            {
                                '$inc': {'comments.$.likes': -1},
                                '$pull': {'comments.$.user_likes': user_id}
                            }
                        )
                else:
                    mongo.db.stories.update_one(
                        {'comments._id': ObjectId(comment_id)},
                        {
                            '$inc': {'comments.$.dislikes': -1},
                            '$pull': {'comments.$.user_dislikes': user_id}
                        }
                    )
                break

        story = mongo.db.stories.find_one({'comments._id': ObjectId(comment_id)})
        for comment in story['comments']:
            if comment['_id'] == ObjectId(comment_id):
                return jsonify(success=True, likes=comment['likes'], dislikes=comment['dislikes'])

@main.route('/follow/<user_id>', methods=['POST'])
@login_required
def follow_user(user_id):
    user_to_follow = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    if user_to_follow:
        current_user_id = current_user.id
        if current_user_id not in user_to_follow.get('followers', []):
            mongo.db.users.update_one({'_id': ObjectId(user_id)}, {'$addToSet': {'followers': current_user_id}})
            mongo.db.users.update_one({'_id': ObjectId(current_user_id)}, {'$addToSet': {'following': user_id}})
            flash('You are now following this user!', 'success')
        else:
            flash('You are already following this user!', 'warning')
    else:
        flash('User not found!', 'danger')
    return redirect(url_for('main.user_profile', user_id=user_id))


@main.route('/unfollow/<user_id>', methods=['POST'])
@login_required
def unfollow_user(user_id):
    user_to_unfollow = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    if user_to_unfollow:
        current_user_id = current_user.id
        if current_user_id in user_to_unfollow.get('followers', []):
            mongo.db.users.update_one({'_id': ObjectId(user_id)}, {'$pull': {'followers': current_user_id}})
            mongo.db.users.update_one({'_id': ObjectId(current_user_id)}, {'$pull': {'following': user_id}})
            flash('You have unfollowed this user!', 'success')
        else:
            flash('You are not following this user!', 'warning')
    else:
        flash('User not found!', 'danger')
    return redirect(url_for('main.user_profile', user_id=user_id))


@main.route('/user/<user_id>')
@login_required
def user_profile(user_id):
    user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    if user:
        return render_template('user_profile.html', user=user)
    else:
        flash('User not found!', 'danger')
        return redirect(url_for('main.index'))


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    user = mongo.db.users.find_one({'_id': ObjectId(current_user.id)})
    followers_count = len(user.get('followers', []))
    following_count = len(user.get('following', []))
    stories_count = mongo.db.stories.count_documents({'user_id': current_user.id})

    followers = [mongo.db.users.find_one({'_id': ObjectId(follower_id)}) for follower_id in user.get('followers', [])]
    followings = [mongo.db.users.find_one({'_id': ObjectId(following_id)}) for following_id in
                  user.get('following', [])]

    return render_template('profile.html', user=current_user, followers_count=followers_count,
                           following_count=following_count, stories_count=stories_count, followers=followers,
                           followings=followings)

@main.route('/profiles')
def profiles():
    users = mongo.db.users.find()
    return render_template('profiles.html', users=users)


