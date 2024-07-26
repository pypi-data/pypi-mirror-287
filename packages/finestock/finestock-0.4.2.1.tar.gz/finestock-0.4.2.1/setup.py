from setuptools import setup, find_packages

setup(
    name='finestock',
    version='0.4.2.1',
    description='Korean Stock OpenAPI Package(EBest, KIS, LS) creation written by alshin',
    author='A.Lok, Shin',
    author_email='shinalok357@gmail.com',
    url='https://github.com/shinalok/finestock',
    install_requires=['websockets', 'asyncio', 'requests', 'loguru',],
    packages=find_packages(exclude=[]),
    keywords=['ebest', 'kis', 'ls', 'openapi', 'stock', 'kr'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)