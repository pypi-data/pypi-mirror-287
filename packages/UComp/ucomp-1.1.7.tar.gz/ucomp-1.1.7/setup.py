from setuptools import setup, find_packages

setup(
    name='UComp',
    version='1.1.7',
    author='Diego J. Pedregal',
    author_email='diego.pedregal@uclm.es',
    description='Modelling and forecasting univariate time series',
    long_description='Modelling and forecasting univariate time series',
    url='https://github.com/djpedregal/UComp',
    packages=find_packages(),
    include_package_data=True,
    package_data={'UComp': ['UComp/*.pyd', 'UComp/*.so', 'UComp/libopenblas.dll', 'UComp/*.bin']},
    keywords='paquete ejemplo',
    install_requires=[
        'numpy>=1.18.0',
        'requests>=2.25.0',
        'seaborn',
        'pandas',
        'matplotlib',
        'scipy',
    ],
)
