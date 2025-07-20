# Ansible Project Review

This is a personal Ansible setup for managing laptops and desktops across macOS, Linux (Debian/Fedora/Arch), and Windows (via WSL). The goal is to keep it modular, declarative, and as cross-platform as possible without overengineering.

## Please review the entire Ansible project for:

- YAML syntax errors or formatting issues
- Ansible best practices (role structure, variable use, `when` conditions, idempotency, etc.)
- Redundant files or legacy cruft that should be removed
- Naming issues or inconsistencies across files
- Tasks or playbooks that may run in the wrong order or be ineffective
- Opportunities to DRY up repeated logic
- Typos in task names, variables, or file paths
- Logical gaps where a system may not be configured as expected

## Structure

Here’s how the repo is organized:

- `inventory/hosts.yml`: defines personal/work/mac/linux groups
- `group_vars/`: defines vars by group (e.g. `personal_linux.yml`, `laptop.yml`, etc.)
- `playbooks/site.yml`: the main entry point, targeting groups
- `roles/software/`: installs shared and OS-specific packages
- `roles/xdg_dirs/`: sets up XDG directories and user folder remaps
- `roles/gnome_setup/`: optional DE config
- `roles/common/`: deprecated
- All Firefox and Rust install logic has been moved to `software/tasks/` with toggles like `install_rust: true`

## Notes

- macOS uses Homebrew (with cask support)
- Linux installs may use Apt, DNF, or Pacman
- Fedora RPM Fusion setup is done in `software/tasks/setup_fedora_repos.yml`
- Package lists are stored in `software/vars/main.yml` with a canonical name and OS-specific aliases
- Windows support is experimental/minimal for now

## Goal

Give me a list of:
- Critical issues (syntax, broken logic)
- Warnings (redundancy, non-idiomatic Ansible)
- Suggestions (naming, structure improvements, maintainability tips)
