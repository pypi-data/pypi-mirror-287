import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='s1300056_learn',
    version='2024.07.29.1',
    author='SUZUKI Haruto',
    author_email='s1300056@u-aizu.ac.jp',
    description='This is description',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    url='https://github.com/YATTAmanre/s1300056_learn',
    license='GPLv3',
    install_requires=[
        'pami',
        'statistics',
        'visualization',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
    python_requires='>=3',
)