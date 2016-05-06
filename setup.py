from __future__ import unicode_literals

from setuptools import setup, find_packages

setup(
        name='xddos',
        url='https://github.com/servancho/xddos',
        description='XDDoS - DDoS protection system',
        keywords='ddos protection nginx web',
        version='1.1.16',
        author='Dmitry Shilyaev',
        author_email='dima@justhost.ru',
        license='MIT',
        zip_safe=True,
        install_requires=['argparse'],
        packages=find_packages(exclude=['tests']),
        scripts=['xddos.py'],

        data_files=[
            ('/usr/share/xddos',
             ['deps/tlog.sh',
              'deps/logrotate.d.xddos', 'deps/cron',
              'deps/runner.sh', 'deps/enable.sh', 'deps/disable.sh'])],

        entry_points={
            'console_scripts': [
                'xddos=xddos:main',
            ],
        },
)
