import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="mcb-Altair-locust-plugnins",
    version="0.0.1",
    author="Bhagyaraj",
    author_email="mc_raj4u@yahoo.co.in",
    packages=["locust_plugins"],
    description="A sample test package",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/mcraj4u/altair-coe-locust-plugins",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)
