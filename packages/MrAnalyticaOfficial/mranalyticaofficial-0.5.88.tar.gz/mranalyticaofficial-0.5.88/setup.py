from setuptools import setup, find_packages

setup(
    name='MrAnalyticaOfficial',
    version='0.5.88',  # Atualize a versão para refletir as novas mudanças
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'opencv-contrib-python',  # Inclui contrib para suportar o módulo cv2.face
        'numpy'
    ],
    author='Seu Nome',
    author_email='seu.email@example.com',
    description='Uma biblioteca poderosa para análise de dados, incluindo o módulo PhoenixVision para reconhecimento facial.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/seuusuario/MrAnalyticaOfficial',  # Atualize com a URL correta do seu projeto
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
