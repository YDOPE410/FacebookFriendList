# FacebookFriendList

Script output list of friends from Facebook. Based on Selenium.

*Opens Facebook in chrome tab
*Login into account
*Getting friend list
*Print in console friends names and profile links
*Close chrome tab

#Getting started:
Clone this repository to your machine.
```
$ git clone https://github.com/YDOPE410/FacebookFriendList.git
```
## Requirements

### Python
If it not exists install it. Download it from official site: https://www.python.org/
Or update it if yours python version less than 3.7.

### Install additional modules
Application use selenium module to work with the browser. 
```bash
$ pip install -r requirements.txt 
``` 
### Install additional software
*The program uses a Google Chrome browser. All actions happen in this browser. If it not exists install it. Download it from official site: https://www.google.ru/chrome/
*Chrome web driver binary. Download it from official site: http://chromedriver.chromium.org/downloads

### Modify the configuration file
Change data in "config_default.json".
*"login": facebook account login
*"password": facebook account password
*"path_to_driver": path to used driver for web-browser
*"path_to_save_logs": path where save logs
*"site": url web-site to open

### Running
To run the application use the command:
```bash
python3.7 launcher.py
```
