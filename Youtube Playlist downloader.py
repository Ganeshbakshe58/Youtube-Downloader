from pytube import Playlist, query, YouTube


def downloadVideo(link):
    youtube = YouTube(link)
    print(f".....Downloading {youtube.title}")
    youtube.streams.get_highest_resolution().download(
        f"./{playlist.title}", f"{number}. {youtube.title}")
    print(f"{youtube.title} successfullly downloaded")


playlist_link = input('Enter the url of the playlist: ')
playlist = Playlist(playlist_link)
print(f'Downloading: {playlist.title}')
print('Number of videos in playlist: %s' % len(playlist.video_urls))


number = 1
for video in playlist.video_urls:
    try:
        downloadVideo(video)
        number += 1
    except:
        number += 1
        continue

print("Download Successfully Complete")
