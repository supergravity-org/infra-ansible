#!/bin/sh

if [ ! -e env ]; then
  virtualenv --prompt="(sglabs)" env
fi

. env/bin/activate

if [ ! -e env/bin/ansible ]; then
  pip install -r requirements.txt
fi

#export ANSIBLE_CONFIG='./ansible.cfg'
#export ANSIBLE_HOSTS=./etc/hosts
