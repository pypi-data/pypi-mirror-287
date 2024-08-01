"""The package setup file for AntPack."""
import os
import sys
from setuptools import setup, find_namespace_packages
import pybind11
from pybind11.setup_helpers import Pybind11Extension, build_ext

if sys.version_info[:2] < (3, 7):
    raise RuntimeError("Python version >= 3.7 required.")



def get_version(setup_fpath):
    """Retrieves the version number."""

    os.chdir(os.path.join(setup_fpath, "src", "antpack"))
    with open("__init__.py", "r", encoding="utf-8") as fhandle:
        version_line = [l for l in fhandle.readlines() if
                    l.startswith("__version__")]
        version = version_line[0].split("=")[1].strip().replace('"', "")
    os.chdir(setup_fpath)
    return version



def main():
    """Builds the package and extension."""
    home_dir = os.path.dirname(os.path.abspath(__file__))
    read_me = os.path.join(home_dir, "README.md")
    with open(read_me, "r", encoding="utf-8") as fhandle:
        long_description = "".join(fhandle.readlines())

    cpp_extra_link_args = []
    cpp_extra_compile_args = [
        "-std=c++14"
    ]

    extensions=[
        Pybind11Extension("antpack_cpp_ext",
            sources=[
                "src/antpack/ext/ant_ext.cpp",
                "src/antpack/ext/ig_aligner.cpp",
                "src/antpack/ext/vj_match_counter.cpp",
                "src/antpack/ext/utilities.cpp",
                "src/antpack/ext/responsibility_calcs.cpp",
                "src/antpack/ext/cterm_finder.cpp"
            ],
            include_dirs=[
                "src/antpack/ext",
                pybind11.get_include(),
            ],
            language="c++",
            extra_compile_args=cpp_extra_compile_args  + ["-fvisibility=hidden", "-O3"],
            extra_link_args=cpp_extra_link_args,
        )
    ]

    setup(
        name="antpack",
        package_dir={"":"src"},
        version=get_version(home_dir),
        description="A Python package for processing, manipulating and making inferences about antibody sequence data",
        long_description=long_description,
        long_description_content_type='text/markdown',
        #packages=find_namespace_packages(),
        cmdclass={"build_ext":build_ext},
        setup_requires=['pybind11>=2.4'],
        install_requires=['pybind11>=2.4', "numpy"],
        include_package_data=True,
        ext_modules=extensions,
        python_requires=">=3.7",
        project_urls = {
            'Homepage': 'https://github.com/jlparkI/AntPack',
            'Documentation': 'https://antpack.readthedocs.io/en/latest/index.html'
            },
        package_data={"": ["*.h", "*.c", "*.cpp"]}
    )





if __name__ == "__main__":
    main()
