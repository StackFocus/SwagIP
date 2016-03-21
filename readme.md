## SwagIP [![Build Status](https://travis-ci.org/thatarchguy/SwagIP.svg)](https://travis-ci.org/thatarchguy/SwagIP) ![Python](https://img.shields.io/badge/python-2.7-blue.svg) ![Flask](http://flask.pocoo.org/static/badges/made-with-flask-s.png)



A simple way to get your public IP address and other connection related information  

#####Examples of retrieving your public IP address from Linux/Unix CLI:
```
wget -qO - ip.swagger.pro
curl ip.swagger.pro
fetch -qo - ip.swagger.pro
```

#####Example of retrieving your public IP address from PowerShell 3+:
```
Invoke-RestMethod http://ip.swagger.pro
```

### Authors
- [Kevin Law](https://github.com/thatarchguy)
- [Matt Prahl](https://github.com/PrahlM93)

### Installation
```
$ pip install -r requirements.txt
$ python app.py
```
### Testing
```
$ py.test tests/
```

### Docker
Docker is used to scale the application
```
$ docker build -t swagip .
$ docker run -p 0.0.0.0:80:8080 swagip
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
