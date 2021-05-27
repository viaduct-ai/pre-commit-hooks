# pre-commit-hooks
Viaduct's pre-commit hooks 

## Available hooks

- check_notebook_has_parameters_cell: Check that all notebooks contain a cell tagged with `parameters` (for [papermill](https://papermill.readthedocs.io/en/latest/usage-parameterize.html))
- nbstripout: Strip outputs from notebooks.
- validate_encrypted_secret_name: Check kubernetes [SOPS](https://github.com/viaduct-ai/kustomize-sops/) encrypted yaml secrets filenames end with `.enc.yaml`
- validate_secrets_are_encrypted: Check kubernetes secrets are encrypted with [SOPS](https://github.com/viaduct-ai/kustomize-sops/)
