from os import path

from setuptools import setup

def readme():
    with open('README.md', encoding="utf-8") as f:
        return f.read()

setup(
    name='arabic_pronounce_custom',
    version="0.2.6",
    description='Pronounce Arabic words on the fly',
    long_description=readme(),
    long_description_content_type='text/markdown',
    author='Ali Adel',
    author_email='aliadelsaid2003gmail.com',
    url='',
    include_package_data=True,
    zip_safe=False,
    license='GPL-3.0',
    packages=['arabic_pronounce'],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    )
)