from setuptools import setup

setup(
    name='ani-shedule',
    version='0.2.0',
    description='See Airing Anime',
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
    install_requires=['requests==2.32.3', 'lxml==5.2.2', 'tqdm==4.63.0', 'argparse==1.4.0', 'prompt_toolkit==3.0.43', 'tabulate==0.9.0'],
    entry_points={
        'console_scripts': [
            'ani-shedule=shedule:main',
        ],
    },
)