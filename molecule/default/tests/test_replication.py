import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


# Tests that replication is up and running
def test_replication(host):
    primary_replication_query = "SELECT * FROM pg_stat_replication"
    replica_replication_query = "SELECT * FROM pg_stat_wal_receiver"

    replication = ''
    if 'primary' in host.ansible.get_variables()['inventory_hostname']:
        replication = host.run("set -eu && su - postgres -s /bin/bash -c \"psql -t -c 'SELECT * FROM pg_stat_replication'\"")
    elif 'replica' in host.ansible.get_variables()['inventory_hostname']:
        replication = host.run_test("set -eu && su - postgres -s /bin/bash -c \"psql -t -c 'SELECT * FROM pg_stat_wal_receiver'\"")

    assert ('10.10' in replication.stdout)
