from setuptools import setup, find_packages

setup(
    name='MrAnalyticaOfficial',
    version='0.7.52',  # Atualizado para refletir as mudanças significativas
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'opencv-contrib-python',
        'numpy',
        'psutil',
        'scikit-learn',
        'tensorflow',  # Agora incluímos TensorFlow como uma dependência padrão
    ],
    author='Seu Nome',
    author_email='seu.email@example.com',
    description='Uma biblioteca poderosa para análise de dados, incluindo o módulo PhoenixVision para reconhecimento facial avançado e otimizado.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/seuusuario/MrAnalyticaOfficial',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',  # Aumentado para 3.7 para garantir compatibilidade com TensorFlow
)