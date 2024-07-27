from setuptools import setup, find_packages

setup(
    name='fuzzy_redirect_mapper',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'fuzzywuzzy[speedup]',
        'python-Levenshtein',
    ],
    entry_points={
        'console_scripts': [
            'fuzzy_redirect_mapper=fuzzy_redirect_mapper.redirect_mapper:main',
        ],
    },
    author='Chris Lever SEO',
    author_email='hello@chrisleverseo.com',
    description='A tool to speed up redirect mapping using fuzzy matching.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://chrisleverseo.com/t/python-fuzzy-multi-format-redirect-builder.147/',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
