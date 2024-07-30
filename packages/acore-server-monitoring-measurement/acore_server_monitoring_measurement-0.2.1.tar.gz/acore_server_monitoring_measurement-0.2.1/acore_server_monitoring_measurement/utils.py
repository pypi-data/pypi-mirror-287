# -*- coding: utf-8 -*-

import typing as T
import time
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


START = get_utc_now().replace(hour=0, minute=0, second=0, microsecond=0)


def run():
    print(f"{datetime.now()}")


def every(
    seconds: int,
    verbose: bool = True,
):
    """
    Execute tasks at precise N-second intervals, aligned with the clock.
    The script runs at exact multiples of N seconds past the minute,
    ensuring consistent timing. For instance, with N=30, executions occur at
    :00 and :30 of each minute (e.g., 08:10:00, 08:10:30, 08:11:00)

    Usage example::

        for _ in every(30):
            # do something
    """
    while 1:
        elapsed = int((get_utc_now() - START).total_seconds() * 1000)
        div, mod = divmod(elapsed, seconds * 1000)
        wait_secs = (seconds * 1000 - mod) / 1000
        if verbose:
            until_time = START + timedelta(seconds=(div + 1) * seconds)
            print(
                f"\rwait {wait_secs} seconds till {until_time.isoformat()} for the next run ...",
                end="",
                flush=True,
            )
        time.sleep(wait_secs)
        yield
