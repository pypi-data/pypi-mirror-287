import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobb_morphIVD",
    version="1.3",
    author="Biobb developers - Maria Paola Ferri",
    author_email="maria.ferri@bsc.es",
    description="Biobb_3DShaper is use case to run a simulation with Abaqus.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="Bioinformatics Workflows BioExcel Compatibility",
    url="https://github.com/mapoferri/Biobb_MorphIVD",
    project_urls={
        "Documentation": "http://biobb_template.readthedocs.io/en/latest/",
        "Bioexcel": "https://bioexcel.eu/"
    },
    packages=setuptools.find_packages(exclude=['adapters', 'docs', 'test']),
    install_requires=['biobb_common==3.8.0','biobb_md>=3.7.0', 'biobb_analysis==3.8.0'],
    python_requires='==3.8.*',
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
    ),
)
