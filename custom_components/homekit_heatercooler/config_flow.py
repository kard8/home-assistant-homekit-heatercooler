from homeassistant import config_entries
import voluptuous as vol
from homeassistant.helpers.selector import selector

DOMAIN = "ac_heater_homekit"

class ACHomeKitFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(
                title="AC → HomeKit Heater/Cooler",
                data=user_input
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("ac_entity"): selector({
                    "entity": {"domain": "climate"}
                }),
            })
        )
