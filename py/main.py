import re
import requests
import webbrowser

chrome_path = '/usr/bin/google-chrome %s --incognito'
clientId = {'client_id': 'e5abff372b091b82ea72'}
deviceCodeRequest = requests.post('https://github.com/login/device/code', data = clientId)
deviceCode = re.search('device_code=(.*)&expires_in', deviceCodeRequest.text).group(1)
userCode = re.search('user_code=(.*)&verification_uri', deviceCodeRequest.text).group(1)
print('You\'re user code is: ' + userCode + ". Please enter it in the launced webpage.")
webbrowser.get(chrome_path).open('https://github.com/login/device')

userInput = input("Press ENTER when you are done")

body = {'client_id': 'e5abff372b091b82ea72', 'device_code': deviceCode, 'grant_type': 'urn:ietf:params:oauth:grant-type:device_code'}
tokenRequest = requests.post('https://github.com/login/oauth/access_token', data = body)
token = re.search('access_token=(.*)&scope=&token_type=bearer', tokenRequest.text).group(1)

authHeader = {"Authorization": "token " + token}
userDataRequest = requests.get('https://api.github.com/user', headers = authHeader)
fullName = re.search('\"name\":\"(.*)\",\"company', userDataRequest.text).group(1)
print('Aren\'t you ' + fullName + '? :)')
