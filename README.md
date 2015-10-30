supergravity ansible roles
==========================

This ansible repository configures the (http://supergravity.org)[supergravity] infrastructure.


HOWTO
-----

This setup is only tested on linux (feedback about other systems welcome)

install (https://docs.chef.io/install_dk.html)[chefdk] (required for (http://kitchen.ci)[testkitchen]).
install (https://www.vagrantup.com/downloads.html)[vagrant]
install python with virtualenv.
Debian/Ubuntu:

```sh
  apt-get install python-virtualenv git
```

Enter test environment:
```sh
  git clone https://github.com/supergravity-org/infra-ansible.git
  cd infra-ansible
  . ./enter.sh
```

To run your configuration simply run:

```sh
  kitchen converge web
```

It will start a virtual machine and configures it for the webservices used.

Change your '''/etc/hosts''' file:
```
127.0.0.1       localhost [...] ask.supergravity.local supergravity.local wiki.supergravity.local www.supergravity.local
```

Now you can visit (http://supergravity.local:8080)[http://supergravity.local:8080] for your changes.


Directory structure
-------------------

| Directory/File | Content |
| ---------------|---------|
| etc/           | host files |
| roles          | ansible roles for configuration of services |
| keystore       | encrypted passwords for services |
| supergravity_main | (http://wagtail.io)[wagtail] root of cms |
| tasks/         | ansible tasks for rolling out |
| .kitchen.yml   | kitchen configuration for testing |


Tips
----

Because ansible would configure everything from start to bottom which is not
necessary most of the time, you can jump to the last place that worked well by
setting a environment variable:

```sh
ANSIBLE_EXTRA_FLAGS='--start-at-task="discourse | Clone discourse_docker repo"' kitchen converge web
```

Will save you a lot of time :)
