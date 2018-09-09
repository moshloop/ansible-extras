

### Ansible Extras

Ansible Role for creating systemd services, for managing existing services use the built-in [systemd](https://docs.ansible.com/ansible/latest/modules/systemd_module.html) module.

## Filters

| name                                          | description                                                  |
| --------------------------------------------- | ------------------------------------------------------------ |
| **file_exists**(path)                         |                                                              |
| **dir_exists**(path)                          |                                                              |
| **is_empty**(val)                             |                                                              |
| **jsonpath**(data)                            | transforms data using jsonpath_rw                            |
| **nestedelement**(path)                       | Returns an nested element from an object tree by path (seperated by / or .) |
| **play_groups**(play_hosts, groups, hostvars) | Returns a list of groups that are active within a play       |
| **split**(string, separator=' ')              |                                                              |
| **to_map**(map, key, value)                   |                                                              |
| **walk_up**(object, path)                     | Walks up an object tree from the lowest level collecting all attributes not available at lower levels |
| **map_to_entries**(dict, key, value)          | Convert a dict into a list of entries                        |
| **sub_map**(dict, prefix)                     | Filter a map by key prefix and remove prefix from keys       |


#### cloudinit_iso

```yaml
      - cloudinit_iso:
          dest: "{{playbook_dir}}/cloudinit.iso"
          user: |
            #cloud-config
            preserve_hostname: true
            hostname: ansible-hostname
            users:
                - name: hostname
```

#### systemd_service
**Options**
```
OPTIONS (= is mandatory):
= ExecStart
= Name
- Description
- InstallArgs
- RestartOn [Default: on-failure]
- RunAs [Default: root]
- ServiceArgs
- UnitArgs
- WantedBy [Default: multi-user.target]
- state (Choices: present, absent)[Default: present]
```

**EXAMPLES**
```yaml
  - hosts: all
    roles:
      - moshloop.systemd
    tasks:
        - systemd_service:
            Name: test
            ExecStart: "/usr/bin/nc -l 200"
        - systemd_service:
            Name: test
            ExecStart: "/usr/bin/nc -l 200"
            UnitArgs:
                After: networking.service
```

### Dependencies

- genisoimage