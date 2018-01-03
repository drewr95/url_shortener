import setuptools


setuptools.setup(
    name='urlshortener',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'urlshortener = urlshortener.cli.admin:cli',
        ],
    },
    install_requires=[
        'flask-sqlalchemy',
        'gitignoreio',
        'psycopg2',
        'sqlalchemy',
    ],
)
