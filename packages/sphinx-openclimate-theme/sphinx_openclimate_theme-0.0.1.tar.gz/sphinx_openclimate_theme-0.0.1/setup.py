# -*- coding: utf-8 -*-
"""`sphinx_openclimate_theme` lives on `Github`_.

.. _github: https://github.com/open-climate/sphinx_openclimate_theme

"""
from io import open
from setuptools import setup
#import versioneer

setup(
    name='sphinx_openclimate_theme',
#    version=versioneer.get_version(),
#    cmdclass=versioneer.get_cmdclass(),
    version='0.0.1',
    url='https://github.com/open-climate/sphinx_openclimate_theme/',
    license='MIT',
    author='Ian Edwards',
    author_email='ian@myacorn.com',
    description='openclimte theme for Sphinx',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    zip_safe=False,
    packages=['sphinx_openclimate_theme'],
    package_data={'sphinx_openclimte_theme': [
        'theme.conf',
        '*.html',
        'static/*.css',
        'static/*.otf',
        'static/*.png'
    ]},
    include_package_data=True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points = {
        'sphinx.html_themes': [
            'openclimate = sphinx_openclimate_theme',
        ]
    },
    install_requires=[
       'sphinx', 'sphinx_bootstrap_theme'
    ],
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
