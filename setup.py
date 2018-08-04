from setuptools import setup, find_packages


setup(
    name='mcdashboard',
    version='1.0',
    install_requires=[
        'bcrypt',
        'flask_assets',
        'jsmin',
        'flask',
        'docker',
        'wtforms'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
        ]
    }
)
