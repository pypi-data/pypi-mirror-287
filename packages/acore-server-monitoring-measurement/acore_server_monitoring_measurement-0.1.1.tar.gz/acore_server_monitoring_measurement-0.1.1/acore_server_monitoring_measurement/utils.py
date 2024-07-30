# -*- coding: utf-8 -*-

import typing as T
from datetime import datetime, timezone, timedelta

from acore_server_metadata.api import Server

from .constants import EXPIRE_IN_HOURS


def get_utc_now() -> datetime:
    return datetime.utcnow().replace(tzinfo=timezone.utc)


def get_create_at_expire_at() -> T.Tuple[datetime, datetime]:
    create_at = get_utc_now()
    expire_at = create_at + timedelta(hours=EXPIRE_IN_HOURS)
    return create_at, expire_at


def get_server_status(
    server: Server,
) -> T.Tuple[
    bool,
    bool,
    bool,
    bool,
    T.Optional[str],
    T.Optional[str],
]:
    is_ec2_exists = server.is_ec2_exists()
    is_rds_exists = server.is_rds_exists()
    is_ec2_running = server.is_ec2_running()
    is_rds_running = server.is_rds_running()
    if is_ec2_running:
        ec2_status = server.ec2_inst.status
    else:
        ec2_status = None
    if is_rds_running:
        rds_status = server.rds_inst.status
    else:
        rds_status = None
    return (
        is_ec2_exists,
        is_rds_exists,
        is_ec2_running,
        is_rds_running,
        ec2_status,
        rds_status,
    )
