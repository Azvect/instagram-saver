import requests
import json
import os
import time

# Function to download url using requests
def download(url, file_name):
    with open(file_name, "wb") as file:
        response = requests.get(url)
        file.write(response.content)

def exec(max_id):
    url = 'https://www.instagram.com/api/v1/feed/saved/posts/?max_id=' + max_id
    # Ask for cookies and csrftoken
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'x-ig-app-id': '936619743392459',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': csrftoken,
        'cookie': cookies
    }
    r = requests.get(url, headers=headers)
    data = json.loads(r.text)
    # Create directory
    if not os.path.exists('insta'):
        os.makedirs('insta')
    for i in data['items']:
        # Check if i['media']['code'] is already downloaded. If so then skip
        if os.path.exists('insta/' + i['media']['code'] + '.jpg') or os.path.exists('insta/' + i['media']['code'] + '.mp4'):
            continue
        time.sleep(1)
        i = i['media']
        # Download images
        if i['media_type'] == 1:
            download(i['image_versions2']['candidates'][0]['url'], 'insta/' + i['code'] + '.jpg')
        # Download videos
        elif i['media_type'] == 2:
            download(i['video_versions'][0]['url'], 'insta/' + i['code'] + '.mp4')
        # Download carousel
        elif i['media_type'] == 8:
            mainname = i['code']
            # Create directory for carousel with code as name
            if not os.path.exists('insta/' + mainname):
                os.makedirs('insta/' + mainname)
            for j in i['carousel_media']:
                # Download images with incrementing name
                if j['media_type'] == 1:
                    download(j['image_versions2']['candidates'][0]['url'], 'insta/' + mainname + '/' + str(j['id']) + '.jpg')
                # Download videos with incrementing name
                elif j['media_type'] == 2:
                    download(j['video_versions'][0]['url'], 'insta/' + mainname + '/' + str(j['id']) + '.mp4')
        # if last item then return max_id
    # Check if next_max_id is None
    if 'next_max_id' not in data:
        return None
    else:
        return data['next_max_id']

# Ask for cookies
cookies = input('Enter you cookie: ')
# Get csrftoken from cookies
csrfstart = cookies.find('csrftoken=') + 10
csrfend = cookies[csrfstart:].find(';')
csrftoken = cookies[csrfstart:csrfstart + csrfend]

# Run exec with returned max_id until max_id is None
max_id = ''
while max_id != None:
    max_id = exec(max_id)
    print('Next max_id: ' + str(max_id))
