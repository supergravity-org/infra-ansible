Exim4
=====

Installs and configures Exim4 as an internet mailer. Role features include:

* SPF record checking on inbound mail
* Antivirus support (ClamAV)
* Anti spam support (Spamassassin)
* Authentication via SASLauthd
* Fail2ban filter for restricting automated attacks on port 25
* OpenSSL key generation (if needed)

DKIM mail verification on inbound mail is still planned and DKIM mail signing
on outbound mail is a work in progress.

This has only been tested on Debian Wheezy but in theory will work on any
Debian based system. Work is ongoing to ensure RedHat family of systems are
supported correctly by the role as well.

Requirements
------------

This role doesn't install an antivirus so if you wish to use that functionality
you will need to install one yourself.

Because this role uses sasl for authentication by default it authenticates
against the system user database. Thats fine where user=account but not if you
intend to do virtual mail hosting (where mail accounts are separate to system
accounts).
In those cases the authentication part of the role may need to be changed -
feel free to let me know if you would like to see options available in the role

Role Variables
--------------

Exim4 configuration template variables and their defaults

```
openssl_certs_path: /etc/ssl/
openssl_keys_path: /etc/ssl/
exim_primary_hostname: 'example.com'
exim_domainlist_local_domains: '@:localhost'
exim_domainlist_relay_to_domains: ''
exim_hostlist_relay_from_hosts: '127.0.0.1'
exim_av_scanner_enable: false
exim_av_scanner_path: clamd:/var/run/clamav/clamd.ctl
exim_spamd_enable: false
exim_spamd_address: '127.0.0.1 783'
exim_tls_enable: true
exim_tls_advertise_hosts: ''
exim_daemon_smtp_ports: '25 : 465 : 587'
exim_tls_on_connect_ports: '465'
exim_check_rfc2047_length_enable: false
exim_acl_check_rcpt_dnsbls_enable: true
exim_acl_check_rcpt_host_lookup_enable: true
exim_acl_check_rcpt_spf_enable: true
exim_acl_check_data_malware_enable: true
exim_acl_check_data_spam_enable: true
exim_routers_localuser_use_maildir: true
exim_transport_remote_smtp_dkim_enable: false
exim_transport_remote_smtp_dkim_domain: '${lookup{$sender_address}lsearch*@{/etc/exim4/dkim-senders.list}}'
exim_transport_remote_smtp_dkim_selector: '$dkim_domain'
exim_transport_remote_smtp_dkim_private_key: ''
exim_transport_remote_smtp_dkim_canon: 'relaxed'
exim_transport_remote_smtp_dkim_strict: 'false'
exim_transport_remote_smtp_dkim_sign_headers: ''
```

# Should we install the fail2ban filter for exim+saslauthd
exim_fail2ban_enable: false

Further work
------------
* Finish DKIM support
* Split clamav/spamassassin/sasl install and configuration to their own roles

Dependencies
------------

franklinkim.openssl is used by this role. This role overrides
openssl_certs_path and openssl_keys_path in its defaults but leaves the
specifics of handling the key alone. Please refer to the openssl role README to
seee its other options.

goetzk.spamassassin is used to handle the installation and configuration of
spamassassin. Integration between the roles should improve once the split
between them is complete.

Example Playbook
----------------

    - hosts: servers
      vars:
         - exim_primary_hostname: smtp.example.com
      roles:
         - goetzk.exim

License
-------

GPL2+

Author Information
------------------

Issues or feedback can be reported to the author at karl@kgoetz.id.au; please
prefix the subject with 'ansible' or 'role'.

