import datetime

import isodate

from src.mixins import YouTubeMixin


class PlayList(YouTubeMixin):
    def __init__(self, playlist_id):
        self.__playList_id = playlist_id
        self.youtube = self.get_service()
        playlists = self.youtube.playlists().list(
            id=self.__playList_id,
            part='snippet',
        ).execute()
        self.title: str = playlists['items'][0]['snippet']['title']
        self.url: str = f"https://www.youtube.com/playlist?list={self.__playList_id}"

    def get_videos_response(self):
        """
        Метод, который возвращает  информацию с данными видео для дальнейшем работы: кол-во просмотров,
        лайков, дизлайковюб, комментариев, продолжительность.
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
        return video_response

    @property
    def total_duration(self) -> datetime:
        """
        Метод, который возвращает объект класса `datetime.timedelta` с суммарной длительность плейлиста
        """
        video_response = self.get_videos_response()

        total_duration = datetime.timedelta()
        for video in video_response['items']:
            iso_8601_duration: list = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration

    def show_best_video(self) -> str:
        """
        Метод, который возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)
        """
        video_response = self.get_videos_response()
        best_video = None
        max_likes = 0
        for video in video_response['items']:
            like_count = int(video['statistics']['likeCount'])
            if like_count > max_likes:
                max_likes = like_count
                best_video = video['id']
        if best_video:
            return f'https://youtu.be/{best_video}'
