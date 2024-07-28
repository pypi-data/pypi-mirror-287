from os import path
from distutils.core import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='PyDataforge',
    version='1.0.4',
    description='A package for removing sensitive information from data',
    long_description=long_description,  # 项目的详细说明，通常读取 README.md 文件的内容
    long_description_content_type='text/markdown',
    author='Guipeng Wei',
    author_email='18316734738@163.com',
    url='',
    license='MIT License',
    packages=['PyDataforge'],
    platforms=["all"],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
