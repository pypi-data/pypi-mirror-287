from setuptools import setup, find_packages

# Read the requirements from the requirements.txt file
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="fmperf",
    version="0.0.2",
    package_data={"fmperf.data": ["ai.txt", "all_nbins_64.pkl"]},
    packages=find_packages(),
    url='https://github.com/fmperf-project/fmperf.git',
    author='IBM Research',
    license='Apache 2.0',
    install_requires=required,
)