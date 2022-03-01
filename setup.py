import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="barfi",
    version="0.4.2",
    author="Adithya Krishnan",
    author_email="krishsandeep@gmail.com",
    description="Framework for a graphical programming environment.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/krish-adi/barfi",
    # package_dir={"": "barfi"},
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
        "networkx >= 2.6.2",
    ],
    project_urls={
        'Source': 'https://github.com/krish-adi/barfi',
    },
)
