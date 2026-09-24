#!/usr/bin/env bash
# Seed GitHub milestones, labels, and issues from backlog.json.
#
# Requires: gh (GitHub CLI, logged in with `gh auth login`) and jq.
# Run from anywhere inside your cloned repo:
#
#   DRY_RUN=1 tools/backlog/seed_issues.sh   # preview only
#   tools/backlog/seed_issues.sh             # create for real
#
# NOT idempotent for issues: running twice creates duplicates.
set -euo pipefail

cd "$(dirname "$0")"
FILE="backlog.json"

command -v gh >/dev/null || { echo "gh (GitHub CLI) is required"; exit 1; }
command -v jq >/dev/null || { echo "jq is required"; exit 1; }

run() {
  if [[ "${DRY_RUN:-0}" == "1" ]]; then
    printf 'DRY RUN:'; printf ' %q' "$@"; printf '\n'
  else
    "$@"
  fi
}

echo "== milestones"
jq -r '.milestones[]' "$FILE" | while IFS= read -r m; do
  run gh api "repos/{owner}/{repo}/milestones" -f title="$m" --silent || echo "  (exists?) $m"
done

echo "== labels"
jq -r '.labels[] | [.name, .color, .description] | @tsv' "$FILE" |
while IFS=$'\t' read -r name color desc; do
  run gh label create "$name" --color "$color" --description "$desc" --force
done

echo "== issues"
jq -c '.issues[]' "$FILE" | while IFS= read -r issue; do
  title=$(jq -r '.title' <<<"$issue")
  body=$(jq -r '.body' <<<"$issue")
  milestone=$(jq -r '.milestone' <<<"$issue")
  labels=$(jq -r '.labels | join(",")' <<<"$issue")
  run gh issue create --title "$title" --body "$body" --milestone "$milestone" --label "$labels"
done

echo "done."
