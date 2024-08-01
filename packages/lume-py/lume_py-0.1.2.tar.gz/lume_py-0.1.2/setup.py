from setuptools import setup, find_packages

setup(
    name='lume-py',
    version='0.1.2',
    description='A description of your SDK',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Lume SDK',
    author_email='aryan@lume.ai',
    url='https://github.com/Lume-ai/lume-py',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'httpx>=0.27.0',
        'pydantic>=2.8.2',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.12',
)
