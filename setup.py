##############################################################################
#
# Copyright (c) 2004 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from setuptools import setup

__version__ = '1.1.1.dev0'

setup(
    name='five.customerize',
    version=__version__,
    description='TTW customization of template-based Zope views',
    long_description=(open('README.rst').read() + "\n" +
                      open('CHANGES.rst').read()),
    keywords='zope views templates customization ttw',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    url='https://pypi.python.org/pypi/five.customerize',
    license='ZPL 2.1',
    packages=['five', 'five.customerize'],
    package_dir={'': 'src'},
    namespace_packages=['five'],
    include_package_data=True,
    platforms='Any',
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.portlets',
        'zope.component',
        'zope.componentvocabulary',
        'zope.dottedname',
        'zope.interface',
        'zope.lifecycleevent',
        'zope.pagetemplate',
        'zope.schema',
        'zope.traversing',
        'zope.viewlet',
        'Acquisition',
        'Zope2',
    ],
    extras_require={
        'test': [
            'zope.publisher',
            'zope.site',
            'zope.testing',
            'transaction',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Zope2',
        'License :: OSI Approved :: Zope Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
)
