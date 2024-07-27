from os.path import dirname, join

from setuptools import Extension, find_packages, setup  # type: ignore

setup(
    name="tree_sitter_python",
    packages=find_packages("bindings/python"),
    package_dir={"": "bindings/python"},
    package_data={
        "tree_sitter_python": ["*.pyi", "py.typed"],
        "tree_sitter_python.queries": ["*.scm"],
    },
    ext_modules=[
        Extension(
            name="tree_sitter_python._binding",
            sources=[
                "bindings/python/tree_sitter_python/binding.c",
                "src/parser.c",
                "src/scanner.c",
            ],
            include_dirs=[join(dirname(__file__), "src")],
            extra_compile_args=["-std=c99"],
        ),
    ],
    zip_safe=False,
)
