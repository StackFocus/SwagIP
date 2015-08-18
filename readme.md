## SwagIP

A simple way to get your public IP address and other connection related information  

#####Examples of retrieving your public IP address from Linux/Unix CLI:
```
wget -qO - ip.swagger.pro
curl ip.swagger.pro
fetch -qo - ip.swagger.pro
```

#####Example of retrieving your public IP address from PowerShell 3+:
```
Invoke-RestMethod -URI http://ip.swagger.pro
```

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
$ docker run -p 0.0.0.0:80:8080 [image id]
```

### Screenshots
#####Browser Information:
![Browser Information](screenshots/browser.png?raw=true)

#####Wget Commands:
![Wget Commands](screenshots/wget.png?raw=true)

#####Curl Commands:
![Curl Commands](screenshots/curl.png?raw=true)

#####Fetch Commands:
![Fetch Commands](screenshots/fetch.png?raw=true)

#####PowerShell Commands:
![PowerShell Commands](screenshots/powershell.png?raw=true)
