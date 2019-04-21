import requests,re
from bs4 import BeautifulSoup

''' 
URL of the archive web-page which provides link to 
all mp3 files. It would have been tiring to 
download each video manually. 
In this example, we first crawl the webpage to extract 
all the links and then download mp3 files. 

'''

# specify the URL of the archive here
archive_url = "https://www.soundsmarathi.com/noisy-sounds.html"



def get_video_links():
    # create response object
    r = requests.get(archive_url)

    # create beautiful-soup object
    soup = BeautifulSoup(r.content, 'html.parser')
	
	# filter the link sending with .mp3 and save url into linkss
    linkss = [a['href'] for a in soup.find_all('a', attrs={'href':re.compile(".mp3$")})]
    


    return linkss


def download_video_series(linkss):
    for link in linkss:

        '''iterate through all links in video_links 
        and download them one by one'''

        # obtain filename by splitting url and getting
        # last string
        file_name = link.split('/')[-1]

        print("Downloading file:%s" % file_name)

        # create response object
        r = requests.get(link, stream=True)

        # download started
        with open('H:\\NS production\\' + file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

        print("%s downloaded!\n" % file_name)

    print("All videos downloaded!")
    return


if __name__ == "__main__":
    # getting all video links
    video_links = get_video_links()

    # download all videos
    download_video_series(video_links)

