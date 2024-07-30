from setuptools import setup, find_packages

setup(
    name='clspt',
    version='0.1.0',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # 'scrapy>=2.0.0',
    ],
)
