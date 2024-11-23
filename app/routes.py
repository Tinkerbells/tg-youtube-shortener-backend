from flask import Flask, render_template, request, jsonify, Blueprint
from app.work_with_url import get_video_summarize, get_video_id_from_url
api = Blueprint("api", __name__)


@api.route('/')
def index():
    return render_template('index.html')


@api.route('/summarize', methods=['POST'])
def summarize_video():
    data = request.json
    youtube_url = data.get('url')

    if not youtube_url:
        return jsonify({"error": "You must pass the video URL"}), 400

    youtube_id = get_video_id_from_url(youtube_url)
    video_text = get_video_summarize(youtube_id)

    return jsonify({"summary": video_text})
