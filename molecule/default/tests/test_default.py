import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_unifi_service(host):
    unifi = host.service('unifi')

    assert unifi.is_running
    assert unifi.is_enabled
