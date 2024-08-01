# xxy

## Config file
Config file is under `~/.xxy_cfg.json`.

## Development
Install dependency
```shell
pip install -e .[dev]
```

### Log critiria
- Error: Something wrong, can't run anymore.
- Warning: Something wrong, but can still run.
- Success: At most once per run. User should easy to understand.
- Info: More than once per run. User should easy to understand.
- Debug: at most three per second, technical details for developers.
- Trace: more than three per second, easy to know where code is hang.
