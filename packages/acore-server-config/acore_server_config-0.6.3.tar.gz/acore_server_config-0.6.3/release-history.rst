.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.6.3 (2024-07-26)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Miscellaneous**

- Change the default config bucket name from ``{bsm.aws_account_id}-{bsm.aws_region}-artifacts`` to ``{bsm.aws_account_alias}-{bsm.aws_region}-artifacts``.


0.6.2 (2024-06-20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- Fix dependency.


(YANKED) 0.6.1 (2024-06-20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add the following config field:
    - ``db_engine_version``
    - ``db_admin_username``
- Add the following public API:
    - ``acore_server_config.api.Server.is_ready_for_create_new_server``
    - ``acore_server_config.api.Server.is_ready_for_create_cloned_server``
    - ``acore_server_config.api.Server.is_ready_for_create_updated_server``
    - ``acore_server_config.api.Server.is_ready_for_stop_server``
    - ``acore_server_config.api.Server.is_ready_for_start_server``
    - ``acore_server_config.api.Server.is_ready_for_delete_server``
    - ``acore_server_config.api.Env.server_black``
    - ``acore_server_config.api.Env.server_white``
    - ``acore_server_config.api.Env.server_yellow``
    - ``acore_server_config.api.Env.server_orange``

**Minor Improvements**

- Fix doc build.


0.5.2 (2024-06-16)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

- Add support for 3.11, 3.12
- Rework the documentation.

**Bugfixes**

- Fix a bug that caused by ``config_patterns<1.0.7``, bump config_pattern to 1.0.7+.


0.5.1 (2023-07-28)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add ``acore_config.config.define.server.Server.acore_db_app_version`` config field.


0.4.2 (2023-07-28)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Miscellaneous**

- upgrade dependencies, no API changes.
- improve internal implementation.


0.4.1 (2023-06-26)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- merge the following config field from ``wserver_fleet_manager`` project:
    - ``acore_config.config.define.server.Server.ec2_ami_id``
    - ``acore_config.config.define.server.Server.ec2_instance_type``
    - ``acore_config.config.define.server.Server.ec2_subnet_id``
    - ``acore_config.config.define.server.Server.ec2_key_name``
    - ``acore_config.config.define.server.Server.ec2_eip_allocation_id``
    - ``acore_config.config.define.server.Server.acore_soap_app_version``
    - ``acore_config.config.define.server.Server.acore_server_bootstrap_version``
    - ``acore_config.config.define.server.Server.db_snapshot_id``
    - ``acore_config.config.define.server.Server.db_instance_class``
    - ``acore_config.config.define.server.Server.lifecycle``


0.3.4 (2023-06-26)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- fix a bug that cannot detect it is a EC2 runtime when using ``sudo command``.


0.3.3 (2023-06-26)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Miscellaneous**

- upgrade dependencies, no API changes.


0.3.2 (2023-06-21)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Minor Improvements**

- add support to use this in AWS CodeBuild and AWS Lambda.


0.3.1 (2023-06-19)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Create two new API ``acore_server_config.api.Ec2ConfigLoader``, ``acore_server_config.api.ConfigLoader`` to replace ``acore_server_config.api.get_server``. The old api remains for backward compatibility until the next major release.


0.2.3 (2023-06-18)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- fix a parameter default value typo in ``acore_server_config.api.get_server`` API.


0.2.2 (2023-06-18)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- fix a bug that the key forget to pass ``parameter_name`` to ``Config.read`` method in ``acore_server_config.api.get_server`` API.


0.2.1 (2023-06-17)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add support to use AWS S3 as the backend
- Now AWS S3 is the default backend
- Add support to manage game server configuration (the ``*.conf`` file)


0.1.3 (2023-06-17)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- fix a bug that the key in ``env.servers[${key}]`` should be ``${server_name}``, but not ``${server_id}``.


0.1.2 (2023-06-17)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- fix a bug that the final AWS parameter name convention should be ``${parameter_name_prefix}${env_name}``, but not ``${parameter_name_prefix}-${env_name}``.


0.1.1 (2023-06-17)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First release
- Allow developer to deploy server configurations in batch to AWS parameter store.
- Allow EC2 instance to auto-discover its configuration from AWS parameter store.
- Add the following public api:
    - ``acore_server_config.api.IS_LOCAL``
    - ``acore_server_config.api.IS_GITHUB_CI``
    - ``acore_server_config.api.IS_EC2``
    - ``acore_server_config.api.IS_CODEBUILD_CI``
    - ``acore_server_config.api.EnvEnum``
    - ``acore_server_config.api.Env``
    - ``acore_server_config.api.Config``
    - ``acore_server_config.api.Server``
    - ``acore_server_config.api.get_server``
