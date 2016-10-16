# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<SCRIPT
#!/bin/bash
apt-get update
apt-get install -y python python-pip python-dev python-virtualenv
mkdir -p /opt/swagip/logs
virtualenv /opt/swagip/env
source /opt/swagip/env/bin/activate
cd /opt/swagip/git
pip install -r requirements.txt
SCRIPT

Vagrant.configure(2) do |config|
  config.vm.box = "boxcutter/ubuntu1604"
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.synced_folder "./", "/opt/swagip/git"
  config.vm.provision "shell", inline: $script
  config.vm.provision :shell, :inline => "cd /opt/swagip/git && /opt/swagip/env/bin/uwsgi --ini=/opt/swagip/git/wsgi.ini &", run: "always"
end
