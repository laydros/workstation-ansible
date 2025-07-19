# Workstation Ansible Playbooks

These playbooks provision a personal workstation across a few different operating systems. The inventory currently contains a single host group, `laptop`, which points to `localhost` for running the playbooks locally.

## Quick start

Run Ansible locally against the desired playbook:

```bash
ansible-playbook -i hosts debian-based.yml  -c local -K
ansible-playbook -i hosts fedora-based.yml  -c local -K
ansible-playbook -i hosts mac-based.yml     -c local -K
```

`site.yml` includes a minimal role set for experimentation and can also be executed in the same way.

## Playbooks

- **debian-based.yml** – installs common packages for Debian/Ubuntu systems using the `common` and `flatpak` roles.
- **fedora-based.yml** – installs packages for Fedora systems and applies GNOME tweaks. Roles used: `common`, `m3db_client`, `gnome_setup`, and `flatpak`.
- **mac-based.yml** – installs Homebrew packages via the `mac-software` role.
- **site.yml** – example playbook invoking the generic `software` role.

## Roles

Each directory under `roles/` contains an Ansible role. Highlights include:

- **common** – basic command line tools, Rust installation, and Firefox setup.
- **flatpak** – installs flatpak and a selection of desktop applications from Flathub.
- **gnome_setup** – configures GNOME settings and keyboard shortcuts.
- **m3db_client** – optional setup for mounting a network share.
- **debian_software**, **fedora-software**, **mac-software**, and **software** – OS specific package lists.

Role READMEs currently contain only scaffolding text.

## Documentation

The `doc/` directory holds notes for various machines and manual setup steps. These documents are not automated yet but serve as references while the roles evolve.

## Credits

The repository makes use of ideas and snippets from:

- <https://github.com/jnv/ansible-role-debian-backports>
- <https://github.com/cisagov/ansible-role-backports>
- <https://github.com/hurricanehrndz/ansible-rustup>
- <https://github.com/abaez/ansible-role-rustup>

## Future improvements

This repository is a work in progress. Some ideas to align the layout with Ansible best practices:

- Add an `ansible.cfg` file to define defaults such as `inventory` and `connection`.
- Move OS specific variables into `group_vars/` and `host_vars/` instead of including files from tasks.
- Flesh out the README for each role with purpose and usage details.
- Use tags and handlers consistently so pieces can be executed independently.
- Consider a `playbooks/` directory for the entry point playbooks to keep the root tidy.
- Gradually convert manual steps from the `doc/` directory into automated tasks.
