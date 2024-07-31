import os
import sys

from setuptools import find_packages, setup, Command
from setuptools.command.build_ext import build_ext as _build_ext
from setuptools.command.install import install as _install
from shutil import rmtree

MODULE_NAME = 'sdk_license_client'
VERSION = '0.0.1'

ROOTPATH = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s: str):
        """控制台输出."""
        sys.stdout.write('\033[1m{0}\033[0m'.format(s) + '\n')
        sys.stdout.flush()  # 确保内容被及时输出

    def initialize_options(self):
        """
        初始化选项
        :return:
        """
        pass

    def finalize_options(self):
        """
        检查和处理选项
        :return:
        """
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(ROOTPATH, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))  # sys.executable 为 Python 解释器的路径

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system(f'git commit -am "Update version {VERSION}"')
        os.system('git push')
        # os.system(f'git tag v{VERSION}')
        # os.system('git push --tags')

        sys.exit()


setup(
    name=MODULE_NAME,
    version=VERSION,
    author="alan",
    author_email="al6nlee@gmail.com",
    description="license的客户端",
    long_description=long_description,  # 项目的详细描述，会显示在PyPI的项目描述页面。必须是rst(reStructuredText) 格式的
    long_description_content_type="text/markdown",
    url="https://github.com/al6nlee/sdk_license_client",
    packages=find_packages(exclude=('tests', 'tests.*')),  # 指定最终发布的包中要包含的packages
    license='MIT License',  # 指定许可证类型
    classifiers=[
        "Intended Audience :: Developers",  # 目标用户
        'License :: OSI Approved :: MIT License',  # 许可证类型
        "Programming Language :: Python :: 3",  # 支持的 Python 版本
        "Topic :: Software Development"
    ],
    install_requires=[],  # 项目依赖哪些库(内置库就可以不用写了)，这些库会在pip install的时候自动安装
    python_requires='>=3.8',
    package_data={  # 默认情况下只打包py文件，如果包含其它文件比如.so格式，增加以下配置
        "loggingA": [
            "*.py",
            "*.so",
        ]
    },
    cmdclass={
        # 'build_ext': BuildExtCommand,  # 构建 C 扩展模块
        # 'install': InstallCommand,  # 安装包到 Python 环境
        'push': UploadCommand,  # python3 setup.py push 触发，使用 twine
    },
)
