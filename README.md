## ELFTracer

* Useful when you want to:
  * transfer ELF binaries file to buildroot env., but the file depends on many dynamic libs
  * extract any ELF binaries to a minimized contianer image
* ELFTracer gives a list of path of unique depend-libs, you can use this path to copy or do other actions


* Simply based on tools of ELF file, such as `ldd`, etc.
* Currently only contains static analysis, will add dynamic analysis such as `lsof`, etc.
* Contributions are very welcomed
