import pathlib

import setuptools

setuptools.setup(
    name="py-cdgram",
    version="0.2.0",
    description="This Python package helps you download images from Pinterest URLs.",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://amalnath.vercel.app",
    author="Amal Nath H",
    author_email="amalnath0600@gmail.com",
    license="GNU GENERAL PUBLIC LICENSE",
    project_urls={
        "Documentation": "https://github.com/MrTG-CodeBot/pymedia/blob/main/README.md",
        "source": "https://github.com/MrTG-CodeBot/pymedia",
    },
    python_requires= ">=3.9.0, <3.11.0",
    install_requires=["requests", "bs4", "google-generativeai"],
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={"console_scripts": ["pymedia= pymedia.cli:main"]}
)
