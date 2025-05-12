from setuptools import setup, find_packages

setup(
    name='awesome-package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],  # list your dependencies here
    tests_require=['pytest'],
    description='An awesome package for doing awesome things.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/awesome-package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)


