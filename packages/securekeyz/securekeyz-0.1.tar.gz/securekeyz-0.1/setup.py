from setuptools import setup

setup(
    name='securekeyz',
    version='0.1',
    description="SecureKeyz is a Python-based command-line tool designed to help you securely manage your API keys. It allows you to store, modify, and transfer API keys between different services while keeping them encrypted.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='hasan',
    author_email='hasanfq818@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['argparse==1.4.0', 'prompt_toolkit==3.0.43', 'prompt_toolkit==3.0.43'],
    entry_points={
        'console_scripts': [
            'securekeyz=mail:main',
        ],
    },
)