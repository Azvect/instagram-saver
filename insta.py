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
    cookies = input('Enter cookies: ')
    csrftoken = input('Enter csrftoken: ')
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
        time.sleep(1)
        i = i['media']
        # Download images
        if i['media_type'] == 1:
            download(i['image_versions2']['candidates'][0]['url'], 'insta/' + i['code'] + '.jpg')
        # Download videos
        elif i['media_type'] == 2:
            download(i['video_versions'][0]['url'], 'insta/' + i['code'] + '.mp4')
        # Print error if media type is not 1 or 2 (More than 1 image or video)
        else:
            print('Unknown media type')
            print('Media type: ' + str(i['media_type']))
            print('The url is: ' + i['code'])
        # if last item then return max_id
    return data['next_max_id']

# Run exec with returned max_id until max_id is None
max_id = ''
while max_id != None:
    max_id = exec(max_id)
    print('Next max_id: ' + str(max_id))