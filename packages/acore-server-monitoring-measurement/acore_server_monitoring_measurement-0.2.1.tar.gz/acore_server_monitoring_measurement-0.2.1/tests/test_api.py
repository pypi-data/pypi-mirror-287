# -*- coding: utf-8 -*-

from acore_server_monitoring_measurement import api


def test():
    _ = api
    _ = api.Ec2RdsStatusMeasurement
    _ = api.WorldServerStatusMeasurement


if __name__ == "__main__":
    from acore_server_monitoring_measurement.tests import run_cov_test

    run_cov_test(__file__, "acore_server_monitoring_measurement.api", preview=False)
