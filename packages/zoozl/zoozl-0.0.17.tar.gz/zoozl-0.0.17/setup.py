"""
Build for zoozl services
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

    setuptools.setup(
        name="zoozl",
        version="0.0.17",
        author="Juris Kaminskis",
        author_email="juris@zoozl.net",
        description="Zoozl services",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/Kolumbs/zoozl",
        packages=["zoozl"],
        install_requires=[
            "rapidfuzz==2.11.1",
            "membank>=0.4.1",
            "chatbot>=0.0.5",
            "chatbot_fifa_extension>=0.0.3",
        ],
        python_requires=">=3.11",
)
