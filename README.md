# Instagram Saver
This is a Python script that allows you to download your saved posts on Instagram. The script uses the **`requests`** library to make API calls to Instagram and the **`json`** library to process the response data.

## Requirements
* Python 3.x
* requests


## Usage
1. Clone the repository and navigate to the directory where the script is located
2. Install the required library by running **`pip install requests`**
3. Run the script with **`python insta.py`**
4. Enter your cookies and csrftoken when prompted
5. The saved posts will be downloaded to a directory named 'insta'

## How to get cookies and csrftoken from Instagram using a browser
1. Open Instagram in a browser and log in to your account.
2. Right-click anywhere on the page and select "Inspect" or "Inspect Element"
3. Go to the "Application" or "Storage" tab
4. Under "Cookies", find "www.instagram.com" and click on it
5. Look for the "cookie" key-value pair and copy the entire value (this is your cookies)
6. Find the "csrftoken" key-value pair and copy the value (this is your csrftoken)
7. Use the copied values as input when prompted in the script.

**Note: Cookies and csrftoken are sensitive information and should not be shared with anyone.**


## Note
* The script is set to wait for 1 second between each download to avoid overloading the Instagram servers. You can adjust this as needed by changing the value of the sleep() function.
* The script will continue to download saved posts until there are no more posts to download, indicated by a returned **`next_max_id`** of **`None`**.
