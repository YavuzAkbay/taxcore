from setuptools import setup, find_packages

setup(
    name='taxcore',
    version='0.1.4',
    description='A comprehensive technical analysis library for Python.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/YavuzAkbay/taxcore',
    author='Yavuz',
    author_email='akbay.yavuz@example.com',
    license='GPL-3.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
