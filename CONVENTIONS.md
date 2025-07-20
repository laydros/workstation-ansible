# Conventions

This project follows a few simple conventions to keep the Ansible codebase consistent.

## YAML Style
- Use two spaces for indentation.
- Keys and variables use `snake_case`.
- Boolean values should be `true`/`false` rather than `yes`/`no`.

## Ansible Practices
- Prefer fully qualified module names (e.g. `ansible.builtin.package`).
- Use `package` where possible instead of distro-specific modules.
- Use `loop` instead of deprecated `with_items`.
- Keep tasks idempotent and guarded with `when:` conditions.

## Linting and Tests
- Run `ansible-lint` and `yamllint .` before committing.
- Validate playbooks with `ansible-playbook playbooks/site.yml --syntax-check`.
- Example tests can be run with `ansible-playbook tests/test_all.yml` and `molecule test` in `roles/software`.

