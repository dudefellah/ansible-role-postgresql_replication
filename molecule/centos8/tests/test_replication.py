import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


# Tests that replication is up and running
def test_replication(host):
    primary_replication_query = "SELECT * FROM pg_stat_replication"
    replica_replication_query = "SELECT * FROM pg_stat_wal_receiver"

    if host.ansible.get_variables()['inventory_hostname'] == 'postgresql-molecule-centos-8-primary-instance':
        host.run_test("set -euxo pipefail && su - postgres -s /bin/bash -c \"psql -t -c 'SELECT * FROM pg_stat_replication'\" | grep -q '10.10.1.3'")
    elif host.ansible.get_variables()['inventory_hostname'] == 'postgresql-molecule-centos-8-replica-instance':
        host.run_test("set -euxo pipefail && su - postgres -s /bin/bash -c \"psql -t -c 'SELECT * FROM pg_stat_wal_receiver'\" | grep -q '10.10.1.2'")
