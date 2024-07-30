
.. image:: https://readthedocs.org/projects/acore-server-monitoring-measurement/badge/?version=latest
    :target: https://acore-server-monitoring-measurement.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/acore_server_monitoring_measurement-project/actions/workflows/main.yml/badge.svg
    :target: https://github.com/MacHu-GWU/acore_server_monitoring_measurement-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/acore_server_monitoring_measurement-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/acore_server_monitoring_measurement-project

.. image:: https://img.shields.io/pypi/v/acore-server-monitoring-measurement.svg
    :target: https://pypi.python.org/pypi/acore-server-monitoring-measurement

.. image:: https://img.shields.io/pypi/l/acore-server-monitoring-measurement.svg
    :target: https://pypi.python.org/pypi/acore-server-monitoring-measurement

.. image:: https://img.shields.io/pypi/pyversions/acore-server-monitoring-measurement.svg
    :target: https://pypi.python.org/pypi/acore-server-monitoring-measurement

.. image:: https://img.shields.io/badge/Release_History!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/acore_server_monitoring_measurement-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/acore_server_monitoring_measurement-project

------

.. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://acore-server-monitoring-measurement.readthedocs.io/en/latest/

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://acore-server-monitoring-measurement.readthedocs.io/en/latest/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/acore_server_monitoring_measurement-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/acore_server_monitoring_measurement-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/acore_server_monitoring_measurement-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/acore-server-monitoring-measurement#files


Welcome to ``acore_server_monitoring_measurement`` Documentation
==============================================================================
.. image:: https://acore-server-monitoring-measurement.readthedocs.io/en/latest/_static/acore_server_monitoring_measurement-logo.png
    :target: https://acore-server-monitoring-measurement.readthedocs.io/en/latest/

这个 Python 库提供了对服务器监控数据的采集功能. 它有两种模式:

- telemetry: 遥测. 可以从任何地方采集监控数据. 通常是把采集监控数据的代码放在 Lambda Function 上, 然后每 5 分钟运行一次既可.
- localmetry: 本地监控数据采集, 需要将这个库安装在 EC2 游戏服务器 上, 然后的用 GNU Screen 将一个每 5 分钟采集一次数据的脚本放在后台运行既可实现监控数据的采集.


.. _install:

Install
------------------------------------------------------------------------------
``acore_server_monitoring_measurement`` is released on PyPI, so all you need is to:

.. code-block:: console

    $ pip install acore-server-monitoring-measurement

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade acore-server-monitoring-measurement
