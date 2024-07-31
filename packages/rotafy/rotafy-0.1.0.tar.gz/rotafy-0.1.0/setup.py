# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rotafy', 'rotafy.api', 'rotafy.config', 'rotafy.rota']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.7,<9.0.0',
 'clicksend-client>=5.0.78,<6.0.0',
 'jinja2>=3.1.4,<4.0.0',
 'matplotlib>=3.9.0,<4.0.0',
 'pandas>=2.2.2,<3.0.0',
 'python-dateutil>=2.9.0.post0,<3.0.0',
 'recurrent>=0.4.1,<0.5.0',
 'retry>=0.9.2,<0.10.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['rotafy = rotafy.cli:cli']}

setup_kwargs = {
    'name': 'rotafy',
    'version': '0.1.0',
    'description': 'Build, update, and delegate a rota/roster of chores, notifying individuals when their scheduled task is upcoming',
    'long_description': '# rotafy\nBuild, update, and delegate a rota/roster of chores, notifying individuals when their scheduled task is upcoming\n\n## Contributing\n\nRun `pre-commit install`.',
    'author': 'Ryan McKeown',
    'author_email': 'ryanmckeown@mail4me.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
