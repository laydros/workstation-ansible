<!-- AI_AGENT_GUIDANCE: This file provides AI agents with instructions on interacting with this codebase. -->

# AGENTS.md

## Introduction
This repository uses Ansible to configure personal and work computers. AI agents should consult this guide before modifying the codebase. It explains roles, variables and conventions so changes remain consistent.

---

## 🧠 Project Purpose

This repository configures personal and workstations across multiple platforms:
- Linux (Debian, Fedora, Arch)
- macOS (via Homebrew)
- Windows (via WSL, optional/experimental)

The system uses modular Ansible roles with host groups defined in `inventory/hosts.yml` and corresponding variables in `group_vars/`.

---

## 🧩 Role Overview

### `software`
Installs shared and platform-specific packages.
- Uses a canonical package list with OS-specific aliases (`software/vars/main.yml`)
- Installs optional components like Rust and Firefox based on group vars
- Enables RPM Fusion on Fedora
- Controlled by:
  - `install_rust`
  - `install_firefox`
  - `install_firefox_dev`

### `flatpak`
Installs Flatpak applications user-scoped.
- Controlled by `flatpak_apps` in group vars

### `xdg_dirs`
Configures and remaps XDG user directories on Linux systems.
- Controlled by `configure_xdg_dirs`

### `gnome_setup`
Sets GNOME desktop preferences via `gsettings` or `command`
- Controlled by `use_gnome`
- May require `changed_when: false` for idempotency

### `m3db_client`
Installs M3DB CLI and related work tooling.
- Controlled by `install_m3db`
- Typically only used on `work_linux` machines

---

## 🗂️ Inventory Structure

Defined in `inventory/hosts.yml` using YAML.

Host groups include:
- `personal_linux`, `personal_macos`, `personal_windows`
- `work_linux`, `work_windows`
- `laptop`, `desktop`, `vm`
- `mac`, `linux`, `windows`

Each group may have corresponding `group_vars/<group>.yml` files.

---

## 🧪 Testing and Execution

Main entry point:
```bash
ansible-playbook playbooks/site.yml
```

To limit to a specific group:
```bash
ansible-playbook playbooks/site.yml --limit laptop
```

Optional: you may use `--check` or `--diff` to preview changes.

---

## 🔍 Agent Guidelines

- Do not modify or restore the deprecated `roles/common/` directory
- Use `loop` instead of `with_items`
- Normalize `true/false` over `yes/no` in YAML
- Prefer the `package` module over distro-specific ones when possible, unless flags are needed
- Ensure all referenced variables have a default or are defined in `group_vars/`
- Respect `when:` conditionals and OS-specific logic when injecting new tasks

---

## 🧹 Cleanup State

The project is in a clean state post-refactor. Agents should:
- Avoid reintroducing old playbook structures (`fedora-based.yml`, etc.)
- Prefer idempotent tasks and cross-platform patterns

---

## ✍️ Maintainer Note

This repository is actively used to manage a mix of personal and work systems. AI agents should assume that consistency, readability, and predictability are more important than overly clever automation.

---

## Project Structure
- `playbooks/` contains entry point playbooks such as `site.yml`.
- `roles/` holds Ansible roles (`software`, `flatpak`, `gnome_setup`, `m3db_client`, `xdg_dirs`).
- `inventory/` defines host groups in `hosts.yml`.
- `group_vars/` stores group variable files.
- `tests/` contains example playbook tests.
- `doc/` holds assorted notes.

## Build & Run
Development typically uses a Python virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
ansible-galaxy collection install -r requirements.yml
```
Validate and execute playbooks:
```bash
ansible-lint
yamllint .
ansible-playbook playbooks/site.yml --syntax-check
ansible-playbook tests/test_all.yml --check -i inventory/hosts.yml
cd roles/software && molecule test
```

## Code Guidelines
See [CONVENTIONS.md](CONVENTIONS.md) for style and best practices.

## Contribution Workflow
1. Create a feature branch.
2. Make focused commits with clear messages.
3. Open a pull request targeting `main` and describe your changes.

## Related Docs
- [README.md](README.md)
- [CONVENTIONS.md](CONVENTIONS.md)

