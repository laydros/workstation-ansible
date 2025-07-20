#!/bin/bash

set -euo pipefail

# Lint and Syntax Check
echo "Running Lint and Syntax Checks..."
yamllint .
ansible-lint
ansible-playbook playbooks/site.yml --syntax-check

# Playbook Tests
echo "Running Playbook Tests..."
ansible-playbook tests/test_all.yml --check -i inventory/hosts.yml
ansible-playbook tests/test_personal_linux.yml --check -i inventory/hosts.yml
ansible-playbook tests/test_work_mac.yml --check -i inventory/hosts.yml

# Molecule Tests
echo "Running Molecule Tests..."
for role in roles/*/; do
  if [ -f "${role}molecule/default/molecule.yml" ]; then
    echo "Testing role: $(basename "${role}")"
    (cd "${role}" && molecule test)
  fi
done

echo "All tests passed!"
