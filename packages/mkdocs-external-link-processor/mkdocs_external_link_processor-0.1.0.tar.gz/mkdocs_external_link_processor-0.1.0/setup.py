from setuptools import setup, find_packages

setup(
    name='mkdocs-external-link-processor',
    version='0.1.0',
    description='A MkDocs plugin that adds a CSS attributes to external links',
    author='Raistlin Wolfe',
    author_email='jdoonan61@gmail.com',
    url='https://github.com/StellarWolfEntertainment/mkdocs-external-link-processor',
    packages=find_packages(),
    install_requires=[
        'mkdocs>=1.4.0',
        'beautifulsoup4>=4.9.0'
    ],
    entry_points={
        'mkdocs.plugins': [
            'mkdocs_external_link_processor=mkdocs_external_link_processor.mkdocs_external_link_processor:MkdocsExternalLinkProcessor',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)