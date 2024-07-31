from setuptools import setup, find_packages

setup(
    name='MrAnalyticaOfficial',
    version='0.5.2',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'mediapipe',
        'numpy',
        'face_recognition',
    ],
    author='Matheus Rodrigo',
    author_email='mranalytica@mranalytica.com',
    description='The MR Analytica technologies',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://mranalytica.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
