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

        self.__channel_id = channel_id
        channel = self.get_service().channels().list(
            id=self.__channel_id,
            part='snippet,statistics'
        ).execute()

        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.subscribers_count = int(channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(channel['items'][0]['statistics']['videoCount'])
        self.view_count = int(channel['items'][0]['statistics']['viewCount'])

    def __str__(self):
        """
        Возвращает описание канала и ссылку на канал
        """
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """
        Возвращает общее количестов подписчиков
        """
        return self.subscribers_count + other.subscribers_count

    def __sub__(self, other):
        """
        Возвращает разницу в количетсве подписчиков
        """
        return self.subscribers_count - other.subscribers_count

    def __gt__(self, other):
        """
        Сравнкние по количеству подписчиков
        """
        return self.subscribers_count > other.subscribers_count

    def __ge__(self, other):
        """
        Сравнкние по количеству подписчиков
        """
        return self.subscribers_count >= other.subscribers_count

    def __lt__(self, other):
        """
        Сравнкние по количеству подписчиков
        """
        return self.subscribers_count < other.subscribers_count

    def __le__(self, other):
        """
        Сравнкние по количеству подписчиков
        """
        return self.subscribers_count <= other.subscribers_count

    def __eq__(self, other):
        """
        Сравнение количества подписчиков
        """
        return self.subscribers_count == other.subscribers_count

    @property
    def channel_id(self):
        return self.__channel_id

    @staticmethod
    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.get_service().channels().list(
            id=self.__channel_id,
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

    def to_json(self, file):
        """
        Cохраняет в файл значения атрибутов экземпляра Channel
        """
        data = {
            "channel_id_": self.__channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriber_count": self.subscribers_count,
            "video_count": self.video_count,
            "view_count": self.view_count
        }
        with open(file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
