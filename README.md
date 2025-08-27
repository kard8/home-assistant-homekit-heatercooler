# HomeKit HeaterCooler for Home Assistant

This custom integration allows you to expose a `climate` entity to Apple HomeKit as a **HeaterCooler** accessory type, instead of the default Thermostat.

## Features
- Maps HA `climate` entities to HomeKit `HeaterCooler`
- Supports `hvac_mode` (heat, cool, auto)
- Fan speed control
- Swing/oscillation support

## Installation
1. Copy the `custom_components/homekit_heatercooler/` folder into your Home Assistant `config/custom_components/` directory.
2. Restart Home Assistant.
3. Configure your `homekit:` bridge in `configuration.yaml`.

```yaml
homekit:
  - filter:
      include_entities:
        - climate.living_room_ac
    entity_config:
      climate.living_room_ac:
        type: heatercooler
```

## HACS
This repo is HACS compatible. Add it as a custom repository in HACS.
