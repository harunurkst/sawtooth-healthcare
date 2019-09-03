# Copyright 2017 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------

from __future__ import print_function

from setuptools import setup, find_packages

conf_dir = "/etc/sawtooth"

setup(
    name='healthcare-client',
    version='0.1',
    description='Sawtooth HealthCare Client Example',
    author='Hyperledger Sawtooth',
    url='https://github.com/hyperledger/sawtooth-core',
    # packages=find_packages(exclude=['processor', 'rest_api']),
    packages=find_packages(),
    install_requires=[
        # 'aiohttp',
        'colorlog',
        'protobuf',
        'sawtooth-sdk',
        'requests',
        'sawtooth-signing',
        'PyYAML',
        'sawtooth-cli',
    ],
    # data_files=data_files,
    entry_points={
        'console_scripts': [
            'healthcare-cli-python = cli.workflow.healthcare_cli:main_wrapper',
        ]
})
