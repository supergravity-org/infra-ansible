#!/bin/bash
# openssl req -new -key supergravity_private.pem -sha256 -nodes \
#   -subj '/C=DE/ST=Sachsen/L=Dresden/O=Supergravity/OU=IT/CN=supergravity.org/
#          subjectAltName=DNS.1=ask.supergravity.org,
#          DNS.2=wiki.supergravity.org,DNS.3=discuss.supergravity.org' > supergravity.csr
openssl req -new -sha256 \
    -key supergravity_private.pem \
    -subj "/C=DE/ST=Sachsen/O=Supergravity/CN=supergravity.org" \
    -reqexts SAN \
    -config <(cat /etc/ssl/openssl.cnf \
        <(printf "[SAN]\nsubjectAltName=DNS:*.supergravity.org,DNS:supergravity.me,DNS:*.supergravity.me,DNS:supergravity.us,DNS:*.supergravity.us")) \
    -out supergravity.csr
