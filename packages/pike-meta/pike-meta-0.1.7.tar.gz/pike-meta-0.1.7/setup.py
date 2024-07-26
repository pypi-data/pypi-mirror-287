import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pike-meta",
    version="0.1.7",
    author="D.V. Krivonos",
    author_email="danil01060106@gmail.com",
    description="A tool for Oxford Nanopore amplicon metagenomics",
    long_description="Pike",
    long_description_content_type="",
    url="https://github.com/DanilKrivonos/Pike",
    project_urls={
        "Bug Tracker": "https://github.com/DanilKrivonos/Pike",
    },
    package_data={

    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    include_package_data=True,
    packages=['Pike', 'Pike.src', 'Pike.example_data'],
    install_requires=[
        'numpy',
        'scikit-bio',
        'biopython',
        'pandas',
        'scipy',
        'scikit-learn',
        'hdbscan',
        'umap-learn',
	'medaka'
    ],
    entry_points={
        'console_scripts': [
            'pike=Pike.pike:main',
            'get_taxonomy=Pike.get_taxonomy:main'
		           ]
    }
)
