import setuptools
from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='s1290166_learn',
    version='0.1.0',
    author='Hiroyuki Matushima',
    author_email='hiroyuki0228n@gmail.com',
    description='This software is being developed by Hiroyuki Matushima',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/uda/PAMI',  # 正しいURLに変更してください
    packages=find_packages(include=['s1290166_learn', 's1290166_learn.*']),
    license='GPLv3',
    install_requires=[
        'pandas',
        'numpy',
        'scipy',
        'matplotlib',
        'seaborn',
        'requests',
        'pillow',
        'tqdm',
        'pami'
    ],
    extras_require={
        'gpu': ['cupy', 'pycuda'],
        'spark': ['pyspark'],
        'dev': ['twine', 'setuptools', 'build'],
        'all': ['cupy', 'pycuda', 'pyspark', 'twine', 'setuptools', 'build']
    },
    classifiers=[
        'Development Status :: 4 - Beta',  # 状態に応じて変更可能
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
)
