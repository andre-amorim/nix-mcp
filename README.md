# Nix MCP Extension

A Gemini CLI extension for managing Nix flakes and scaffolding projects.

## Prerequisites

- [Nix](https://nixos.org/download.html)
- [Gemini CLI](https://geminicli.com/)
- [uv](https://github.com/astral-sh/uv)

## Installation

1. Clone this repository.
2. Link the extension to Gemini CLI:
   ```bash
   gemini extensions link .
   ```
3. Restart Gemini CLI.

## Tools

| Tool | Description |
| :--- | :--- |
| `nix_flake_init` | Initialize a new flake in a directory. |
| `nix_flake_check` | Run `nix flake check` to verify validity. |
| `nix_flake_update` | Update flake inputs. |
| `nix_scaffold_dendritic` | Scaffold a project using the Dendritic (flake-parts) pattern. |

## Development

This extension is built with Python using `fastmcp`.

Run the server locally for testing:
```bash
uv run nix-mcp
```
