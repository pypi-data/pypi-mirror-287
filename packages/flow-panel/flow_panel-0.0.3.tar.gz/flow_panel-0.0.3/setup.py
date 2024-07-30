from setuptools import setup, find_packages

setup(
    name='flow_panel',
    version='0.0.3',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
        ],
    },
    # Optional fields
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bin2ai/flow-panel',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
