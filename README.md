# Pythonista Installer
This script downloads releases from GitHub and installs them in Pythonista.

Fork this code and use it to install your own Pythonista apps. Just replace the APP_NAME and APP_URL variables to match your own app. Your users will be able to easily install your app by copying and pasting this code into the Pythonista console:
    
```
import requests as r; exec(r.get('https://url.to/installer/script').text)
```

## Credits

This code was forked from the installer from [Shaun Hevey's PyDoc repository](https://github.com/shaun-h/PyDoc)

## To-do

- Add an update script