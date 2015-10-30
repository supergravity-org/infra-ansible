supergravity ansible roles
==========================

This ansible repository configures the [supergravity](http://supergravity.org) infrastructure.


HOWTO
-----

This setup is only tested on linux (feedback about other systems welcome)

install [chefdk](https://docs.chef.io/install_dk.html) (required for [testkitchen](http://kitchen.ci)).
install [vagrant](https://www.vagrantup.com/downloads.html)
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

To see a list of targets:

```sh
  kitchen list
```



It will start a virtual machine and configures it for the webservices used.

Change your '''/etc/hosts''' file:
```
127.0.0.1       localhost [...] ask.supergravity.local supergravity.local wiki.supergravity.local www.supergravity.local
```

Now you can visit [http://supergravity.local:8080](http://supergravity.local:8080) for your changes.


Directory structure
-------------------

| Directory/File | Content |
| ---------------|---------|
| etc/           | host files |
| roles          | ansible roles for configuration of services |
| keystore       | encrypted passwords for services |
| supergravity_main | [wagtail](http://wagtail.io) root of cms |
| tasks/         | ansible tasks for rolling out |
| .kitchen.yml   | kitchen configuration for testing |

Software used
-------------

 * [wagtail](http://wagtail.io) cms
 * [askbot](http://askbot.org) question/answer site
 * [discourse](http://www.discourse.org) discussion platform (IN PROGRESS)
 * [docuwiki](https://www.dokuwiki.org) wiki (TODO) (in docker, no php on the host)


Tips
----

Because ansible would configure everything from start to bottom which is not
necessary most of the time, you can jump to the last place that worked well by
setting a environment variable:

```sh
ANSIBLE_EXTRA_FLAGS='--start-at-task="discourse | Clone discourse_docker repo"' kitchen converge web
```

Will save you a lot of time :)
