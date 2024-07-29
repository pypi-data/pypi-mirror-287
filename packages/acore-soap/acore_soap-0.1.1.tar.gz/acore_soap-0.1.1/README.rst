
.. image:: https://readthedocs.org/projects/acore-soap/badge/?version=latest
    :target: https://acore-soap.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/acore_soap-project/actions/workflows/main.yml/badge.svg
    :target: https://github.com/MacHu-GWU/acore_soap-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/acore_soap-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/acore_soap-project

.. image:: https://img.shields.io/pypi/v/acore-soap.svg
    :target: https://pypi.python.org/pypi/acore-soap

.. image:: https://img.shields.io/pypi/l/acore-soap.svg
    :target: https://pypi.python.org/pypi/acore-soap

.. image:: https://img.shields.io/pypi/pyversions/acore-soap.svg
    :target: https://pypi.python.org/pypi/acore-soap

.. image:: https://img.shields.io/badge/Release_History!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/acore_soap-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/acore_soap-project

------

.. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://acore-soap.readthedocs.io/en/latest/

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://acore-soap.readthedocs.io/en/latest/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/acore_soap-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/acore_soap-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/acore_soap-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/acore-soap#files


Welcome to ``acore_soap`` Documentation
==============================================================================
.. image:: https://acore-soap.readthedocs.io/en/latest/_static/acore_soap-logo.png
    :target: https://acore-soap.readthedocs.io/en/latest/

`azerothcore 魔兽世界服务器 <https://www.azerothcore.org/>`_ 自带一个类似于 Terminal 的交互式 Console. GM 可以在里面输入命令来创建账号, 修改密码, 封禁账号等, 例如 ``.account create $account $password``. 你如果用 GM 账号登录游戏客户端, 你也可以在游戏内聊天框输入 GM 命令, 本质是一样的.

如果你希望像操作 Rest API 一样的远程执行命令, 以上两种方法就不太实用了. 一种你需要 SSH 到服务器上才能接触到 console, 一种你需要登录游戏客户端, 而客户端是没有我们需要的变成接口的. 而这种需求对于服务器维护者来说又是实实在在的. 例如服务器可能有一个官网, 让会员用户可以在网站上点击购买物品后, 游戏服务器就自动运行一条 GM 命令将物品发送到用户游戏角色的邮箱. 在这个例子里 GM 命令的发起端是 Web 服务器, 而运维的时候 GM 命令的发起端可以是任何东西, 例如 VM, Container, Lambda Function 等. 所以我们就需要一套机制能仅让有权限的人或机器远程执行 GM 命令. 这个需求对于长期的正式运营非常重要.

我创造了一整套工具用于实现这个需求. 其中这个 ``acore_soap`` 项目是这一整套工具的基石. 在应用层, 它提供了一套 Pythonic 的 API 用参数化的方式发送 GM 命令, 并将返回的信息解析成机器友好的 Python 对象. 在底层, 它提供了一套 ``SOAPRequest`` 和 ``SOAPResponse`` 的抽象, 实现了发送 command 和获取 response message 的核心逻辑. 你可以用这个基石来构建更高级的应用, 例如一个 Web 服务器, 一个 Discord Bot 等等.


.. _install:

Install
------------------------------------------------------------------------------

``acore_soap`` is released on PyPI, so all you need is to:

.. code-block:: console

    $ pip install acore-soap

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade acore-soap
