from testinfra.utils.ansible_runner import AnsibleRunner


testinfra_hosts = \
    AnsibleRunner('.molecule/ansible_inventory').get_hosts('test')


def test_command(Command):
    cmd = '/bin/bash -l -c "pyenv --version"'
    assert Command(cmd).rc == 0
