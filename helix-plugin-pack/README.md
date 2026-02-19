# Helix Plugin Pack (Test)

Repo testowy pod instalacje wielu pluginow do HelixBot.

## Zawartosc

- `plugin1`
- `plugin2`
- `plugin3`

Kazdy plugin ma wymagana strukture:

- `__init__.py`
- `plugin.py`
- `commands.py`
- `events.py`
- `config_schema.py`
- `helix_plugin.json`

## Test instalacji

### Prefix command

```bash
!plugin install_pack https://github.com/<twoj-user>/helix-plugin-pack plugin1 plugin2 plugin3
```

### Slash command

```text
/plugin install_pack repo_url:https://github.com/<twoj-user>/helix-plugin-pack names_csv:plugin1,plugin2,plugin3
```

Potem sprawdz:

- `!plugin list`
- `/plugin list`
