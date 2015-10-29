#!/bin/bash

PROJECT_NAME=$1

PROJECT_DIR=/vagrant
VIRTUALENV_DIR=/home/vagrant/.virtualenvs/$PROJECT_NAME

PYTHON=$VIRTUALENV_DIR/bin/python
PIP=$VIRTUALENV_DIR/bin/pip


# Create database
su - vagrant -c "createdb $PROJECT_NAME"


# Virtualenv setup for project
su - vagrant -c "pyvenv $VIRTUALENV_DIR"
# Replace previous line with this if you are using Python 2
# su - vagrant -c "/usr/local/bin/virtualenv $VIRTUALENV_DIR"

su - vagrant -c "echo $PROJECT_DIR > $VIRTUALENV_DIR/.project"


# Install PIP requirements
su - vagrant -c "$PIP install -r $PROJECT_DIR/requirements/dev.txt"


# Set execute permissions on manage.py as they get lost if we build from a zip file
chmod a+x $PROJECT_DIR/manage.py


# Run syncdb/migrate/update_index
su - vagrant -c "$PYTHON $PROJECT_DIR/manage.py migrate --noinput && \
                 $PYTHON $PROJECT_DIR/manage.py update_index"

# Load Fixtures
su - vagrant -c "$PYTHON $PROJECT_DIR/manage.py load_initial_data"

# Install NodeJS and Bower
apt-get install python-software-properties
add-apt-repository ppa:chris-lea/node.js
apt-get -y update
apt-get install -y nodejs
npm install -g bower

# Add a couple of aliases to manage.py into .bashrc
cat << EOF >> /home/vagrant/.bashrc
export PYTHONPATH=$PROJECT_DIR
export DJANGO_SETTINGS_MODULE=$PROJECT_NAME.settings.dev

alias dj="django-admin"
alias djrun="dj runserver 0.0.0.0:8000"
alias djcelery="celery -A $PROJECT_NAME worker --loglevel=info -s /tmp/celerybeat-schedule \$1"

source $VIRTUALENV_DIR/bin/activate
export PS1="[$PROJECT_NAME \W]\\$ "
cd $PROJECT_DIR
EOF
