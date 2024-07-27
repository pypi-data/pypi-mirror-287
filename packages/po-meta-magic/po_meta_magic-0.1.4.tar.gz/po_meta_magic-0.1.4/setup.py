from setuptools import setup, find_packages

setup(
    name='po_meta_magic',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        'pillow',
        'fuzzywuzzy',
        'python-dateutil',
        'pytesseract',
    ],
)
