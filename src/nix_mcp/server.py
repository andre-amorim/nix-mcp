
import os
import subprocess
from pathlib import Path
from typing import Optional
from fastmcp import FastMCP

# Initialize FastMCP
mcp = FastMCP("nix-mcp")

@mcp.tool()
def nix_flake_init(directory: str = ".", template: Optional[str] = None) -> str:
    """Initialize a new flake in the specified directory."""
    cmd = ["nix", "flake", "init"]
    if template:
        cmd.extend(["--template", template])
    
    try:
        subprocess.run(cmd, cwd=directory, check=True, capture_output=True, text=True)
        return f"Successfully initialized flake in {directory}"
    except subprocess.CalledProcessError as e:
        return f"Error initializing flake: {e.stderr}"

@mcp.tool()
def nix_flake_check(directory: str = ".") -> str:
    """Run nix flake check."""
    try:
        subprocess.run(["nix", "flake", "check"], cwd=directory, check=True, capture_output=True, text=True)
        return "Flake check passed."
    except subprocess.CalledProcessError as e:
        return f"Flake check failed: {e.stderr}"

@mcp.tool()
def nix_flake_update(directory: str = ".") -> str:
    """Run nix flake update."""
    try:
        subprocess.run(["nix", "flake", "update"], cwd=directory, check=True, capture_output=True, text=True)
        return "Flake updated successfully."
    except subprocess.CalledProcessError as e:
        return f"Error updating flake: {e.stderr}"

@mcp.tool()
def nix_scaffold_dendritic(directory: str = ".", name: str = "my-dendritic-flake") -> str:
    """Scaffold a new Nix project following the Dendritic (modular flake-parts) pattern.
    
    Creates:
    - flake.nix (using flake-parts)
    - systems/ (host configurations)
    - modules/ (shared modules)
    - pkgs/ (custom packages)
    - README.md
    """
    target_dir = Path(directory)
    target_dir.mkdir(parents=True, exist_ok=True)

    # Create directory structure
    (target_dir / "systems").mkdir(exist_ok=True)
    (target_dir / "modules").mkdir(exist_ok=True)
    (target_dir / "pkgs").mkdir(exist_ok=True)

    # flake.nix content
    flake_nix = """{
  description = "%s";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
  };

  outputs = inputs@{ flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [ "x86_64-linux" "aarch64-linux" "aarch64-darwin" "x86_64-darwin" ];
      
      # Import your modules here. 
      # In the Dendritic pattern, you treat every file as a module.
      imports = [
        ./modules
      ];

      perSystem = { config, self', inputs', pkgs, system, ... }: {
        # Per-system configuration (packages, devShells, checks)
        # packages.default = pkgs.callPackage ./pkgs/my-package.nix {};
      };
    };
}
""" % name

    # Write flake.nix
    with open(target_dir / "flake.nix", "w") as f:
        f.write(flake_nix)

    # Write modules/default.nix to make the import work
    modules_default = """{
  imports = [
    # Add your shared modules here
  ];
}
"""
    with open(target_dir / "modules/default.nix", "w") as f:
        f.write(modules_default)

    # README
    readme = """# %s

This project is structured following the Dendritic pattern principles using `flake-parts`.

## Structure

- `flake.nix`: Entry point.
- `modules/`: Shared NixOS/Home Manager modules.
- `systems/`: System configurations (hosts).
- `pkgs/`: Custom packages.

## Usage

- `nix flake check`: Verify configuration.
- `nix run .#<app>`: Run an app.
""" % name

    with open(target_dir / "README.md", "w") as f:
        f.write(readme)

    return f"Successfully scaffolded Dendritic project in {target_dir}"

if __name__ == "__main__":
    mcp.run()
