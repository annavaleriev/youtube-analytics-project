from src.channel import Channel


class Video:
    def __init__(self, video_id):
        self.__video_id = video_id
        self.youtube = Channel.get_service()
        video_response = self.youtube.videos().list(
            id=self.__video_id,
            part='snippet,statistics,contentDetails,topicDetails',
        ).execute()

        self.video_title: str = video_response['items'][0]['snippet']['title']
        self.video_url: str = f"https://www.youtube.com/watch?v={self.__video_id}"
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f"{self.video_title}"


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.__playlist_id = playlist_id




# test_video = Video("92MOI1mMVfg")
# print(test_video.video_title)
# print(test_video.video_url)
# print(test_video.view_count)
# # print(test_video.like_count)
# # test_PLVideo = PLVideo("MqWvAf7k1Qk&list", "PL-0SBsH5CZOxSsJA8aUlqLVEtYtqchInF&index")
# test_PLVideo = PLVideo("4fObz_qw9u4", "PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC")
# print(test_PLVideo.video_url)
# print(test_PLVideo.video_title)
# # print(str(test_PLVideo))
# print(test_PLVideo.view_count)
# print(test_PLVideo.like_count)



    # def __str__(self):
    #     re
    #     # assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'
        # assert str(video2) == 'MoscowPython Meetup 78 - вступление'


        # super().__init__(name, price, quantity)
        # self.__number_of_sim: int = number_of_sim



    #     channel = self.get_service().channels().list(
    #         id=self.__channel_id,
    #         part='snippet,statistics'
    #     ).execute()
    #

    # video_title: str = video_response['items'][0]['snippet']['title']
    # view_count: int = video_response['items'][0]['statistics']['viewCount']
    # like_count: int = video_response['items'][0]['statistics']['likeCount']
    # comment_count: int = video_response['items'][0]['statistics']['commentCount']
    #
    # self.title = channel['items'][0]['snippet']['title']
    # self.description = channel['items'][0]['snippet']['description']
    # self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
    # self.subscribers_count = int(channel['items'][0]['statistics']['subscriberCount'])
    # self.video_count = int(channel['items'][0]['statistics']['videoCount'])
    # self.view_count = int(channel['items'][0]['statistics']['viewCount'])
    #
    # # - id видео
    # # - название видео
    # # - ссылка на видео
    # # - количество просмотров
    # # - количество лайков
    #
    # '''
    # получить статистику видео по его id
    # получить id можно из адреса видео
    # https://www.youtube.com/watch?v=gaoc9MPZ4bw или https://youtu.be/gaoc9MPZ4bw
    # '''
    # video_id = 'gaoc9MPZ4bw'
    # video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
    #                                        id=video_id
    #                                        ).execute()
    # # printj(video_response)
    # video_title: str = video_response['items'][0]['snippet']['title']
    # view_count: int = video_response['items'][0]['statistics']['viewCount']
    # like_count: int = video_response['items'][0]['statistics']['likeCount']
    # comment_count: int = video_response['items'][0]['statistics']['commentCount']
