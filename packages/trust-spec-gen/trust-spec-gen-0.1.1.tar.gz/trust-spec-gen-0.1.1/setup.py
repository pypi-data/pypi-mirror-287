from setuptools import setup, find_packages

setup(
    name='trust-spec-gen',
    version='0.1.1',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'argparse',
    ],
    entry_points={
        'console_scripts': [
            'trust = trust_spec_gen.main:run',
        ],
    }
)
