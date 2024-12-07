import asyncio
import json
import re
import os
import subprocess
from typing import Optional
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

# Расширенный список языков для поиска транскрипции
LANGUAGES = [
    "ru",
    "en",
    "fr",
    "de",
    "es",
    "it",
    "pt",
    "nl",
    "pl",
    "uk",
    "zh",
    "ja",
    "ko",
    "tr",
]

# Динамическое определение абсолютного пути к файлу cookies
COOKIES_PATH = os.path.join(os.getcwd(), "app", "cookies.txt")

MAX_TOKENS = 2000  # Define the token limit for LLM input
APPROX_TOKEN_LENGTH = (
    4  # Average character length per token (approximation for English text)
)


async def fetch_transcript(url: str) -> Optional[str]:
    """
    Асинхронно получает транскрипцию YouTube видео.
    Пытается найти транскрипцию на любом из поддерживаемых языков.
    Ограничивает выходной текст до 2000 токенов.

    Args:
        url (str): URL YouTube видео

    Returns:
        Optional[str]: Отформатированный текст транскрипции или None в случае ошибки
    """
    try:
        # Извлекаем ID видео из URL
        video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
        if not video_id_match:
            return None
        video_id = video_id_match.group(1)

        # Запускаем получение транскрипции в отдельном потоке через asyncio
        transcript = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: YouTubeTranscriptApi.get_transcript(
                video_id,
                languages=LANGUAGES,
                cookies=COOKIES_PATH,
            ),
        )

        # Форматируем текст
        formatter = TextFormatter()
        formatted_text = formatter.format_transcript(transcript).replace("\n", " ")

        # Урезаем текст, чтобы он соответствовал лимиту токенов
        max_characters = MAX_TOKENS * APPROX_TOKEN_LENGTH
        truncated_text = formatted_text[:max_characters]
        return truncated_text

    except Exception as e:
        print(f"Ошибка при получении транскрипции: {str(e)}")
        return None


def clean_youtube_url(url):
    video_id = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    return f"https://www.youtube.com/watch?v={video_id}"


def get_video_metadata(url):
    """Get video metadata. Вывод в виде словаря"""
    try:
        video_id_match = clean_youtube_url(url)
        result = subprocess.run([
            'yt-dlp',
            '--dump-json',
            '--no-playlist',
            video_id_match
        ], check=True, capture_output=True, text=True)


        metadata = json.loads(result.stdout)
        header_parts = {}

        if title := metadata.get('title'):
            header_parts["title"] = title

        if channel := metadata.get('channel'):
            header_parts["channel"] = channel

        if upload_date := metadata.get('upload_date'):
            header_parts["upload_date"] = upload_date

        if duration := metadata.get('duration_string'):
            header_parts["duration"] = duration

        if views := metadata.get('view_count'):
            header_parts["views"] = views

        if description := metadata.get('description'):
            header_parts["description"] = description

        if tags := metadata.get('tags'):
            header_parts["tags"] = tags

        return header_parts
    except Exception as e:
        raise e
