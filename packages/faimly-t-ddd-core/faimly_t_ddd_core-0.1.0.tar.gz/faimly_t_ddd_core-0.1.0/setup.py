from setuptools import setup, find_packages

setup(
    name="faimly_t_ddd_core",
    version="0.1.0",
    author="David Gonzalez",
    author_email="degonzalez2194@gmial.com",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Faimly-T/Python-DDD-TemplateCode.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
