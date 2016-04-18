import fabric

def start():
  # vagrant up
  # vagrant ssh
  # source .server/venv/bin/activate
  pass


def install():
  # vagrant box add ubuntu/trusty64
  # vagrant ssh

  install_frontend()
  install_backend()
  install_mongodb()




def install_backend():
  # sudo apt-get update
  # sudo apt-get -y install python-pip
  # sudo pip install virtualenv
  # sudo apt-get install build-essential
  # sudo apt-get install libffi-dev
  # sudo apt-get install python-devel
  # pip install -r ./requirements.txt
  pass





def install_frontend():
  # Install Nodejs
  # curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash -
  # sudo apt-get install -y nodejs
  #
  # Install global deps
  # sudo npm install npm -g
  # sudo npm install webpack -g
  #
  # Install deps
  # cd ./client
  # npm install
  pass

def install_mongodb():
  # sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
  # echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
  # sudo apt-get update
  # sudo apt-get install -y mongodb-org=3.2.5 mongodb-org-server=3.2.5 mongodb-org-shell=3.2.5 mongodb-org-mongos=3.2.5 mongodb-org-tools=3.2.5
  # echo "mongodb-org hold" | sudo dpkg --set-selections
  # echo "mongodb-org-server hold" | sudo dpkg --set-selections
  # echo "mongodb-org-shell hold" | sudo dpkg --set-selections
  # echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
  # echo "mongodb-org-tools hold" | sudo dpkg --set-selections
  pass

