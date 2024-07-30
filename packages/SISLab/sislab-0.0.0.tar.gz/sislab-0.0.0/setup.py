from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="SISLab",
    version="0.0.0",
    description="Inje University Department of Biomedical Engineering SISLab open source library for signal processing, image processing and AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Shyubi",
    author_email="sjslife97@gmail.com",
    url="https://github.com/Shyuvi/SISLab",  # 프로젝트의 URL을 명시하세요
    packages=find_packages(),
    install_requires=["numpy", "pillow", "opencv-python", "tensorflow", "pytorch", "scikit-learn", "scipy", "matplotlib"],
    python_requires=">=3.8",
    keywords=["shyubi", "sislab", "signal", "image"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # 해당 라이선스를 명시하세요
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)