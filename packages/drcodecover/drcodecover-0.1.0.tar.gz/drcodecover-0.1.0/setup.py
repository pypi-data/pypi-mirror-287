from setuptools import setup, find_packages

setup(
    name='drcodecover',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'sentry-sdk',
    ],
    author='Mohd Nadeem',
    author_email='codewithnadeem@gmail.com',
    description='A special package for drcode',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/codewithnadeem14502/drcode-wrapper-python',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)