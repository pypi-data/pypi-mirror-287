# test-copasi
This project builds the COPASI binary wheels from the COPASI and copasi dependencies. 


```bash
git clone https://github.com/fbergmann/test-copasi
cd test-copasi
git submodule update --init --remote --recursive  --rebase

# update copasi version
cd copasi_source && ./gitTools/UpdateCopasiVersion --force
```

at that point we are ready to build the python source package:

```bash
./scripts/create-source-package.sh
```

## Pyodide
The source package works now also in pyodide. Here is how to build 
the emscripten wheels using pyodide & docker: 


```bash
git clone https://github.com/pyodide/pyodide.git
./run_docker
make

```

**Note** the versions built, are not compatible with each other, so always check out the correct tag of pyodide for what you want. For example using: 

```bash
cd pyodide 
git checkout tags/v0.25.0
```

if you switch tags, be sure to rebuild cpython and emsdk: 

```bash
run_docker
```

then in the docker container execute

```bash
make -C emsdk clean
make -C cpython clean
make -C emsdk
make -C cpython
source ./emsdk/emsdk/emsdk_env.sh
make
```


Now we are ready to build the wheel. From the pyodide directory (`/src` in docker assuming you extracted the python-copasi source package there):

```
PYTHON_INCLUDE_DIR=`echo /src/cpython/installs/python-*/include/python*/` pyodide build python-copasi-4.43.287 --exports whole_archive
```