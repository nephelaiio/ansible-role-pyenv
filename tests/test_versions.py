from testinfra.utils.ansible_runner import AnsibleRunner


testinfra_hosts = \
    AnsibleRunner('.molecule/ansible_inventory').get_hosts('compile')


def test_command(Command):
    versions = ['3.6.0']
    for version in versions:
        cmd_tpl = "/bin/bash -l -c \"pyenv versions | grep {}\""
        cmd = cmd_tpl.format(version)
        assert Command(cmd).rc == 0
