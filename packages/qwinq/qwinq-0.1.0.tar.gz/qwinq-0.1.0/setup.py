from setuptools import find_packages, setup

with open("README.MD", "r") as f:
    long_description = f.read()

setup(
    name='qwinq',
    version='0.1.0',
    author="buf1024",
    author_email="buf1024@gmail.com",
    maintainer="buf1024",
    maintainer_email="buf1024@gmail.com",
    packages=find_packages(include=['qwinq']),
    include_package_data=True,
    zip_safe=False,
    description='股票个人量化交易系统',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'qfetch',
        'qdatac',
        'qstrategy',
        'pyecharts',
        'TA-Lib',
    ],
    entry_points={
        'console_scripts': [
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
