"""HomeKit HeaterCooler integration."""
from .const import DOMAIN

async def async_setup(hass, config):
    hass.data[DOMAIN] = {}
    return True

async def async_setup_entry(hass, entry):
    return True

async def async_unload_entry(hass, entry):
    return True
