from setuptools import setup, find_packages
import os

version = '0.1.2'

setup(name='plonetheme.ewb_case',
    version=version,
    description="A Plone 4 theme for EWB Case",
    long_description=open("README.txt").read() + "\n" +
                     open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
    ],
    keywords='',
    author='Matt Bierner',
    author_email='mattbierner@gmail.com',
    url='https://github.com/mattbierner/plonetheme.ewb_case',
    license='Creative Commons Attribution 3.0 Unported',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plonetheme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Plone>=4.0',
        'plone.app.registry',
    ],
    entry_points="""
    # -*- Entry points: -*-
    
    [z3c.autoinclude.plugin]
    target = plone
    """,
    setup_requires=[],
)
    
