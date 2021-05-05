from setuptools import find_packages, setup

setup(
    name="rebase-fu",
    use_scm_version=False,
    version="0.0.1",
    setup_requires=["setuptools_scm", "pytest-runner"],
    tests_require=["pytest"],
    include_package_data=True,
    packages=find_packages(exclude=["tests", "tests/*"]),
    description="all about the rebase, no trouble",
    author="Victor Ng",
    author_email="victor@crankycoder.com",
    url="https://github.com/cranycoder/git-rebase-kata",
    license="MPL 2.0",
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    zip_safe=False,
)
