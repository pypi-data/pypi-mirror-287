# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T
import os

import boto3
from simple_aws_ec2.api import EC2MetadataCache
from acore_server_metadata.api import Server
import acore_server_monitoring_core.api as acore_server_monitoring_core

from .utils import get_create_at_expire_at, get_server_status


class Ec2RdsStatusMeasurement(
    acore_server_monitoring_core.Ec2RdsStatusMeasurement,
):
    """
    todo: docstring
    """

    @classmethod
    def measure_on_outside(
        cls,
        server_id_list: T.List[str],
        boto_ses: boto3.session.Session,
    ):
        """
        Measure EC2 and RDS status outside the worldserver EC2 instance.

        This method can be reused in many runtime environments,
        such as AWS Lambda, EC2, GitHub Action CI, etc.
        """
        create_at, expire_at = get_create_at_expire_at()
        server = Server.batch_get_server(
            ids=server_id_list,
            ec2_client=boto_ses.client("ec2"),
            rds_client=boto_ses.client("rds"),
        )
        with cls.batch_write() as batch:
            for server_id, server in server.items():
                if server is None:
                    is_ec2_exists = None
                    is_rds_exists = None
                    is_ec2_running = None
                    is_rds_running = None
                    ec2_status = None
                    rds_status = None
                else:
                    (
                        is_ec2_exists,
                        is_rds_exists,
                        is_ec2_running,
                        is_rds_running,
                        ec2_status,
                        rds_status,
                    ) = get_server_status(server)

                measurement = Ec2RdsStatusMeasurement(
                    series_id=f"{server_id}-{acore_server_monitoring_core.UseCaseEnum.ec2_rds_status.value}",
                    create_at=create_at,
                    expire_at=expire_at,
                    is_ec2_exists=is_ec2_exists,
                    is_rds_exists=is_rds_exists,
                    is_ec2_running=is_ec2_running,
                    is_rds_running=is_rds_running,
                    ec2_status=ec2_status,
                    rds_status=rds_status,
                )
                batch.save(measurement)

    @classmethod
    def measure_on_lambda(
        cls,
        server_id_list: T.List[str],
    ):
        """
        Measure EC2 and RDS status on AWS Lambda.
        """
        boto_ses = boto3.session.Session(region_name=os.environ["AWS_DEFAULT_REGION"])
        cls.measure_on_outside(
            server_id_list=server_id_list,
            boto_ses=boto_ses,
        )

    @classmethod
    def measure_on_ec2(
        cls,
        server_id_list: T.List[str],
    ):
        """
        Measure EC2 and RDS status on another EC2 instance.
        """
        boto_ses = EC2MetadataCache.load().get_boto_ses_from_ec2_inside()
        cls.measure_on_outside(
            server_id_list=server_id_list,
            boto_ses=boto_ses,
        )

    @classmethod
    def measure_on_github_action(
        cls,
        server_id_list: T.List[str],
    ):
        """
        Measure EC2 and RDS status on GitHub Action CI.
        """
        raise NotImplementedError
