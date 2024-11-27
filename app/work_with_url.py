import asyncio
import re
from typing import Optional
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

# Расширенный список языков для поиска транскрипции
LANGUAGES = [
    'ru', 'en', 'fr', 'de', 'es', 'it', 'pt',
    'nl', 'pl', 'uk', 'zh', 'ja', 'ko', 'tr'
]


async def fetch_transcript(url: str) -> Optional[str]:
    """
    Асинхронно получает транскрипцию YouTube видео.
    Пытается найти транскрипцию на любом из поддерживаемых языков.

    Args:
        url (str): URL YouTube видео

    Returns:
        Optional[str]: Отформатированный текст транскрипции или None в случае ошибки
    """
    try:
        # Извлекаем ID видео из URL
        video_id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url)
        if not video_id_match:
            return None
        video_id = video_id_match.group(1)

        # Запускаем получение транскрипции в отдельном потоке через asyncio
        transcript = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: YouTubeTranscriptApi.get_transcript(video_id, languages=LANGUAGES)
        )

        # Форматируем текст
        formatter = TextFormatter()
        formatted_text = formatter.format_transcript(transcript).replace('\n', ' ')
        return formatted_text

    except Exception as e:
        print(f"Ошибка при получении транскрипции: {str(e)}")
        return None
