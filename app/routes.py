from flask import render_template, request, jsonify, Blueprint
from app.work_with_url import fetch_transcript
from app.work_with_gpt import get_summarization

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
    print("Video text: ", video_text)
    summarization = await get_summarization(video_text)
    print("Summarization: ", summarization)

    return jsonify({"summary": summarization})
