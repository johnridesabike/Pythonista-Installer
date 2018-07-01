"""This script downloads releases from GitHub and installs them in Pythonista.

Fork this code and use it to install your own Pythonista apps. Just replace the
APP_NAME and APP_URL variables to match your own app. Users will be able to
easily install your app by copying and pasting this code into the Pythonista
console:
    
```
import requests as r; exec(r.get('https://url.to/this/script').text)
```

Credits:
This code was copied from the installer from https://github.com/shaun-h/PyDoc
"""
import requests
import os
import console
import shutil
import json
import zipfile
from io import BytesIO

# Replace these variables with your own app's details.
APP_NAME = 'WordRoom'
APP_URL = 'https://api.github.com/repos/johnridesabike/WordRoom/releases/latest'


def install():
    try:
        p = os.path.join(os.path.expanduser('~'), 'Documents', APP_NAME)
        if os.path.exists(p):
            op = console.alert(
                'Please Check',
                APP_NAME +
                ' exists on this device. Would you like to override it?',
                hide_cancel_button=True,
                button1='No',
                button2='Yes')
            if op == 2:
                shutil.rmtree(p)
            elif op == 1:
                return
        os.makedirs(p)
        latestReleaseUrl = APP_URL
        console.show_activity('Getting latest version')
        response = requests.get(latestReleaseUrl)
        release = json.loads(response.text)
        console.hide_activity()

        console.show_activity('Installing ' + APP_NAME + ' ' +
                              release['tag_name'])
        request = requests.get(release['zipball_url'])
        file = zipfile.ZipFile(BytesIO(request.content))
        toRemove = file.namelist()[0]
        os.chdir(p)
        file.extractall()
        for filename in os.listdir(toRemove):
            shutil.move(os.path.join(toRemove, filename), filename)
        shutil.rmtree(toRemove)
        file.close()

        f = open('.version', 'w')
        f.write(release['tag_name'].replace('v', ''))
        f.close()
        console.hide_activity()
        console.alert(
            'Installed',
            APP_NAME + ' ' + release['tag_name'] + ' installed.',
            hide_cancel_button=True,
            button1='Ok')
    except requests.exceptions.ConnectionError as e:
        console.alert(
            'Check your internet connection',
            'Unable to check for update.',
            hide_cancel_button=True,
            button1='Ok')
        console.hide_activity()


if __name__ == '__main__':
    install()
