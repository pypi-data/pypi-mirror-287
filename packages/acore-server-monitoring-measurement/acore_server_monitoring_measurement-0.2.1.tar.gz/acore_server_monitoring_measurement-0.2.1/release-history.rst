.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.2.1 (2024-07-29)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add ``cron_job/run_log_to_ec2_tag_cron_job.py`` and ``cron_job/run_measure_worldserver_cron_job.py`` for GNU screen session.
- Removed the useless ``acorelocalmetry measure_worldserver`` CLI command.


0.1.1 (2024-07-29)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First release
- Add the following public APIs:
    - ``acore_server_monitoring_measurement.api.Ec2RdsStatusMeasurement``
    - ``acore_server_monitoring_measurement.api.WorldServerStatusMeasurement``
- Add the following CLI command:
    - ``acorelocalmetry measure_worldserver``
