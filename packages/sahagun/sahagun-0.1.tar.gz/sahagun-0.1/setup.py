from setuptools import setup, find_packages

setup(
    name='sahagun',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Lista de dependencias si las hay
    ],
    author='Daniel Vanegas',
    author_email='dvanegasf@outlook.com',
    description='Validador de atributos',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://tu_url.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)