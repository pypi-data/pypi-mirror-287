# -*- coding: utf-8 -*-

"""
Implement Cron job running on worldserver EC2 instance.
"""

from pathlib import Path

import pynamodb_mate.api as pm
from simple_aws_ec2.api import EC2MetadataCache
from acore_constants.api import TagKey
from acore_server_metadata.api import Server

from .utils import every
from .paths import path_env_name_cache
from .localmetry import WorldServerStatusMeasurement as Base


def ensure_ec2_environment():  # pragma: no cover
    """
    Ensure all functions in this module is running inside EC2 environment.
    """
    if (
        Path("/home/ubuntu").exists()
        and Path(
            "/home/ubuntu/git_repos/acore_server_monitoring_measurement-project/acore_server_monitoring_measurement/cron_job.py"
        ).exists()
    ):
        pass
    else:
        raise EnvironmentError("You cannot run this outside of EC2 environment")


def get_env_name() -> str:
    try:
        env_name = path_env_name_cache.read_text()
    except FileNotFoundError:  # pragma: no cover
        server = Server.from_ec2_inside()
        env_name = server.env_name
        path_env_name_cache.write_text(env_name)
    return env_name


def run_measure_worldserver_cron_job(
    delay: int = 300,
    verbose: bool = True,
):
    """
    Measure the worldserver status every 5 minutes.
    """
    if delay % 60 != 0:
        raise ValueError("delay must be a multiple of 60")

    ensure_ec2_environment()

    env_name = get_env_name()

    class WorldServerStatusMeasurement(Base):
        class Meta:
            table_name = f"wserver_infra-{env_name}-server_monitoring"
            region = "us-east-1"
            billing_mode = pm.constants.PAY_PER_REQUEST_BILLING_MODE

    for _ in every(seconds=delay, verbose=verbose):
        WorldServerStatusMeasurement.measure_on_worldserver_ec2()


def run_log_to_ec2_tag_cron_job(
    delay: int = 60,
    verbose: bool = True,
):
    """
    Put worldserver status measurement to EC2 tags every 1 minutes.
    """
    if delay % 60 != 0:
        raise ValueError("delay must be a multiple of 60")

    ensure_ec2_environment()

    WorldServerStatusMeasurement = Base

    for _ in every(seconds=delay, verbose=verbose):
        measurement = WorldServerStatusMeasurement.measure_on_worldserver_ec2(
            save=False
        )
        tags = {
            TagKey.WORLDSERVER_MEASURE_TIME: measurement.create_at.isoformat(),
            TagKey.WORLDSERVER_IS_RDS_EXISTS: str(measurement.is_rds_exists),
            TagKey.WORLDSERVER_IS_RDS_RUNNING: str(measurement.is_rds_running),
            TagKey.WORLDSERVER_RDS_STATUS: str(measurement.rds_status),
            TagKey.WORLDSERVER_CONNECTED_PLAYERS: str(measurement.connected_players),
            TagKey.WORLDSERVER_CHARACTERS_IN_WORLD: str(
                measurement.characters_in_world
            ),
            TagKey.WORLDSERVER_SERVER_UPTIME: str(measurement.server_uptime),
            TagKey.WORLDSERVER_CPU_USAGE: str(measurement.cpu_usage),
            TagKey.WORLDSERVER_MEMORY_USAGE: str(measurement.memory_usage),
            TagKey.WORLDSERVER_TOTAL_MEMORY: str(measurement.total_memory),
            TagKey.WORLDSERVER_AVAILABLE_MEMORY: str(measurement.available_memory),
        }
        ec2_metadata_cache = EC2MetadataCache.load()
        instance_id = ec2_metadata_cache.get_instance_id()
        boto_ses = ec2_metadata_cache.get_boto_ses_from_ec2_inside()
        ec2_client = boto_ses.client("ec2")
        ec2_client.create_tags(
            Resources=[instance_id],
            Tags=[dict(Key=k, Value=v) for k, v in tags.items()],
        )
