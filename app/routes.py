from flask import Flask, render_template, request, jsonify, Blueprint
from app.work_with_url import fetch_transcript

api = Blueprint("api", __name__)


@api.route("/")
def index():
    return render_template("index.html")


@api.route("/summarize", methods=["POST"])
async def summarize_video():
    data = request.json
    youtube_url = data.get("url")

    if not youtube_url:
        return jsonify({"error": "You must pass the video URL"}), 400

    video_text = await fetch_transcript(youtube_url)

    return jsonify({"summary": video_text})
