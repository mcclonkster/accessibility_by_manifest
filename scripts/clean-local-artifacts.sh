#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

APPLY=0
INCLUDE_VENVS=0

for arg in "$@"; do
  case "$arg" in
    --apply)
      APPLY=1
      ;;
    --include-venvs)
      INCLUDE_VENVS=1
      ;;
    *)
      echo "Unknown argument: $arg" >&2
      echo "Usage: scripts/clean-local-artifacts.sh [--apply] [--include-venvs]" >&2
      exit 2
      ;;
  esac
done

paths=()

for path in ".pytest_cache" "test_outputs" "quarantine/system-files"; do
  if [[ -e "$path" ]]; then
    paths+=("$path")
  fi
done

while IFS= read -r path; do
  paths+=("$path")
done < <(
  find . \
    \( -path './.git' -o -path './.venv' -o -path './.agents/*/.venv' \) -prune \
    -o -type d -name __pycache__ -print
)

while IFS= read -r path; do
  paths+=("$path")
done < <(
  find . \
    \( -path './.git' -o -path './.venv' -o -path './.agents/*/.venv' \) -prune \
    -o -type f -name .DS_Store -print
)

if [[ "$INCLUDE_VENVS" -eq 1 ]]; then
  if [[ -e ".venv" ]]; then
    paths+=(".venv")
  fi
  while IFS= read -r path; do
    paths+=("$path")
  done < <(find .agents -path '*/.venv' -type d -prune -print 2>/dev/null || true)
fi

if [[ "${#paths[@]}" -eq 0 ]]; then
  echo "No local artifacts found."
  exit 0
fi

if [[ "$APPLY" -eq 0 ]]; then
  echo "Dry run. Re-run with --apply to remove these local artifacts:"
  printf '  %s\n' "${paths[@]}"
  exit 0
fi

rm -rf "${paths[@]}"
echo "Removed local artifacts."
