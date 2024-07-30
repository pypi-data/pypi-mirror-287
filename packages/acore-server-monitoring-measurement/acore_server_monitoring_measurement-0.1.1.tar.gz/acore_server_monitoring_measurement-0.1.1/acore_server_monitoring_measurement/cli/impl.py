# -*- coding: utf-8 -*-

"""
CLI command business logic implementation.
"""

import pynamodb_mate.api as pm
from pathlib import Path
from acore_server_metadata.api import Server

from ..localmetry import (
    WorldServerStatusMeasurement as Base,
)
from ..paths import path_env_name_cache


if Path("/home/ubuntu").exists():
    try:
        env_name = path_env_name_cache.read_text()
    except FileNotFoundError:  # pragma: no cover
        server = Server.from_ec2_inside()
        env_name = server.env_name
        path_env_name_cache.write_text(env_name)
else:
    env_name = "sbx"


class WorldServerStatusMeasurement(Base):
    class Meta:
        table_name = f"wserver_infra-{env_name}-server_monitoring"
        region = "us-east-1"
        billing_mode = pm.constants.PAY_PER_REQUEST_BILLING_MODE


def measure_worldserver():
    """
    Measure worldserver status once.
    """
    WorldServerStatusMeasurement.measure_on_worldserver_ec2()
