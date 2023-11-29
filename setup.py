from setuptools import setup, find_packages

# get the list of dependencies in the requirements.txt
with open('requirements.txt', 'r') as f:
    lib_list = [line.strip() for line in f if line.strip() != '-e .']

setup(
    name='rag',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires = lib_list,
    author='Phi Nguyen',
    author_email='nguyenhongphi2807@gmail.com'
)