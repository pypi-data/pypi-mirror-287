import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mranalytica",
    version="0.0.1",  # Defina a versão inicial
    author="MR Analytica",
    author_email="",
    description="Biblioteca de reconhecimento facial",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seu_usuario/mranalytica",  # Link para o repositório
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Escolha a licença apropriada
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'opencv-python',
        'numpy',
    ],
)
