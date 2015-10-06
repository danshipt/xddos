from setuptools import setup, find_packages

setup(
    name='anti-ddos',
    version='1.0b1',
    author='Dmitry Shilyaev',
    author_email='dima@justhost.ru',
    license='MIT',
    url='https://github.com/servancho/pytin',

    packages=find_packages(exclude=['tests.*', 'ddos.egg-info']),
    scripts=['http_protector.py'],

    zip_safe=True
)
