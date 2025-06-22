from setuptools import setup, find_packages

setup(
    name='jessilver_django_seed',
    version='2.0.0',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    license='MIT License',
    description='A library to facilitate the creation of fake data (seeds) in Django projects.',
    long_description=open('README.md', encoding='utf-8').read(),
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
        'Django>=3.2',
    ],
    python_requires='>=3.7',
    keywords='django, seed, fake data, testing, development',
    project_urls={
        'Documentation': 'https://github.com/jessilver/django_seed#readme',
        'Source': 'https://github.com/jessilver/django_seed',
        'Tracker': 'https://github.com/jessilver/django_seed/issues',
    },
)