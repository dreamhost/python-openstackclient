# Copyright 2012 OpenStack LLC.
# All Rights Reserved
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import os

import setuptools

from openstackclient.openstack.common.setup import generate_authors
from openstackclient.openstack.common.setup import parse_requirements
from openstackclient.openstack.common.setup import parse_dependency_links
from openstackclient.openstack.common.setup import write_git_changelog


requires = parse_requirements()
dependency_links = parse_dependency_links()
write_git_changelog()
generate_authors()


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name="python-openstackclient",
    version="0.1",
    description="OpenStack command-line client",
    long_description=read('README.rst'),
    url='https://github.com/openstack/python-openstackclient',
    license="Apache License, Version 2.0",
    author='OpenStack Client Contributors',
    author_email='openstackclient@example.com',
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    classifiers=[
       'Development Status :: 2 - Pre-Alpha',
       'Environment :: Console',
       'Intended Audience :: Developers',
       'Intended Audience :: Information Technology',
       'License :: OSI Approved :: Apache Software License',
       'Operating System :: OS Independent',
       'Programming Language :: Python',
    ],
    install_requires=requires,
    dependency_links=dependency_links,
    test_suite="nose.collector",
    entry_points={
        'console_scripts': ['openstack=openstackclient.shell:main'],
        'openstack.cli': [
            'list_server=openstackclient.compute.v2.server:List_Server',
            'show_server=openstackclient.compute.v2.server:Show_Server',
            'create_service=' +
                'openstackclient.identity.v2_0.service:Create_Service',
            'list_service=openstackclient.identity.v2_0.service:List_Service',
            'show_service=openstackclient.identity.v2_0.service:Show_Service',
            'create_tenant=' +
                'openstackclient.identity.v2_0.tenant:Create_Tenant',
            'delete_tenant=' +
                'openstackclient.identity.v2_0.tenant:Delete_Tenant',
            'list_tenant=openstackclient.identity.v2_0.tenant:List_Tenant',
            'show_tenant=openstackclient.identity.v2_0.tenant:Show_Tenant',
            'set_tenant=openstackclient.identity.v2_0.tenant:Set_Tenant',
        ]
    }
)
