# Copyright (C) 2016 SYLEAM (<http://www.syleam.fr>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from setuptools import setup

setup(
    name='odoo-sentinel',
    version='1.0',
    author='Sylvain Garancher',
    author_email='sylvain.garancher@syleam.fr',
    packages=['odoosentinel'],
    package_data={'odoosentinel': ['i18n/*/LC_MESSAGES/*.mo']},
    requires=[
        'odoorpc',
    ],
    install_requires=[
        'odoorpc',
    ],
    entry_points={
        'console_scripts': [
            'odoo-sentinel = odoosentinel:main',
        ],
    },
    license='LICENSE.txt',
    description='Odoo custom ncurses client for the stock_scanner module',
    long_description=open('README.txt').read(),
)
