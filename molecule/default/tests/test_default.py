import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_command(Command):
    cmd = '/bin/bash -l -c "pyenv --version"'
    assert Command(cmd).rc == 0
