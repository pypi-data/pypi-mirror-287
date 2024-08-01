import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("version", "r", encoding="utf-8") as f:
    version = f.read()
 
setuptools.setup(
    name="sqlite_easy_ctrl",
    version=version,
    author="xingchen",
    author_email="xingchenawa@qq.com",
    description="一个可以更方便的操作SQLite数据的Python库",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xingchentye/Python-Sqlite3-EasyCtrl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)