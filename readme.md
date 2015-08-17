## SwagIP

A simple way to get your public IP address and other connection related information  

#####Examples of retrieving your public IP address from Linux/Unix CLI:
wget -qO - ip.swagger.pro

curl ip.swagger.pro

fetch -qo - ip.swagger.pro


#####Example of retrieving your public IP address from PowerShell 3+:
Invoke-RestMethod -URI http://ip.swagger.pro

### Installing
```
$ pip install -r requirements.txt
$ python app.py
```
### Tests
```
$ py.test tests/
```

### Docker!
We use docker to scale this application.
```
$ docker build .
```

### Screenshots
#####Browser Information:
<img src='screenshots/1-browser.png' alt='Browser Information' />

#####Wget Commands:
<img src='screenshots/2-wget.png' alt='Wget Commands' />

#####Curl Commands:
<img src='screenshots/3-curl.png' alt='Curl Commands' />

#####Fetch Commands:
<img src='screenshots/4-fetch.png' alt='Fetch Commands' />

#####PowerShell Commands:
<img src='screenshots/5-powershell.png' alt='PowerShell Commands' />
