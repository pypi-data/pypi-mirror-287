"""
================================================================================
   Project: pySQLExport-gui
   Description: A PyQt6 GUI application for managing and exporting SQL query results.
   Author: Aaron
   Email: aaron.mathis@gmail.com
   License: GNU General Public License v3.0 (GPL-3.0)
   License URL: https://www.gnu.org/licenses/gpl-3.0.en.html
================================================================================

   This file is part of pySQLExport-gui.

   pySQLExport-gui is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   pySQLExport-gui is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with pySQLExport-gui. If not, see <https://www.gnu.org/licenses/>.

================================================================================
"""

from setuptools import setup, find_packages

setup(
    name='pySQLExport-gui',
    version='1.0',
    author='Aaron Mathis',
    author_email='aaron.mathis@gmail.com',
    description='A GUI application for exporting SQL query results into csv, json, xml, html, excel, and muck more.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/pySQLExport-gui',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'PyQt6',
        'mysql-connector-python',
        'pandas',
        'psycopg2-binary',
        "fastparquet",
        "numpy",
        "tables"
    ],
    entry_points={
        'console_scripts': [
            'pySQLExport-gui=pySQLExport_gui.__main__:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
