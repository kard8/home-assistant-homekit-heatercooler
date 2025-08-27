from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import HVACMode

async def async_setup_entry(hass, config_entry, async_add_entities):
    async_add_entities([HomeKitHeaterCooler()])

class HomeKitHeaterCooler(ClimateEntity):
    def __init__(self):
        self._attr_name = "HomeKit HeaterCooler"
        self._attr_hvac_mode = HVACMode.OFF

    @property
    def hvac_modes(self):
        return [HVACMode.OFF, HVACMode.COOL, HVACMode.HEAT, HVACMode.AUTO]

    def set_hvac_mode(self, hvac_mode):
        self._attr_hvac_mode = hvac_mode
        self.schedule_update_ha_state()
