# -*- coding: utf-8 -*-

import os
from s3pathlib import context
from boto_session_manager import BotoSesManager
from simple_aws_ec2.api import EC2MetadataCache


from .runtime import (
    IS_LOCAL,
    IS_GITHUB_CI,
    IS_EC2,
    IS_CODEBUILD_CI,
    IS_LAMBDA,
    IS_BATCH,
    IS_FARGATE,
    IS_READTHEDOCS,
)

# environment aware boto session manager
if IS_LOCAL:  # put production first
    bsm = BotoSesManager(
        profile_name="bmt_app_dev_us_east_1",
        region_name="us-east-1",  # hard coded region, because we know what we are doing
    )
elif IS_GITHUB_CI:
    bsm = BotoSesManager(
        region_name="us-east-1",  # hard coded region, because we know what we are doing
    )
elif IS_EC2:
    bsm = BotoSesManager(
        region_name=EC2MetadataCache.load().get_region(),
    )
elif IS_CODEBUILD_CI:
    bsm = BotoSesManager(
        region_name=os.environ["AWS_REGION"],
    )
elif IS_LAMBDA:
    bsm = BotoSesManager(
        region_name=os.environ["AWS_DEFAULT_REGION"],
    )
elif IS_BATCH or IS_FARGATE:
    raise NotImplementedError
elif IS_READTHEDOCS:
    bsm = None
else:  # pragma: no cover
    raise NotImplementedError

if IS_READTHEDOCS:
    pass
else:
    context.attach_boto_session(boto_ses=bsm.boto_ses)
