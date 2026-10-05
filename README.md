# INFINITE LXC VPS Bot — Modular 7.0 PRO

Modular refactor of the supplied `PAID-LXC-BOT-7.0(1).py`. Existing command names and major VPS/node/admin functions are preserved.

## Install

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export DISCORD_TOKEN="YOUR_BOT_TOKEN"
export MAIN_ADMIN_ID="YOUR_DISCORD_USER_ID"
export BOT_NAME="INFINITE VPS BOT"
python3 main.py
```

## Important fixes

- VPS container names are sanitized so bot names containing spaces cannot break `lxc init`.
- Fixed the resource-add command that previously sent the literal `stop {vps_id}`.
- SQLite port deallocation uses `MAX()` instead of `GREATEST()`.
- Node tag editing no longer double-encodes JSON.
- Force node deletion attempts to delete real LXC containers before database cleanup.
- Duplicate host-stat implementations are consolidated.
- The hardcoded Discord token from the supplied file is removed; use `DISCORD_TOKEN` instead.
