import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_version(Command):
    versions = ['3.6.0']
    for version in versions:
        cmd_tpl = "/bin/bash -l -c \"pyenv versions | grep {}\""
        cmd = cmd_tpl.format(version)
        assert Command(cmd).rc == 0
