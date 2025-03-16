from setuptools import setup, find_packages

setup(
    name='jessilver_django_seed',
    version='1.0.2',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A library to facilitate the creation of fake data (seeds) in Django projects.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jessilver/django_seed',
    author='Jesse Silva',
    author_email='jesse1eliseu@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
    install_requires=[
        'Django>=5.1',
    ],
)