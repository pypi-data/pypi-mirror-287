import requests
import setuptools

name = "patternity"
url = "https://pypi.org/project/%s/" % name

response = requests.get(url)
assert response.status_code == 404, "Project already exists"

setuptools.setup(
    url=url,
    name=name,
    version="0.0.0",
    author="Artyom Vancyan",
    author_email="artyom.vancyan2000@gmail.com",
    description="The package is coming soon...",
)
