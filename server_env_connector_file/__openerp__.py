# -*- coding: utf-8 -*-
#
#
#    Authors: Guewen Baconnier
#    Copyright 2015 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

{'name': 'Server environment for Connector File',
 'version': '1.0',
 'author': "Camptocamp",
 'maintainer': 'Camptocamp',
 'license': 'AGPL-3',
 'category': 'Tools',
 'complexity': 'expert',
 'depends': ['server_environment',
             'connector_file',
             ],
 'description': """
Server environment for Connector File
=====================================

This module is based on the `server_environment` module to use files for
configuration.  Thus we can have a different configuration for each
environment (dev, test, prod, ...).  This module defines the configuration
variables for the `connector_file` module.

In the configuration file, you can configure the ftp host, login and
password of the Connector File Backends.

Example of the section to put in the configuration file::

    [file_import_backend.name_of_the_backend]
    ftp_host = localhost
    ftp_user = my_ftp_user
    ftp_password = my_ftp_password

`server_environment` is in https://github.com/OCA/server-tools

""",
 'website': 'http://www.camptocamp.com',
 'data': [],
 'test': [],
 'installable': True,
 'auto_install': False,
 }
