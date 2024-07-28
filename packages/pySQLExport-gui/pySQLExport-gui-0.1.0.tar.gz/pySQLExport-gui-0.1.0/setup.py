from setuptools import setup, find_packages

setup(
    name='pySQLExport-gui',
    version='0.1.0',
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
        'psycopg2-binary'
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
