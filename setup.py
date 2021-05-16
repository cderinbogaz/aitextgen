from setuptools import setup

setup(
    name="aitextgen-aws",
    packages=["aitextgen-aws"],  # this must be the same as the name above
    version="0.5.1",
    description="Fork of aitextgen to set parallel computing settings to be able to run on AWS sagemaker.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Original work by Max Woolf, forked by Ceyhun Derinbogaz",
    author_email="ceyhun@textcortex.com",
    url="https://github.com/cderinbogaz/aitextgen-aws",
    keywords=["gpt-2", "gpt2", "text generation", "ai"],
    classifiers=[],
    license="MIT",
    entry_points={"console_scripts": ["aitextgen=aitextgen.cli:aitextgen_cli"]},
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=[
        "transformers>=4.5.1",
        "fire>=0.3.0",
        "pytorch-lightning>=1.2.7",
        "torch>=1.6.0",
    ],
)
