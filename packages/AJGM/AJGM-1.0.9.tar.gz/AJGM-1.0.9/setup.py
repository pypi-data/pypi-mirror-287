import setuptools
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='AJGM',
    version='1.0.9',
    author='stevenyang',
    author_email='yangsq@hnu.edu.cn',
    description='.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(include=['AJGM', 'AJGM.*']),
    install_requires=['pandas', 'numpy', 'scipy', 'scikit-learn'],
    license='MIT',
    python_requires='>=3.6',
)
