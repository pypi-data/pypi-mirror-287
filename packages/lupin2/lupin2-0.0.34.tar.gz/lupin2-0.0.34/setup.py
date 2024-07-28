import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="lupin2",
  version="0.0.34",
  author="Roryou",
  author_email="rokira0825@outlook.com",
  description="for myself",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/RoRyou/Lupin2",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)


