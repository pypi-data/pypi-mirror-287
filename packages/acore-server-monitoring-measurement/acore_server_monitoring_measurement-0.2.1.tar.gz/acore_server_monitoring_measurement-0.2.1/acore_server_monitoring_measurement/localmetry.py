# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import psutil
from acore_server_metadata.api import Server
from acore_soap.api import gm
import acore_server_monitoring_core.api as acore_server_monitoring_core

from .utils import get_create_at_expire_at, get_server_status


class WorldServerStatusMeasurement(
    acore_server_monitoring_core.WorldServerStatusMeasurement,
):
    """
    todo: docstring
    """

    @classmethod
    def measure_on_worldserver_ec2(
        cls,
        save: bool = True,
    ):
        """
        todo: docstring
        """
        create_at, expire_at = get_create_at_expire_at()
        server = Server.from_ec2_inside()
        (
            is_ec2_exists,
            is_rds_exists,
            is_ec2_running,
            is_rds_running,
            ec2_status,
            rds_status,
        ) = get_server_status(server)

        try:
            soap_response = gm.ServerInfoRequest().send()
            server_info_response = gm.ServerInfoResponse.from_soap_response(
                soap_response
            )
            connected_players = server_info_response.connected_players
            characters_in_world = server_info_response.characters_in_world
            server_uptime = server_info_response.server_uptime
        except Exception:
            connected_players = None
            characters_in_world = None
            server_uptime = None

        cpu_usage = psutil.cpu_percent(interval=1)
        virtual_memory = psutil.virtual_memory()
        memory_usage = virtual_memory.percent
        total_memory = int(virtual_memory.total / 1000000)
        available_memory = int(virtual_memory.available / 1000000)

        measurement = cls(
            series_id=f"{server.id}-{acore_server_monitoring_core.UseCaseEnum.worldserver_status.value}",
            create_at=create_at,
            expire_at=expire_at,
            is_ec2_exists=is_ec2_exists,
            is_rds_exists=is_rds_exists,
            is_ec2_running=is_ec2_running,
            is_rds_running=is_rds_running,
            ec2_status=ec2_status,
            rds_status=rds_status,
            connected_players=connected_players,
            characters_in_world=characters_in_world,
            server_uptime=server_uptime,
            cpu_usage=cpu_usage,
            memory_usage=memory_usage,
            total_memory=total_memory,
            available_memory=available_memory,
        )
        if save:
            measurement.save()
        return measurement
