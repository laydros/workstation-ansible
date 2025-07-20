# Workstation Ansible Playbooks

These playbooks configure personal and work machines across Linux, macOS and Windows.
The main entry point is `playbooks/site.yml` and inventory is defined in
`inventory/hosts.yml`.

## Quick start

Create a Python virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
ansible-galaxy collection install -r requirements.yml
```

Run the playbook against a host group:

```bash
ansible-playbook playbooks/site.yml --limit <group>
```

Available groups include `personal_linux`, `personal_macos`, `personal_windows`,
`work_linux`, `work_windows`, as well as convenience groups like `laptop`,
`desktop`, `vm`, `linux`, `mac` and `windows`. The `ansible.cfg` file already sets
the default inventory and connection options.

## Inventory and Variables

Group variables live under `group_vars/` and control optional role behaviour.
Examples include enabling Flatpak applications or installing Rust.

## Roles

Current roles are located under `roles/`:

- **software** – installs common and OS specific packages. Optional tasks can
  install Rust and Firefox.
- **flatpak** – installs Flatpak and user scoped applications.
- **xdg_dirs** – configures XDG user directories on Linux.
- **gnome_setup** – applies GNOME desktop settings.
- **m3db_client** – mounts the m3db network share for work machines.

Set variables such as `install_rust`, `install_firefox`, `install_firefox_dev`,
`install_m3db` and `configure_xdg_dirs` in the appropriate `group_vars` files to
control these extras.

## Documentation

Manual notes and machine specific setup steps live under the `doc/` directory.

## Development and Testing

Use the provided tools to lint and test the playbooks:

```bash
ansible-lint
yamllint .
ansible-playbook playbooks/site.yml --syntax-check
ansible-playbook tests/test_all.yml --check -i inventory/hosts.yml
cd roles/software && molecule test
```

## Credits

This project borrows ideas from:

- <https://github.com/jnv/ansible-role-debian-backports>
- <https://github.com/cisagov/ansible-role-backports>
- <https://github.com/hurricanehrndz/ansible-rustup>
- <https://github.com/abaez/ansible-role-rustup>

## Developer & Agent Docs
- [AGENTS.md](AGENTS.md)
- [CONVENTIONS.md](CONVENTIONS.md)
