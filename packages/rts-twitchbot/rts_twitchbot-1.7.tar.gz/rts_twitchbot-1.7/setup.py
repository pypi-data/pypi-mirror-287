from setuptools import setup, find_packages

setup(
    name='rts_twitchbot',
    version='1.7',
    packages=find_packages(),
    description='A RTS Package to create your own Twitch Bot.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='RandomTimeTV',
    author_email='dergepanzerte1@gmail.com',
    license='Unlicensed',
    url='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    keywords='',
    install_requires=["rts_webuibuilder", "rts_docsbuilder","extrautilities","websockets"],
)