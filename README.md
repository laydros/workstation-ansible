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
- **mac-based.yml** – installs Homebrew packages via the `software` role.
- **site.yml** – example playbook invoking the generic `software` role.

## Roles

Each directory under `roles/` contains an Ansible role. Highlights include:

- **common** – legacy base packages role now superseded by `software`.
- **flatpak** – installs flatpak and a selection of desktop applications from Flathub.
- **gnome_setup** – configures GNOME settings and keyboard shortcuts.
- **m3db_client** – optional setup for mounting a network share.
- **software** – unified package installation role for Debian, Fedora, and macOS. Optional tasks install Rust and Firefox.

### Optional installs

Set these variables in `group_vars/all.yml` to control which extras the `software` role installs:

```yaml
install_rust: true
install_firefox: true
install_firefox_dev: false
```

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

## Development Setup and Testing

These steps assume you are working within a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt

# Install required Ansible collections
ansible-galaxy collection install -r requirements.yml
```

Run linting and syntax checks:

```bash
ansible-lint
yamllint .
ansible-playbook playbooks/site.yml --syntax-check
```

Execute the test suite:

```bash
ansible-playbook tests/test_all.yml --check -i inventory/hosts.yml
cd roles/software && molecule test
```
