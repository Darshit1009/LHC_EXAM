from setuptools import setup, find_packages
##this is about project description which shown in that pypi 

setup(
    name='Signal_ICT_Darshit_kacha_92400133089',  # package name 
    version='0.1.0',
    author='Darshit Kacha',
    description='Modular signal processing toolkit for ICT coursework',
    long_description=open('README.md', encoding='utf-8').read(),#UTF-8 is a character encoding that represents characters and symbols using 1 to 4 bytes
    long_description_content_type='text/markdown',
    packages=find_packages(),  # Automatically finds your package folder
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    include_package_data=True,
)