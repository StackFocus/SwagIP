# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "puphpet/ubuntu1404-x64"
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.synced_folder "./", "/opt/swagip/git"
  config.vm.provision "shell", path: "ops/Vagrant.sh"
  config.vm.provision :shell, :inline => "cd /opt/swagip/git && /opt/swagip/env/bin/uwsgi --ini=/opt/swagip/git/wsgi.ini &", run: "always"
end
