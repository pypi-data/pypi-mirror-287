import setuptools #导入setuptools打包工具
 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("version", "r", encoding="utf-8") as f:
    version = f.read().strip()
 
setuptools.setup(
    name="Sqlite3_EasyCtrl",
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
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)