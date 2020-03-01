import os
import sys

from enums import Resolution, Type
from exceptions import StreamNotFoundException
from ytdownloader import YouTubeDownloader


def print_help():
    print()
    print()
    print("YouTube Downloader")
    print("Description:")
    print("  YouTube Downloader is a python application to download videos from YouTube")
    print("Usage:")
    print("  python main.py [-o output_folder] [-r preferred resolution] [-t download mime type] LINK1 LINK2 ...")
    print("  ")
    print("  -h -> prints this help")
    print("  -o, --output -> The output folder where you want to save your downloads. The default value is the folder ")
    print("                  my_downloaded_videos that will be created in the application folder")
    print("  -r, --res, --resolution -> The preferred resolution of the video. It is only possible to download\n"
          "                             streams with audio integrated and sometimes the desired resolution doesn't \n"
          "                             have this possibility, so it will be downloaded the best quality available\n"
          "                             with integrated audio. Possible values are:")
    for r in Resolution:
        print(f"        - {r}")
    print("  -t, --type -> The type of stream to download. Possible values are:")
    for t in Type:
        print(f"        - {t}")
    print("  LINK1 LINK2 ... -> The videos' links to download.")
    print("  ")


def parse_args(args: list):
    output = os.path.join(".", "my_downloaded_videos")
    res = Resolution.RES_480P
    type_ = Type.VIDEO_MP4
    links = list()

    i = 1
    while i < len(sys.argv):
        if sys.argv[i] in ["-h", "--help", "/h"]:
            print_help()
            exit(0)
        elif sys.argv[i] in ["-r", "--res", "--resolution"]:
            i += 1
            res = Resolution.get_from_string(sys.argv[i])
        elif sys.argv[i] in ["-t", "--type"]:
            i += 1
            type_ = Type.get_from_string(sys.argv[i])
        elif sys.argv[i].startswith("https://www.youtube.com"):
            links.append(sys.argv[i])

        i += 1

    return output, res, type_, links


def main():
    if len(sys.argv) == 1:
        print("You must enter at least one valid link to download from.")
        print_help()
        sys.exit(-1)

    output, res, type_, links = parse_args(sys.argv)
    if not links:
        print("You must enter at least one valid link to download from.")
        print_help()
        sys.exit(-2)

    if not os.path.exists(output):
        os.mkdir(output)

    for link in links:
        ytd = YouTubeDownloader(link, resolution=res, type=type_, destination=output)
        try:
            ytd.start()
        except StreamNotFoundException as snfe:
            print(snfe)


if __name__ == "__main__":
    main()
    sys.exit(0)
