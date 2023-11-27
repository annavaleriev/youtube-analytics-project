import os

from googleapiclient.discovery import build


class YouTubeMixin:
    @classmethod
    def get_service(cls):
        """
        Возвращающий объект для работы с YouTube API
        """
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube
