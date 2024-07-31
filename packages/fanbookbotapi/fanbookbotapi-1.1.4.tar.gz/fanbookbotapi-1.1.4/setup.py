from setuptools import setup, find_packages

setup(
    name='fanbookbotapi',
    version='1.1.4',
    packages=find_packages(),
    install_requires=[
        # 这里列出你的依赖包，例如：
        # 'numpy',
    ],
    author='wangdage',
    author_email='fanbookwdg1122@outlook.com',
    description='fb bot api',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
