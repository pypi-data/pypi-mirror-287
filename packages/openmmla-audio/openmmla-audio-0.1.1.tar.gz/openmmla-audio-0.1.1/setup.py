import os
import subprocess
from pathlib import Path

from setuptools import setup
from setuptools.command.install import install

NAME = 'openmmla-audio'
DESCRIPTION = ('Audio module for openMMLA platform, including data collection, data processing, and data analytics for '
               'audio data.')

URL = 'https://github.com/ucph-ccs/mbox-audio'
EMAIL = 'lizaibeim@gmail.com'
AUTHOR = 'Zaibei Li'
REQUIRES_PYTHON = '>=3.9.0'
VERSION = "0.1.1"

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
    'PyAudio>=0.2.13',
    'influxdb-client==1.40.0',
    'jiwer==3.0.3',
    'librosa==0.10.1',
    'llvmlite==0.42.0',
    'matplotlib==3.8.3',
    'networkx==3.2.1',
    'paho-mqtt==2.1.0',
    'pydub==0.25.1',
    'pyecharts==2.0.4',
    'redis==5.0.1'
]

extras_require = {
    'server': [
        'Cython==3.0.5',
        'googletrans==4.0.0-rc1',
        'onnxruntime==1.15.1',
        'openai-whisper>=20231117',
        'transformers>=4.38.1',
        'speechbrain>=1.0.0',
        'modelscope>=1.12.0',
        'rotary-embedding-torch>=0.5.3',
        'gunicorn==21.2.0',
        'flask==3.0.2',
        'pandas==2.2.1',
        'gevent==24.2.1',
        'denoiser-compat==0.1.5.dev0',
        'nemo-toolkit[asr]<=1.23.0',
        'huggingface_hub==0.22.0',
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
    packages=['src', 'src/server', 'src/utils', 'src/utils/silero-vad', 'src/utils/silero-vad/files'],
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
