
.. image:: https://readthedocs.org/projects/acore-server/badge/?version=latest
    :target: https://acore-server.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/acore_server-project/actions/workflows/main.yml/badge.svg
    :target: https://github.com/MacHu-GWU/acore_server-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/acore_server-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/acore_server-project

.. image:: https://img.shields.io/pypi/v/acore-server.svg
    :target: https://pypi.python.org/pypi/acore-server

.. image:: https://img.shields.io/pypi/l/acore-server.svg
    :target: https://pypi.python.org/pypi/acore-server

.. image:: https://img.shields.io/pypi/pyversions/acore-server.svg
    :target: https://pypi.python.org/pypi/acore-server

.. image:: https://img.shields.io/badge/Release_History!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/acore_server-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/acore_server-project

.. image:: https://img.shields.io/badge/Acore_Doc--None.svg?style=social&logo=readthedocs
    :target: https://acore-doc.readthedocs.io/en/latest/

------

.. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://acore-server.readthedocs.io/en/latest/

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://acore-server.readthedocs.io/en/latest/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/acore_server-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/acore_server-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/acore_server-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/acore-server#files


Welcome to ``acore_server`` Documentation
==============================================================================
.. image:: https://acore-server.readthedocs.io/en/latest/_static/acore_server-logo.png
    :target: https://acore-server.readthedocs.io/en/latest/

**项目背景**

一个魔兽世界服务器由一个 EC2 游戏服务器 和一个 RDS DB Instance 数据库组成. 其中游戏服务器和数据库的配置信息, 例如账号密码, 机器的 CPU 内存大小, 都由 `acore_server_metadata <https://github.com/MacHu-GWU/acore_server_metadata-project>`_ 这个库管理. 而对于 EC2 和 RDS 的 metadata, 例如 IP 地址, host, 在线状态, 以及对其进行创建, 启动, 停止, 删除等操作则是由 `acore_server_config <https://github.com/MacHu-GWU/acore_server_config-project>`_ 这个库管理. 要想远程运行 GM 命令, 则需要用到 `acore_soap_app <https://github.com/MacHu-GWU/acore_soap_app-project>`_ 这个库. 要想在本地进行数据库应用开发, 则需要用到 `acore_db_ssh_tunnel <https://github.com/MacHu-GWU/acore_db_ssh_tunnel-project>`_ 这个库.

本项目则是将以上四个库整合到一起, 用 ``acore_server.api.Server`` 作为一个统一的入口, 以便于在一个项目中同时使用以上四个库. 并且在对这些子库的 API 调用进行了封装, 将跟 Server 相关的参数都封装起来, 使得我们可以用最少的参数, 方便地调用这些子库的 API.


.. _install:

Install
------------------------------------------------------------------------------

``acore_server`` is released on PyPI, so all you need is to:

.. code-block:: console

    $ pip install acore-server

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade acore-server
