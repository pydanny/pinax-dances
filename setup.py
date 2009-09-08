from setuptools import setup, find_packages
 
version = '0.1.0'
 
LONG_DESCRIPTION = """
=====================================
pinax-dances
=====================================

Pinax wall lets set up flash mob groups
"""
 
setup(
    name='pinax-dances',
    version=version,
    description="Pinax wall lets set up flash mob groups",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='django,pinax',
    author='Daniel Greenfeld',
    author_email='pydanny@gmail.com',
    url='http://github.com/pydanny/pinax-dances/tree/master',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    setup_requires=['setuptools_git'],
)
