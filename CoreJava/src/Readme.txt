原版代码文件中的java代码文件没有合适的包名，无法直接将整个目录拷贝到某个eclipse工程里运行，
因此写了两个python脚本，一个用于将java文件所在目录作为其包名。一个用于移除添加的包名。
这样可以直接拷贝到eclipse工程里去运行了。

注：原来部分代码中加有包名，python脚本会删除旧包名并用目录名作为包名将其替代。可能在某些import代码中需要处理替换导致的错误