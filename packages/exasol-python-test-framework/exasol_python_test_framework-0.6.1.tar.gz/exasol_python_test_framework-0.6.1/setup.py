# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['exasol_python_test_framework',
 'exasol_python_test_framework.docker_db_environment',
 'exasol_python_test_framework.exatest',
 'exasol_python_test_framework.exatest.clients',
 'exasol_python_test_framework.exatest.servers',
 'exasol_python_test_framework.exatest.test',
 'exasol_python_test_framework.performance',
 'exasol_python_test_framework.udf']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.26',
 'pyftpdlib>=1.5.6',
 'pyodbc>=5.1.0,<6.0.0',
 'scipy>=1.13.0,<2.0.0']

extras_require = \
{':sys_platform != "win32"': ['docker>=5.0.3']}

setup_kwargs = {
    'name': 'exasol-python-test-framework',
    'version': '0.6.1',
    'description': 'Python Test framework for Exasol database tests',
    'long_description': '# Exasol Python Test Framework\n\n## About\n\nThis project is shared among other Exasol projects, and provides a test framework to execute integration tests on the database. \n\n\n## Prerequisites\n\n* Linux, macOS\n* Python3.10 and later\n\n### On Linux\n\n * providers (packages) of unixodbc and unixodbc-development artifacts\n\n',
    'author': 'Exasol AG',
    'author_email': 'opensource@exasol.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/exasol/exasol-python-test-framework',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<3.12',
}


setup(**setup_kwargs)
