from setuptools import setup, find_packages

setup(
    name='xddos',
    version='1.0b2',
    author='Dmitry Shilyaev',
    author_email='dima@justhost.ru',
    license='MIT',
    url='https://github.com/servancho/xddos',

    install_requires=['argparse'],

    packages=find_packages(exclude=['tests.*', 'ddos.egg-info']),
    scripts=['xddos.py'],

    zip_safe=True
)
