from __future__ import annotations

import logging

from core.di_container import ServiceContainer
from core.event_bus import EventBus
from core.plugin_base import BasePlugin

log = logging.getLogger(__name__)


class Plugin(BasePlugin):
    name = "plugin1"
    version = "0.1.0"
    dependencies = []

    async def setup(self, bot, container: ServiceContainer, event_bus: EventBus) -> None:
        _ = (bot, container, event_bus)
        log.info("[plugin:%s] setup complete", self.name)

    async def teardown(self) -> None:
        log.info("[plugin:%s] teardown complete", self.name)
