# Nix MCP Extension

This extension provides tools to manage Nix flakes and scaffold projects.

## Tools

### `nix_flake_init`
Initializes a new `flake.nix` in the specified directory.
- **directory**: (Optional) The directory to initialize. Defaults to current.
- **template**: (Optional) A specific template to use.

### `nix_flake_check`
Runs `nix flake check` to verify the flake's validity.
- **directory**: (Optional) The directory containing the flake.

### `nix_flake_update`
Updates the flake's inputs.
- **directory**: (Optional) The directory containing the flake.

### `nix_scaffold_dendritic`
Scaffolds a new Nix project following the "Dendritic" (modular flake-parts) pattern.
- **directory**: (Optional) Target directory.
- **name**: (Optional) Name of the project/flake.
