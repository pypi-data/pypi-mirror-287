from setuptools import setup, find_packages

setup(
    name='pdf_processor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pymupdf',
        'Pillow'
    ],
    entry_points={
        'console_scripts': [
            'pdf_processor=pdf_processor.pdf_processor:process_pdf',
        ],
    },
    author='Xun Qin',
    author_email='lvchenjia2050@gmail.com',
    description='A PDF processing package to convert PDF to images and adjust their brightness and contrast.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lvchenjia/pdf-toolkit',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
