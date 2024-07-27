"""
class163/music.py
Version: 0.2.0
Author: CooooldWind_
E-Mail: 3091868003@qq.com
Copyright @CooooldWind_ / Following GNU_AGPLV3+ License
"""

import time
from netease_encode_api import EncodeSession
from urllib.parse import urlparse, parse_qs


class Music:
    def __init__(self, id: int | str) -> None:
        #  最刚开始时要有的: 解码会话, ID
        self.id = str(id)  #  ID (如果检测到是URL会自动转格式)
        if self.id.find("music.163.com") != -1:
            self.id = url_to_id(self.id)
        self.encode_session = EncodeSession()  #  解码会话
        #  详细信息
        self.__detail_encode_data = {
            "c": str([{"id": self.id}]),
        }  #  解码时的encode_data
        self.title: str = None  #  标题
        self.subtitle: str = None  #  副标题
        self.album: str = None  #  专辑
        self.artist: list[str] = []  #  歌手
        self.publish_time = None  #  发布时间（年月日）
        self.trans_title: str = None  #  标题译文
        self.trans_album: str = None  #  专辑译文
        self.trans_artist: dict = {}  #  歌手译文（需要用歌手原文作为键值）
        self.detail_info_raw: dict = {}  #  解码类返回的数据
        self.detail_info_sorted: dict = {}  #  整理后的数据
        self.cover_url: str = None
        #  歌词相关
        self.__lyric_encode_data = {
            "id": self.id,
            "lv": -1,
            "tv": -1,
        }  #  解码时的encode_data
        self.lyric: str = None  #  歌词原文
        self.trans_lyric: str = None  #  歌词翻译
        self.trans_uploader: str = None  #  翻译歌词的网易云用户昵称
        self.trans_lyric_uptime = None  #  翻译的发布时间（年月日）
        self.lyric_info_raw: dict = {}  #  解码类返回的数据
        self.lyric_info_sorted: dict = {}  #  整理后的数据
        #  音乐文件相关
        """
        id表示歌曲的id号, 
        level是音乐品质, 
        标准为standard, 
        较高音质为higher, 
        极高音质exhigh, 
        无损音质关键词为lossless。
        """
        self.__file_encode_data = {
            "ids": str([self.id]),
            "level": None,  #  standard/higher/exhigh/lossless
            "encodeType": None,  #  如果是lossless就用aac, 其他是mp3
            "csrf_token": "",
        }  #  解码时的encode_data
        self.file_info_raw: dict = {}
        self.file_info_sorted: dict = {}

    def get(self, type: str = "d", session: EncodeSession = None) -> dict:
        if session is None:
            session = self.encode_session
        if type == "d":
            return self.get_detail(session=session)  #  详细信息
        elif type == "l":
            return self.get_lyric(session=session)  #  歌词

    def get_file(self, session: EncodeSession = None, level: str = "standard") -> dict:
        if session is None:
            session = self.encode_session
        self.file_info_raw = session.get_response(
            url="https://music.163.com/weapi/song/enhance/player/url/v1",
            encode_data=self.__file_encode_data,
        )
        return self.file_info_raw

    def get_lyric(self, session: EncodeSession = None) -> dict:
        if session is None:
            session = self.encode_session
        self.lyric_info_raw = session.get_response(
            url="https://music.163.com/weapi/song/lyric",
            encode_data=self.__lyric_encode_data,
        )
        #
        self.lyric = self.lyric_info_raw["lrc"]["lyric"]
        self.trans_lyric = self.lyric_info_raw["tlyric"]["lyric"]
        self.trans_uploader = self.lyric_info_raw["transUser"]["nickname"]
        #
        self.trans_lyric_uptime = time.localtime(
            int(self.lyric_info_raw["transUser"]["uptime"]) / 1000
        )
        self.trans_lyric_uptime = self.trans_lyric_uptime[0:5]
        #
        self.lyric_info_sorted = {
            "lyric": self.lyric,
            "trans_lyric": self.trans_lyric,
            "trans_uploader": self.trans_uploader,
            "trans_lyric_uptime": self.trans_lyric_uptime,
        }
        #
        return self.lyric_info_sorted

    def get_detail(self, session: EncodeSession = None) -> dict:
        if session is None:
            session = self.encode_session
        self.detail_info_raw = session.get_response(
            url="https://music.163.com/weapi/v3/song/detail",
            encode_data=self.__detail_encode_data,
        )["songs"][0]
        #
        self.title = self.detail_info_raw["name"]
        self.album = self.detail_info_raw["al"]["name"]
        #
        self.publish_time = time.localtime(
            int(self.detail_info_raw["publishTime"]) / 1000
        )
        self.publish_time = self.publish_time[0:3]
        #
        if "alia" in self.detail_info_raw:
            if len(self.detail_info_raw["alia"]) > 0:
                self.subtitle = self.detail_info_raw["alia"][0]
        #
        if "tns" in self.detail_info_raw:
            if len(self.detail_info_raw["tns"]) > 0:
                self.trans_title = self.detail_info_raw["tns"][0]
        #
        if "tns" in self.detail_info_raw["al"]:
            if len(self.detail_info_raw["al"]["tns"]) > 0:
                self.trans_album = self.detail_info_raw["al"]["tns"][0]
        #
        for i in self.detail_info_raw["ar"]:
            self.artist.append(i["name"])
            if "tns" in i:
                if len(i["tns"]) > 0:
                    self.trans_artist.update({str(i["name"]): i["tns"]})
        self.cover_url = self.detail_info_raw["al"]["picUrl"]
        #
        self.detail_info_sorted.update(
            {
                "id": self.id,
                "title": self.title,
                "album": self.album,
                "artist": self.artist,
                "publish_time": self.publish_time,
                "subtitle": self.subtitle,
                "trans_title": self.trans_title,
                "trans_album": self.trans_album,
                "trans_artist": self.trans_artist,
                "cover_url": self.cover_url,
            }
        )
        return self.detail_info_sorted


def url_to_id(url: str) -> int:
    try:
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        song_id = query_params.get("id", [None])[0]
        if song_id is not None:
            return int(song_id)
        else:
            raise ValueError("URL 中未找到 'id' 参数")
    except (ValueError, TypeError) as e:
        raise e
