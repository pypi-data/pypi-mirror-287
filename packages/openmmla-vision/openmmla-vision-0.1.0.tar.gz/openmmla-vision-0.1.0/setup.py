import os
import subprocess
from pathlib import Path

from setuptools import setup
from setuptools.command.install import install

NAME = 'openmmla-vision'
DESCRIPTION = 'Vision module for the OpenMMLA platform.'

URL = 'https://github.com/ucph-ccs/mbox-audio'
EMAIL = 'lizaibeim@gmail.com'
AUTHOR = 'Zaibei Li'
REQUIRES_PYTHON = '>=3.9.0'
VERSION = "0.1.0"

HERE = Path(__file__).parent

try:
    with open(HERE / "README.md", encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


def execute_script(script_name):
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    if os.path.exists(script_path):
        print(f"Executing {script_name} script...")
        try:
            subprocess.check_call(['bash', script_path])
        except subprocess.CalledProcessError as e:
            print(f"Failed to execute {script_name}: {str(e)}")
    else:
        print(f"{script_name} script not found.")


class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        execute_script('reset.sh')


# Package and dependency configuration
install_requires = [
    'influxdb-client==1.44.0',
    'matplotlib==3.9.1',
    'opencv-python==4.10.0.84',
    'paho-mqtt==2.1.0',
    'pandas==2.2.2',
    'pupil_apriltags==1.0.4.post10',
    'redis==5.0.7',
    'scipy==1.14.0',
    'networkx==3.3',
    'pyecharts==2.0.6',
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=['openmmla_vision', 'openmmla_vision/services', 'openmmla_vision/utils', 'openmmla_vision/bases'],
    install_requires=install_requires,
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Topic :: Multimedia :: Video :: Capture',
        'Topic :: Education :: Computer Aided Instruction (CAI)',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
    ],
    cmdclass={
        'install': CustomInstallCommand,
    }
)
