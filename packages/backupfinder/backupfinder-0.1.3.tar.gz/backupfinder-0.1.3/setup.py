from setuptools import setup, find_packages

setup(
    name='backupfinder',
    version='0.1.3',
    description='A tool for generating log and backup wordlists based on domain URLs.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='WOPRbot',
    author_email='woprbot@hacknex.us',
    url='https://github.com/pentestfunctions/custom-backup-finder/',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here, e.g.,
        # 'requests>=2.25.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    entry_points={
        'console_scripts': [
            'backupfinder=backupfinder.main:main',
        ],
    },
    python_requires='>=3.6',
)
