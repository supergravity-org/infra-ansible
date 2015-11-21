ansible-role-discourse
======================

Install [Discourse](https://discourse.org).

Requirements
------------

This role needs docker to be installed. Practically, any distribution that
supports `docker >= 1.2` can use this role.

Minimun system RAM should be 1GB, with 2GB recommended.

Role Variables
--------------

In` defaults/main.yml` you will find variables that you normally don't need to
edit. In `vars/main.yml` there are variables like the hostname or the SMTP
server that you must change.

Place any variables that contain sensitive information in `vars/private.yml`.
A `private.yml.example` is provided as an example.

Dependencies
------------

Discourse depends solely on docker. There are multiple docker roles in Ansible
Galaxy, but not a single one that binds all the supported distributions
together. Find the one that supports your distribution and use that.

Tasks
-----

Apart from the main task that installs Discourse, another one called
`swap.yml` is provided. If your server has less than 2GB RAM, a swap file
is automatically created and the appropriate kernel parameters are set.

Scripts
-------

Inside the scripts directory, there is a `genssl` bash script which generates
a self signed certificate to use with Discourse.

Two files (`self_ssl.key` and `self_ssl.crt`) will be created under the scripts
folder. If you want to use them with your Discourse installation, move them
under `files/ssl/` and rename them to `ssl.key` and `ssl.crt`. By default,
anything that ends in `.key` or `.crt` is excluded from git history.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: axil42.discourse, discourse_hostname: 'talk.example.com' }

License
-------

MIT
