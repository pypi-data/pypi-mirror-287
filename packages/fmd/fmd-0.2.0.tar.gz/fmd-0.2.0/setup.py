# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fmd', 'fmd.objs']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.32.3,<3.0.0']

setup_kwargs = {
    'name': 'fmd',
    'version': '0.2.0',
    'description': "Provides users with an easy-to-use interface to access data from the Financial Market Data (FMD) API, specializing in Taiwan's financial market.",
    'long_description': "# fmd\n\nProvides users with an easy-to-use interface to access data from the *Financial Market Data (FMD)* API, specializing in Taiwan's financial market.\n\n## Installation\n\nInstall via `pip`\n```\npip install fmd\n```\n\n## Quick Start\n\nRetrieve data through `FmdApi` with various predefined resources.\n```python\nfrom fmd import FmdApi\n\nfa = FmdApi()\nstock = fa.stock.get(symbol='2330')\ndata = stock.get_price()\n```\n",
    'author': 'Yu Chen, Yang',
    'author_email': 'ycy.tai@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ycytai/fmd',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
