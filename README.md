# nephelaiio.pyenv

[![Build Status](https://github.com/nephelaiio/ansible-role-pyenv/workflows/CI/badge.svg)](https://github.com/nephelaiio/ansible-role-pyenv/actions)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-nephelaiio.pyenv-blue.svg)](https://galaxy.ansible.com/nephelaiio/pyenv/)

An [ansible role](https://galaxy.ansible.com/nephelaiio/pyenv) to install and configure pyenv

## Role Variables

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.
* [nephelaiio.devtools](https://galaxy.ansible.com/nephelaiio/devtools)

## Example Playbook

```
- hosts: servers
  roles:
     - role: nephelaiio.pyenv
```

## Testing

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](https://github.com/nephelaiio/ansible-role-requirements/blob/master/requirements.txt)

Role is tested against the following distributions (docker images):
  * Ubuntu Focal
  * Ubuntu Bionic
  * Ubuntu Xenial
  * CentOS 7
  * Debian Buster

You can test the role directly from sources using command ` molecule test ` 

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
