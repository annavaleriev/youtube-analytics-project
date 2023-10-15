import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """
            Экземпляр инициализируется id канала.
            Дальше все данные будут подтягиваться по API.
        """

        self.channel_id = channel_id
        channel = self.get_service().channels().list(
            id=self.channel_id,
            part='snippet,statistics'
        ).execute()

        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = channel['items'][0]['snippet']['medium']['url']
        self.subscribers_count = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.view_count = channel['items'][0]['statistics']['viewCount']


    @staticmethod
    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.get_service().channels().list(
            id=self.channel_id,
            part='snippet,statistics'
        ).execute()
        self.printj(channel)

    @classmethod
    def get_service(cls):
        """
        Возвращающий объект для работы с YouTube API
        """
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube




