#!/usr/bin/python
from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = r'''
---
module: gsettings
short_description: Manage GNOME settings
description: |
  Sets or gets values via the gsettings command line tool.
options:
  schema:
    description: GNOME schema to modify.
    type: str
    required: true
  key:
    description: Key within the schema.
    type: str
    required: true
  value:
    description: Value to set for the key.
    required: true
  path:
    description: Optional path for the key.
    type: str
'''

EXAMPLES = r'''
- name: Set a GNOME setting
  community.general.gsettings:
    schema: org.gnome.desktop.interface
    key: clock-show-date
    value: true
'''

RETURN = r'''
changed:
    description: Whether the setting was changed.
    type: bool
''' 

import shlex
import subprocess

def run(cmd):
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()

def main():
    module = AnsibleModule(
        argument_spec=dict(
            schema=dict(type='str', required=True),
            key=dict(type='str', required=True),
            value=dict(required=True),
            path=dict(type='str')
        ),
        supports_check_mode=True,
    )

    schema = module.params['schema']
    key = module.params['key']
    value = module.params['value']
    path = module.params.get('path')

    base = ['gsettings']
    if path:
        base += ['--path', path]
    get_cmd = base + ['get', schema, key]
    rc, stdout, stderr = run(get_cmd)
    if rc != 0:
        module.fail_json(msg=stderr)
    current = stdout
    desired = str(value).lower() if isinstance(value, bool) else str(value)

    if current == desired:
        module.exit_json(changed=False, current=current)

    if module.check_mode:
        module.exit_json(changed=True)

    set_cmd = base + ['set', schema, key, desired]
    rc, _, stderr = run(set_cmd)
    if rc != 0:
        module.fail_json(msg=stderr)

    module.exit_json(changed=True, current=desired)

if __name__ == '__main__':
    main()
