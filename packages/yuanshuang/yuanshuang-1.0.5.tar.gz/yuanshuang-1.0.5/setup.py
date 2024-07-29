import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yuanshuang",
    version="1.0.5",
    author="yuanshuang",
    install_requires=[
        # 'numpy<=1.26.4',
        # 'matplotlib>=3.9.1',
        # 'pandas>=2.2.2',
        # 'prophet>=1.1.5'
    ],
    url='',
    author_email="18872142367@qq.com",
    description="sk_pg package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)
