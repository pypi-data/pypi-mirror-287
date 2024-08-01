# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'XDGMM'}

packages = \
['tcup', 'tcup.stan', 'tcup.stan.src', 'xdgmm', 'xdgmm.tests']

package_data = \
{'': ['*']}

install_requires = \
['arviz>=0.19.0,<0.20.0',
 'astroml>=1.0.2.post1,<2.0.0',
 'astropy-iers-data>=0.2024.7.22.0.34.13,<0.2025.0.0.0.0.0',
 'astropy>=6.1.2,<7.0.0',
 'jax>=0.4.23,<0.5.0',
 'numpy>=1.26.3,<2.0.0',
 'numpyro>=0.13.2,<0.14.0',
 'pyerfa>=2.0.1.4,<3.0.0.0',
 'scikit-learn>=1.5.1,<2.0.0',
 'tensorflow-probability[jax]>=0.19.0,<0.20.0']

extras_require = \
{'stan': ['jinja2>=3.1.2,<4.0.0', 'pystan>=3.6.0,<4.0.0']}

setup_kwargs = {
    'name': 'tcup',
    'version': '0.7.0',
    'description': '',
    'long_description': '# t-cup - robust linear regression\n\nThis package presents a statistical model for robust linear regression where\nboth independent and dependent variables are measured with measurement error.\n\nThis code is bundled with [XDGMM](https://github.com/tholoien/XDGMM), a Python\npackage implementing the [extreme deconvolution algorithm]\n(https://arxiv.org/abs/0905.2979).\n',
    'author': 'William Martin',
    'author_email': '30499074+wm1995@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
