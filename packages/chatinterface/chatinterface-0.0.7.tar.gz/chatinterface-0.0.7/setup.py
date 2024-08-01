"""
Build for chatbot
"""
import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    setuptools.setup(
        name="chatinterface",
        version="0.0.7",
        author="Juris Kaminskis",
        author_email="juris@kolumbs.net",
        description="Chatbot implementation",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/Kolumbs/chatbot",
        packages=["chatinterface"],
        install_requires=[
            "rapidfuzz>=2.11.1",
            "membank>=0.4.1",
        ],
        python_requires=">=3.10",
)
