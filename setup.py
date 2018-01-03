import setuptools


setuptools.setup(
    name='urlshortener',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            (
                'urlshortener_update_gitignore'
                '= urlshortener.cli.updategitignore:cli'
                '[gitignore]'
            ),
        ],
    },
    install_requires=[
        'gitignoreio',
    ],
)
