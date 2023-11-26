from datetime import datetime

import isodate
import datetime

from src.channel import Channel


class PlayList:
    def __init__(self, playlist_id):
        self.__playList_id = playlist_id
        self.youtube = Channel.get_service()
        playlists = self.youtube.playlists().list(
            channelId=self.__playList_id,
            part='contentDetails,snippet',
        ).execute()

        self.title: str = playlists['items'][0]['snippet']['title']
        self.url: str = f"https://www.youtube.com/watch?v={self.__playList_id}"

    def total_duration(self) -> datetime:
        """
        Метод, который возвращает объект класса `datetime.timedelta` с суммарной длительность плейлиста
        """

        playlist_videos = self.youtube.playlistItems().list(
            playlistId=self.__playList_id,
            part='contentDetails',
            maxResults=50,
        ).execute()

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = self.youtube.videos().list(
            part='contentDetails,statistics',
            id=','.join(video_ids)
        ).execute()

        total_duration = datetime.timedelta()
        for video in video_response['items']:
            iso_8601_duration: list = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration

    def show_best_video(self):
        """
        Метод, который возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)
        """

    pass
