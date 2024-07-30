# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['maeser',
 'maeser.chat',
 'maeser.controllers',
 'maeser.controllers.common',
 'maeser.graphs']

package_data = \
{'': ['*'],
 'maeser': ['data/static/*',
            'data/static/bootstrap-icons/*',
            'data/static/bootstrap-icons/font/*',
            'data/static/bootstrap-icons/font/fonts/*',
            'data/templates/*']}

install_requires = \
['faiss-cpu>=1.8.0.post1,<2.0.0',
 'flask-login>=0.6.3,<0.7.0',
 'flask>=3.0.3,<4.0.0',
 'langchain-text-splitters>=0.2.2,<0.3.0',
 'langchain>=0.2.8,<0.3.0',
 'langchain_community>=0.2.7,<0.3.0',
 'langchain_core>=0.2.19,<0.3.0',
 'langchain_openai>=0.1.16,<0.2.0',
 'langgraph>=0.1.8,<0.2.0',
 'markdown>=3.6,<4.0',
 'markdownify>=0.13.1,<0.14.0',
 'pyYAML>=6.0.1,<7.0.0',
 'pymdown-extensions>=10.8.1,<11.0.0',
 'ragas>=0.1.10,<0.2.0',
 'requests>=2.32.3,<3.0.0']

extras_require = \
{'gpu': ['faiss-gpu>=1.8.0.post1,<2.0.0']}

setup_kwargs = {
    'name': 'maeser',
    'version': '0.0.1',
    'description': 'A package for building RAG chatbot applications for educational contexts.',
    'long_description': None,
    'author': 'Carson Bush',
    'author_email': 'hyperdriveguy@byui.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
