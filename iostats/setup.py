from setuptools import setup

setup(
    name='otf2_iostat',
    version='0.1',
    py_modules=['nio_ops'],
    install_requires=[
        'intervaltree',
        'six',
        'future',
    ],
    entry_points='''
        [console_scripts]
        otf2_iostat=otf2_iostats
    ''',
)