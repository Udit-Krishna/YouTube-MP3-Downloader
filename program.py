import youtube_dl
import json

from youtube_search import YoutubeSearch


def read_settings():
    with open('config.json','r') as f:
        settings = json.load(f)
        return settings["save_location"]


def choose_video():    
    while True:
        try:
            search = input("\nEnter video to download (0 to quit): ")
            if search == '0':
                return 0
            elif search.find('youtu.be/') != -1 or search.find('youtube.com/') != -1:
                return search

            results = YoutubeSearch(search, max_results=10).to_dict()
            l = []

            for a in range(10):
                print(a+1,'. ',results[a]['title'],'\nby ',results[a]['channel'],'\t',results[a]['duration'],'  ',results[a]['views'])
                l.append([a+1,results[a]['id'],results[a]['title']])

            i = int(input('\nChoose a video: '))

            return l[i-1][1]
        
        except:
            print('No results from the search term. Trying using different terms')

def download_video(save_location,id):
    yt_dl_options = {
        'format' : 'bestaudio/best',
        'outtmpl' : f'{save_location}/%(title)s.mp3',
        'extractaudio': True,
        'audioformat':'mp3'
    }

    with youtube_dl.YoutubeDL(yt_dl_options) as ydl:
        ydl.download([id])

    print('The audio has been downloaded and saved in',save_location)


if __name__ == "__main__":
    save_location = read_settings()
    while True:
        vid_id =choose_video()
        if vid_id == 0:
            break
        download_video(save_location, vid_id)
       
