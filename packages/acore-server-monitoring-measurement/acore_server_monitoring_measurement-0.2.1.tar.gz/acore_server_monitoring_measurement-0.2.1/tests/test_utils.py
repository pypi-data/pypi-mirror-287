# -*- coding: utf-8 -*-

from datetime import datetime
from acore_server_metadata.api import Server
from acore_server_monitoring_measurement.utils import (
    get_create_at_expire_at,
    get_server_status,
    every,
)


def test_get_create_at_expire_at():
    _, _ = get_create_at_expire_at()


def test_get_server_status():
    server = Server(id="sbx-blue")
    _ = get_server_status(server)


def test_every():
    counter = 0
    for _ in every(5):
        counter += 1
        now = datetime.now()
        assert now.second % 5 == 0
        if counter >= 4:
            break


if __name__ == "__main__":
    from acore_server_monitoring_measurement.tests import run_cov_test

    run_cov_test(__file__, "acore_server_monitoring_measurement.utils", preview=False)
