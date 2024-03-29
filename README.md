[![pipeline status](https://gitlab.com/dudefellah/ansible-role-postgresql_replication/badges/main/pipeline.svg)](https://gitlab.com/dudefellah/ansible-role-postgresql_replication/-/commits/main)

PostgresSQL Replication
=========

Set up replication on postgresql servers.

Requirements
------------

Some of the database interaction happens by becoming the local postgres
user. This means that 'become' needs to work, or in other words, if you
don't have sudo installed or your become method set to something else like
`su`, this role will probably fail.

Role Variables
--------------

Role variables are listed and documented in
[main/defaults.yml](main/defaults.yml).

Dependencies
------------

This role uses the [community.general](https://galaxy.ansible.com/community/general)
collection. It also uses [community.postgresql](https://docs.ansible.com/ansible/latest/collections/community/postgresql/index.html)
for Postgres modules.

You will need to install these collections prior to using this role.

Before using this role, you will need to have Postgres installed as well.
I have a role available for this
[here](https://galaxy.ansible.com/dudefellah/postgresql), but you're free
to install and configure Postgres however you'd prefer.

Example Playbook
----------------

Once your postgres instances are installed, you will need to set your primary
server through your host_vars:

* host\_vars/primary.yml

    postgresql_replication_primary: true

* host\_vars/replica.yml

    postgresql_replication_primary: false

Then finally, in your playbook you can have something like this:

    - hosts: pg_servers
      roles:
         - role: dudefellah.postgresql_replication
           postgresql_replication_user: replica
           postgresql_replication_password: replica123
           postgresql_replication_postgresql_conf_filename: /var/lib/pgsql/11/data/postgresql.conf
           postgresql_replication_pg_hba_conf_filename: /var/lib/pgsql/11/data/pg_hba.conf
           postgresql_replication_data_dir: /var/lib/pgsql/11/data

License
-------

GPLv3

Author Information
------------------

Dan - github.com/dudefellah
