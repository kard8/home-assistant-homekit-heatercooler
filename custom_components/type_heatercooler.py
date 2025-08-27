from homeassistant.components.homekit.accessories import HomeAccessory
from homeassistant.components.homekit.const import (
    SERV_HEATER_COOLER,
    CHAR_ACTIVE,
    CHAR_CURRENT_HEATER_COOLER_STATE,
    CHAR_TARGET_HEATER_COOLER_STATE,
    CHAR_ROTATION_SPEED,
    CHAR_SWING_MODE,
)
from pyhap.const import CATEGORY_AIR_CONDITIONER


class HeaterCoolerAccessory(HomeAccessory):
    """Expose a climate entity as a HeaterCooler service in HomeKit."""

    def __init__(self, hass, entity_id, display_name, aid):
        super().__init__(hass, display_name, aid=aid, category=CATEGORY_AIR_CONDITIONER)
        self.entity_id = entity_id

        serv = self.add_preload_service(
            SERV_HEATER_COOLER,
            [
                CHAR_ACTIVE,
                CHAR_CURRENT_HEATER_COOLER_STATE,
                CHAR_TARGET_HEATER_COOLER_STATE,
                CHAR_ROTATION_SPEED,
                CHAR_SWING_MODE,
            ],
        )

        self.char_active = serv.get_characteristic(CHAR_ACTIVE)
        self.char_current = serv.get_characteristic(CHAR_CURRENT_HEATER_COOLER_STATE)
        self.char_target = serv.get_characteristic(CHAR_TARGET_HEATER_COOLER_STATE)
        self.char_speed = serv.get_characteristic(CHAR_ROTATION_SPEED)
        self.char_swing = serv.get_characteristic(CHAR_SWING_MODE)

        self.hass.bus.async_listen("state_changed", self._update_state)

    def _update_state(self, event):
        new = event.data.get("new_state")
        if not new or new.entity_id != self.entity_id:
            return

        attrs = new.attributes
        hvac_mode = new.state

        # Map HVAC mode → HomeKit HeaterCooler
        if hvac_mode == "cool":
            self.char_target.set_value(2)  # Cool
        elif hvac_mode == "heat":
            self.char_target.set_value(1)  # Heat
        else:
            self.char_target.set_value(0)  # Auto/Off

        if "fan_mode" in attrs:
            try:
                speed = int(attrs["fan_mode"])
                self.char_speed.set_value(speed)
            except Exception:
                pass

        if "swing_mode" in attrs:
            self.char_swing.set_value(1 if attrs["swing_mode"] == "on" else 0)
