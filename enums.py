from enum import Enum


class Resolution(Enum):
    RES_NONE = 0
    RES_144P = 1
    RES_240P = 2
    RES_360P = 3
    RES_480P = 4
    RES_720P = 5
    RES_1080P = 6
    RES_2160P = 7

    def __str__(self):
        s = self.name[4:].capitalize()
        return s

    @staticmethod
    def get_from_string(res: str):
        for r in Resolution:
            if res.capitalize() in str(r):
                return r
        else:
            print(f"Resolution {res} not recognized")


class Type(Enum):
    AUDIO_MP4 = 0
    AUDIO_WEBM = 1
    VIDEO_MP4 = 10
    VIDEO_WEBM = 11

    def get_mime_type(self) -> str:
        s = self.name.replace("_", "/").lower()
        return s

    def __str__(self):
        s = self.name.replace("_", "/").lower()
        return s
        # return 'my custom str! {0}'.format(self.value)

    @staticmethod
    def get_from_string(type):
        for t in Type:
            if type.lower() == str(t):
                return t
        else:
            print(f"Type {type} not recognized")


class CODECS(Enum):
    pass
    # vcodec="vp9"
    # vcodec="avc1.42001E"
    # vcodec="avc1.64001F"
    # vcodec="avc1.640028"
    # vcodec="avc1.4d401f"
    # vcodec="avc1.4d401e"
    # vcodec="avc1.4d4015"
    # vcodec="avc1.4d400c"
    # vcodec="avc1.4d400b"
    #
    # acodec="mp4a.40.2"
    # acodec="opus"
    # acodec="mp4a.40.5"
