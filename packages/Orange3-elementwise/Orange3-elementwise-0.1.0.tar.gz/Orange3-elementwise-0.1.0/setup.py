#!/usr/bin/env python

from os import path, walk

import sys
from setuptools import setup, find_packages



NAME = "Orange3-elementwise"

VERSION = "0.1.0"

DESCRIPTION = "A collection of elementwise widgets"
LONG_DESCRIPTION = open(path.join(path.dirname(__file__), 'README.pypi'),
                        'r', encoding='utf-8').read()

LICENSE = "GPLv3+"

KEYWORDS = (
    'orange3 add-on',
    'elementwise',
)

PACKAGES = find_packages()

PACKAGE_DATA = {
    'orangecontrib.elementwise': ['tutorials/*.ows'],
    'orangecontrib.elementwise.widgets': ['icons/*'],
}

DATA_FILES = [
    # Data files that will be installed outside site-packages folder
]

requirements = ['requirements.txt']


INSTALL_REQUIRES = sorted(set(
    line.partition('#')[0].strip()
    for file in (path.join(path.dirname(__file__), file)
                 for file in requirements)
    for line in open(file)
) - {''})


EXTRAS_REQUIRE={
    'doc': ['sphinx', 'recommonmark'],
},


ENTRY_POINTS = {
    # Entry points that marks this package as an orange add-on. If set, addon will
    # be shown in the add-ons manager even if not published on PyPi.
    'orange3.addon': (
        'elementwise = orangecontrib.elementwise',
    ),
    # Entry point used to specify packages containing tutorials accessible
    # from welcome screen. Tutorials are saved Orange Workflows (.ows files).
    'orange.widgets.tutorials': (
        # Syntax: any_text = path.to.package.containing.tutorials
        'elementwise_tutorials = orangecontrib.elementwise.tutorials',
    ),

    # Entry point used to specify packages containing widgets.
    'orange.widgets': (
        # Syntax: category name = path.to.package.containing.widgets
        # Widget category specification can be seen in
        #    orangecontrib/example/widgets/__init__.py
        'Elementwise = orangecontrib.elementwise.widgets',
    ),

    # Register widget help
    "orange.canvas.help": (
        'html-index = orangecontrib.elementwise.widgets:WIDGET_HELP_PATH',)
}

NAMESPACE_PACKAGES = ["orangecontrib"]

TEST_SUITE = "orangecontrib.elementwise.tests.suite"


def include_documentation(local_dir, install_dir):
    global DATA_FILES

    doc_files = []
    for dirpath, _, files in walk(local_dir):
        doc_files.append((dirpath.replace(local_dir, install_dir),
                          [path.join(dirpath, f) for f in files]))
    DATA_FILES.extend(doc_files)


if __name__ == '__main__':
    include_documentation('doc/_build/html', 'help/orange3-elementwise')
    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        license=LICENSE,
        packages=PACKAGES,
        package_data=PACKAGE_DATA,
        data_files=DATA_FILES,
        install_requires=INSTALL_REQUIRES,
        extra_requires=EXTRAS_REQUIRE,
        entry_points=ENTRY_POINTS,
        keywords=KEYWORDS,
        namespace_packages=NAMESPACE_PACKAGES,
        zip_safe=False,
    )
