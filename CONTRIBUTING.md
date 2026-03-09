# Contributing

## Change classification

| Class | Paths | Review required | Notes |
|-------|-------|----------------|-------|
| Safety-critical | `data/registers/oadc-*`, `docs/adversarial/duress-*`, `docs/cross-cutting/safe-state*`, `schemas/` | Safety/security lead + independent reviewer | Two-person review; impact analysis required |
| Contract | `policies/`, `docs/contracts/` | Legal review + CISO + management | Operating contracts are operationally binding |
| Operational | `data/registers/` (non-OADC), `checklists/`, `templates/` | Peer review (1 reviewer) | |
| Documentation | `docs/` (non-critical) | Peer review (1 reviewer) | |

## Safety-critical change process

For any change to OADC definitions, duress protocols, safe-state specifications, or H-state thresholds:

1. Raise a change request describing the proposed change and rationale
2. Impact analysis: what does this change affect? (CACE: changing anything changes everything)
3. Safety/security lead reviews: does the change weaken any protection?
4. If new risks: update risk assessment before merging
5. Two-person review sign-off
6. Merge only to `main` after sign-off

## Commit conventions

- Sign all commits (GPG or SSH): `git commit -S`
- Use conventional commits: `feat:`, `fix:`, `docs:`, `policy:`, `register:`, `schema:`
- Policy approvals: create a signed tag `policy/POL-OR-XX-vN.N` after management sign-off

## Branch model

- `main` — approved, current governance state
- `draft/*` — work in progress
- No direct pushes to `main` — merge requests only

## Local validation

Run local validation before opening a merge request:

```bash
make validate
```

## Evidence

Every approved register update and policy version is stored in the evidence pipeline. Do not manually upload — use the merge-to-main CI trigger.
