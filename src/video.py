from src.mixins import YouTubeMixin


class Video(YouTubeMixin):
    def __init__(self, video_id):
        self.__video_id = video_id
        self.youtube = self.get_service()
        video_response = self.youtube.videos().list(
            id=self.__video_id,
            part='snippet,statistics,contentDetails,topicDetails',
        ).execute()
        try:
            self.title: str = video_response['items'][0]['snippet']['title']
            self.video_url: str = f"https://youtu.be/{self.__video_id}"
            self.view_count: int = int(video_response['items'][0]['statistics']['viewCount'])
            self.like_count: int = int(video_response['items'][0]['statistics']['likeCount'])
        except IndexError:
            self.title = None
            self.video_url = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        return f"{self.title}"


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.__playlist_id = playlist_id
