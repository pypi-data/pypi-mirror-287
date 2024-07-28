# setup.py
from setuptools import setup, find_packages

setup(
    name='MrAnalyticaOfficial',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy'
    ],
    author='Seu Nome',
    author_email='seu.email@example.com',
    description='Uma ferramenta que facilita a identificação facial.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/seuusuario/PhoenixVision',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
