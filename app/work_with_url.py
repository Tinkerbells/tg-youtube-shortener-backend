from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import re


Global_languages = [
    "ru", "en", "es", "fr", "de", "it", "pt", "zh", "ja", "ko", "ar", "hi",
    "bn", "pa", "jv", "mr", "te", "tr", "th", "vi", "pl", "uk"
]


def get_video_id_from_url(url):
    """Do ID from URL"""

    match = re.search(r'v=([a-zA-Z0-9_-]+)', url)

    if match:
        ID = match.group(1)
        return ID
    else:
        return None


def get_video_summarize(video_id):
    try:

        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=Global_languages)

        formatter = TextFormatter()
        formatted_transcript = formatter.format_transcript(transcript)


        summary = " ".join(formatted_transcript.split())

        return summary

    except Exception as e:
        return f"Error while extracting text: {str(e)}"

