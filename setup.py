from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
        name='pgbackup',
        version='0.1.0',
        description='Database backups local ow s3',
        long_description=readme,
        author='Arthur',
        author_email='arthur393@gmail.com',
        install_requeres=[],
        packages=find_packages('src'),
        package_dir={'':'src'}
)
