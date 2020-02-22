from threading import Thread

from pytube import YouTube

from enums import Resolution, Type
from exceptions import StreamNotFoundException


class YouTubeDownloader(Thread):
    def __init__(self, link: str, resolution: Resolution, type: Type, destination):
        Thread.__init__(self)
        self.name = link
        self.link = link
        self.preferred_resolution = resolution
        self.type = type
        self.output_path = destination

    def __start_download(self):
        print(f"Analysing {self.link}")
        v = YouTube(self.link, on_complete_callback=self.__download_complete)
        # Check if it has a stream like user wants
        stream = v.streams.filter(mime_type=str(self.type),
                                  resolution=str(self.preferred_resolution),
                                  progressive=True).first()
        if not stream:
            # since it doesn't have a stream with the desired configuration, let's
            # download the best available. Search for the nearest match
            stream = v.streams.filter(mime_type=str(self.type), progressive=True).order_by("resolution").desc().first()
            if not stream:
                raise StreamNotFoundException(self.link)

        file_ = stream.title.title().replace(" ", "_") + "_" + stream.resolution
        print(f"Downloading {file_} from {self.link}")
        stream.download(filename=file_, output_path=self.output_path)

    def __download_complete(self, stream, file_path):
        print(f"Download complete for {stream} in {file_path}")

    def run(self):
        self.__start_download()
