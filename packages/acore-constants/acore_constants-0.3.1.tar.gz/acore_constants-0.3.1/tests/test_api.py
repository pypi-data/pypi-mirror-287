# -*- coding: utf-8 -*-

import os
import pytest


def test():
    from acore_constants import api

    _ = api.TagKey
    _ = api.TagKey.SERVER_ID
    _ = api.TagKey.SERVER_LIFECYCLE
    _ = api.TagKey.WOW_STATUS
    _ = api.TagKey.WOW_STATUS_MEASURE_TIME
    _ = api.TagKey.WORLDSERVER_MEASURE_TIME
    _ = api.TagKey.WORLDSERVER_IS_RDS_EXISTS
    _ = api.TagKey.WORLDSERVER_IS_RDS_RUNNING
    _ = api.TagKey.WORLDSERVER_RDS_STATUS
    _ = api.TagKey.WORLDSERVER_CONNECTED_PLAYERS
    _ = api.TagKey.WORLDSERVER_CHARACTERS_IN_WORLD
    _ = api.TagKey.WORLDSERVER_SERVER_UPTIME
    _ = api.TagKey.WORLDSERVER_CPU_USAGE
    _ = api.TagKey.WORLDSERVER_MEMORY_USAGE
    _ = api.TagKey.WORLDSERVER_TOTAL_MEMORY
    _ = api.TagKey.WORLDSERVER_AVAILABLE_MEMORY

    _ = api.ServerLifeCycle
    _ = api.ServerLifeCycle.running
    _ = api.ServerLifeCycle.smart_running
    _ = api.ServerLifeCycle.stopped
    _ = api.ServerLifeCycle.deleted


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
