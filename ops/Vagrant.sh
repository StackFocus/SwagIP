#!/bin/bash
export DEBIAN_FRONTEND=noninteractive

echo 'Updating the aptitude repository...'
apt-get -y update > /dev/null

packages=('python' 'python-pip' 'python-dev')

for package in "${packages[@]}"
do
    if dpkg --get-selections | grep -q "^$package[[:space:]]*install$" >/dev/null
    then
        echo "Skipping the installation of $package"
    else
        echo "Installing $package..."
        apt-get install -y $package > /dev/null
    fi
done

echo 'Checking the python version...'
if [ $(python -V 2>&1 | grep -c "2.7") -eq 0 ]
then
    >&2 echo 'Please ensure that python 2.7 is installed and is the default python version'
    exit 1
fi

echo 'Creating the /opt/swagip/logs directory'
mkdir /opt/swagip/logs

if ! [ -d '/opt/swagip/env' ]
then
    echo 'Installing the virtual environment...'
    pip install virtualenv > /dev/null
    virtualenv /opt/swagip/env > /dev/null
    source /opt/swagip/env/bin/activate
else
    >&2 echo '/opt/swagip/env already exists. Please make sure it is removed before rerunning the script'
    exit 1
fi

cd /opt/swagip/git
echo 'Installing the Python packages required in the virtualenv...'
pip install -r requirements.txt > /dev/null
deactivate

unset DEBIAN_FRONTEND

echo 'The installation has completed!'
