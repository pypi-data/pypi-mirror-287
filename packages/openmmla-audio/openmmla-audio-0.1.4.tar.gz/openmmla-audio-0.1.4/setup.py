import os
import subprocess
from pathlib import Path

from setuptools import setup
from setuptools.command.install import install

NAME = 'openmmla-audio'
DESCRIPTION = 'Audio module for OpenMMLA platform, including data collection, data processing, and data analytics.'

URL = 'https://github.com/ucph-ccs/mbox-audio'
EMAIL = 'lizaibeim@gmail.com'
AUTHOR = 'Zaibei Li'
REQUIRES_PYTHON = '>=3.9.0'
VERSION = "0.1.4"

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
    'PyAudio>=0.2.14',
    'influxdb-client==1.44.0',
    'jiwer==3.0.4',
    'librosa==0.10.2.post1',
    'llvmlite==0.43.0',
    'matplotlib==3.9.1',
    'networkx==3.3',
    'paho-mqtt== 2.1.0',
    'pydub==0.25.1',
    'pyecharts==2.0.6',
    'redis==5.0.7',
]

extras_require = {
    'server': [
        'nemo-toolkit[asr]<=1.23.0',
        'modelscope[framework]==1.16.1',
        'denoiser-compat==0.1.5.dev0',
        'googletrans==3.0.0',
        'onnxruntime==1.18.1',
        'openai-whisper==20231117',
        'transformers==4.33.3',
        'speechbrain==1.0.0',
        'rotary-embedding-torch==0.6.4',
        'gunicorn==22.0.0',
        'flask==3.0.3',
        'pandas==2.2.2',
        'gevent==24.2.1',
        'huggingface_hub==0.23.5',
    ]
}

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
    packages=['openmmla_audio', 'openmmla_audio/services', 'openmmla_audio/utils', 'openmmla_audio/base',
              'openmmla_audio/silero-vad', 'openmmla_audio/silero-vad/files'],
    install_requires=install_requires,
    extras_require=extras_require,
    include_package_data=True,
    license='MIT License',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
        'Topic :: Education :: Computer Aided Instruction (CAI)',
    ],
    cmdclass={
        'install': CustomInstallCommand,
    }
)
