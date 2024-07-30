import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="Altair-mcb-locust-plugins",
    version="0.0.2",
    author="Bhagyaraj",
    author_email="mc_raj4u@yahoo.co.in",
    packages=["locust_plugins/dashboards/locust-grafana", "locust_plugins/dashboards/locust-timescale", "locust_plugins/dashboards/screenshots", "locust_plugins/listeners", "locust_plugins/users"],
    description="A sample test package",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/mcraj4u/altair-coe-locust-plugins",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)
