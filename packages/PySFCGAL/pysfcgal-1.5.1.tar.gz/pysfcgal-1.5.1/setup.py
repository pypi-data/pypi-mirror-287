from setuptools import setup, Extension

setup(
    name="PySFCGAL",
    version="1.5.1",
    description="Python binding of SFCGAL.",
    long_description="""Python binding of SFCGAL. SFCGAL is a C++ wrapper
    library around CGAL with the aim of supporting ISO 191007:2013 and OGC
    Simple Features for 3D operations.""",
    url="https://gitlab.com/SFCGAL/pysfcgal",
    author="Joshua Arnott (initial work) and Loïc Bartoletti (Oslandia)",
    author_email="info@oslandia.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: BSD License",
    ],
    packages=["pysfcgal"],
    setup_requires=["cffi>=1.0.0"],
    ext_modules=[
        Extension(
            'pysfcgal.sfcgal',
            ['pysfcgal/sfcgal_def.c', 'pysfcgal/sfcgal_def_msvc.c'],
            include_dirs=['pysfcgal'],
            py_limited_api=True
            )
        ],
    cffi_modules=["pysfcgal/sfcgal_build.py:ffibuilder"],
    install_requires=["cffi>=1.0.0"],
    extras_require={'contract': ["icontract>=2.6.0"]}
)
