import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grape_grape",
    version="1.0.3",
    author="putao",
    author_email="putaoisapig@163.com",
    description="grape_grape",
    long_description="grape_grape",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=["Pillow", "requests"]
)
