import setuptools

packages = [
    'cube2common',
    'cube2common.utils',
]

setuptools.setup(
    name="cube2common",
    version="0.1",
    packages=packages,
    package_dir={'' : 'src'},
    install_requires=[],
    author="Chasm",
    author_email="fd.chasm@gmail.com",
    url="https://github.com/fdChasm/cube2common",
    license="MIT",
    description="Common Python building blocks for working with the cube 2 engine.",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English"
    ],
)
