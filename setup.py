from setuptools import setup

license = ''
long_description = ''

setup(
    name='twitch_cli',
    version='0.1',
    author='zxcvfrank',
    author_email='zxcvfrank@gmail.com',
    packages=['twitch_cli'],
    url='',
    license=license,
    description='Twitch API command line tools',
    test_suite='tests',
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'twitch_cli = twitch_cli.render:main',
        ]
    },
    install_requires=[
        'tabulate'
    ],
)