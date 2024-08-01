from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='MrAnalyticaOfficial',
    version='0.5.82',  # Incrementei a versão
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'opencv-contrib-python',
        'numpy',
        'face_recognition',
        'dlib'
    ],
    author='Matheus Rodrigo',
    author_email='mranalytica@mranalytica.com',
    description='The MR Analytica technologies for computer vision and face recognition',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://mranalytica.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)