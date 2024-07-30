.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.3.1 (2024-07-29)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add the following constant:

    - ``acore_constants.api.TagKey.WORLDSERVER_MEASURE_TIME = "wserver:worldserver_measure_time"``
    - ``acore_constants.api.TagKey.WORLDSERVER_IS_RDS_EXISTS = "wserver:worldserver_is_rds_exists"``
    - ``acore_constants.api.TagKey.WORLDSERVER_IS_RDS_RUNNING =`` "wserver:worldserver_is_rds_running"
    - ``acore_constants.api.TagKey.WORLDSERVER_RDS_STATUS = "wserver:worldserver_rds_status"``
    - ``acore_constants.api.TagKey.WORLDSERVER_CONNECTED_PLAYERS =`` "wserver:worldserver_connected_players"
    - ``acore_constants.api.TagKey.WORLDSERVER_CHARACTERS_IN_WORLD =`` "wserver:worldserver_characters_in_world"
    - ``acore_constants.api.TagKey.WORLDSERVER_SERVER_UPTIME = "wserver:worldserver_server_uptime"``
    - ``acore_constants.api.TagKey.WORLDSERVER_CPU_USAGE = "wserver:worldserver_cpu_usage"``
    - ``acore_constants.api.TagKey.WORLDSERVER_MEMORY_USAGE = "wserver:worldserver_memory_usage"``
    - ``acore_constants.api.TagKey.WORLDSERVER_TOTAL_MEMORY = "wserver:worldserver_total_memory"``
    - ``acore_constants.api.TagKey.WORLDSERVER_AVAILABLE_MEMORY = "wserver:worldserver_available_memory"``


0.2.1 (2023-06-26)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add the following constant:
    - ``acore_constants.api.TagKey.SERVER_LIFECYCLE = "wserver:server_lifecycle"``
    - ``acore_constants.api.ServerLifeCycle``
    - ``acore_constants.api.ServerLifeCycle.running = "running"``
    - ``acore_constants.api.ServerLifeCycle.smart_running = "smart_running"``
    - ``acore_constants.api.ServerLifeCycle.stopped = "stopped"``
    - ``acore_constants.api.ServerLifeCycle.deleted = "deleted"``


0.1.2 (2023-06-26)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- rename ``WOW_STATUS_TAG_KEY`` to ``WOW_STATUS``
- rename ``WOW_STATUS_MEASURE_TIME_TAG_KEY`` to ``WOW_STATUS_MEASURE_TIME``


0.1.1 (2023-06-26)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First release
- Add the following constant:
    - ``acore_constants.api.TagKey.SERVER_ID = "wserver:server_id"``
    - ``acore_constants.api.TagKey.WOW_STATUS_MEASURE_TIME_TAG_KEY = "wserver:wow_status_measure_time"``
    - ``acore_constants.api.TagKey.WOW_STATUS_TAG_KEY = "wserver:wow_status"``
