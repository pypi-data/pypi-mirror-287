import os
from setuptools import setup  # type: ignore


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()


VERSION = '1.0.1'

setup(
    name="pynose-exclude",
    version=VERSION,
    author="Nyefan",
    author_email="pynose-exclude@nyefan.org",
    description="Exclude specific directories from pynose runs.",
    long_description=read('README.rst'),
    license='GNU LGPL',
    url="https://github.com/nyefan/pynose-exclude",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        ("License :: OSI Approved :: GNU Library or Lesser General "
         "Public License (LGPL)"),
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        ],

    py_modules=['pynose_exclude'],
    zip_safe=False,

    entry_points={
        'nose.plugins': ['pynose_exclude = pynose_exclude:PynoseExclude']
        },
    install_requires=['pynose']
)
