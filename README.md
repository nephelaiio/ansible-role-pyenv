# nephelaiio.pyenv

[![Build Status](https://travis-ci.org/nephelaiio/ansible-role-pyenv.svg?branch=master)](https://travis-ci.org/nephelaiio/ansible-role-pyenv)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-systemd--service-blue.svg)](https://galaxy.ansible.com/nephelaiio/pyenv/)

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

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](/requirements.txt)

Role is tested against the following distributions (docker images):
  * Ubuntu Xenial
  * CentOS 7
  * Debian Stretch
  * Arch Linux

You can test the role directly from sources using command ` molecule test ` 

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
