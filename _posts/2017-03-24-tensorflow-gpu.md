---
layout: post
title:  "Compile Tensorflow with GPU Support on Fedora"
date:   2017-03-24
categories: misc
comments: true
---

Since sometimes the training with CPU is low, I try to compile a tensorflow with gpu support. And I install it on a desktop and open `openssh-server` since my laptop does not have Nvidia GPU.

## Environments

- Fedora 25 Workstation with GUI.
- Kernel version `4.9.14-200.fc25.x86_64`.
- GTX 950.
- We use `zsh` and `oh-my-zsh`.
- Public IP address.
- Need admin permission.

## Dependencies

We need compile many things from source code and it is tricky to deal with. Here is the relationship.

- gcc5
    - compiles by gcc6
- Nvidia CUDA and cuDNN
- python and pip
    - pyenv
    - Anaconda
- Bazel (compiled from source code)
    - gcc
    - Java
    - others

## SSH Support

To install `openssh-server`, type (Fedora may have it already)

```
sudo dnf install openssh-server
```

To see if it is running,

```shell
/sbin/service sshd status
```

To start

```shell
systemctl start sshd.service
systemctl enable sshd.service
```

In order to change the port, just

```shell
vim /etc/ssh/sshd_config
```

and uncomment `Port 22` and replace `22` with any port like `12340`. Finally,

```shell
semanage port -a -t ssh_port_t -p tcp 12340
systemctl restart sshd.service
```

To test if it works ok,

```shell
ssh username@127.0.0.1 -p 12340
```

## Install Gcc 5

By default, Fedora

```shell
sudo dnf install gcc gcc-c++ kernel-devel kernel-headers
```

 installs `gcc6` and `g++`. However, `CUDA` is not compatible with `gcc` later than 5. Therefore, we need a `gcc5`. You can get it in another way. Here I choose to compile it from source code. Note that you need `gcc5.4` since it seems there is a bug in `gcc5.3` when compiling `gcc5.3` with `gcc6.3`.

```shell
# Download
wget http://ftp.gnu.org/gnu/gcc/gcc-5.4.0/gcc-5.4.0.tar.gz

# unzip
tar xvfj gcc-5.4.0.tar.gz
cd gcc-5.4.0

# Download prerequisites
./contrib/download_prerequisites
cd ..

# build
mkdir objdir
cd objdir
../gcc-5.4.0/configure --with-system-lib --disable-multilib --enable-languages=c,c++ --prefix=/home/jasonqsy/gcc54
make -j4
make install
```

Note that you need set `prefix` by hand since the default `prefix` is `/usr/local`. To test it,

```Shell
~/gcc54/bin/gcc --version
```

and it shows 5.4.0.

## Python version

Personally, I use `pyenv` to manage versions of `python` and install `anaconda` because it is designed for scientific computation. To install pyenv, follow [pyenv](https://github.com/pyenv/pyenv#basic-github-checkout) or type as follows.

```shell
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
exec $SHELL
```

And we have `pyenv` now. To install `anaconda`, type

```shell
pyenv install anaconda3-3.4.0
pyenv global anaconda3-3.4.0
```

To test the installation, type

```
conda list
python --version
```

and should be 3.6. Moreover, `protobuf` should be installed by

```shell
pip install protobuf
```

## Install CUDA

We need

- CUDA 8.0
- cuDNN

Download CUDA from <https://developer.nvidia.com/cuda-downloads>. Then

```shell
sudo rpm -i cuda-repo-fedora23-8-0-local-ga2-8.0.61-1.x86_64.rpm
sudo dnf clean all
sudo dnf install cuda
```

and `cuda` will be installed at `/usr/local/cuda-8.0`. We will need the directory when compiling `tensorflow`.

For cuDNN, register and download it from <https://developer.nvidia.com/cudnn>. Just extracting it is ok. I choose to put it at `/usr/local/cudnn`.

## Install Bazel

Fedora does not have bazel binary support directly. Hence, we need compile from source. Here we use a trick. I download a compiled `bazel 0.4.2` to solve the dependencies including `java`.

Download `bazel` installer from <https://github.com/bazelbuild/bazel/releases>. Type

```
chmod +x bazel-version-installer-os.sh
./bazel-version-installer-os.sh
```

You can set your custom `prefix` by `—prefix ~`. By default, it is `/usr/local`.

## Compile Tensorflow

Make sure that your `gcc` version is not later than 5. `CUDA` has not supported `gcc6`.

First, we need download the source code and configure.

```shell
git clone https://github.com/tensorflow/tensorflow
cd tensorflow
./configure
```

We have

```shell
./configure
Please specify the location of python. [Default is /home/jasonqsy/.pyenv/shims/python]:
Please specify optimization flags to use during compilation when bazel option "--config=opt" is specified [Default is -march=native]:
Do you wish to use jemalloc as the malloc implementation? [Y/n] n
jemalloc disabled
Do you wish to build TensorFlow with Google Cloud Platform support? [y/N] n
No Google Cloud Platform support will be enabled for TensorFlow
Do you wish to build TensorFlow with Hadoop File System support? [y/N] n
No Hadoop File System support will be enabled for TensorFlow
Do you wish to build TensorFlow with the XLA just-in-time compiler (experimental)? [y/N] n
No XLA JIT support will be enabled for TensorFlow
Found possible Python library paths:
  /home/jasonqsy/.pyenv/versions/anaconda3-4.3.0/lib/python3.6/site-packages
Please input the desired Python library path to use.  Default is [/home/jasonqsy/.pyenv/versions/anaconda3-4.3.0/lib/python3.6/site-packages]

Using python library path: /home/jasonqsy/.pyenv/versions/anaconda3-4.3.0/lib/python3.6/site-packages
Do you wish to build TensorFlow with OpenCL support? [y/N] n
No OpenCL support will be enabled for TensorFlow
Do you wish to build TensorFlow with CUDA support? [y/N] y
CUDA support will be enabled for TensorFlow
Please specify which gcc should be used by nvcc as the host compiler. [Default is /usr/bin/gcc]: /home/jasonqsy/gcc54/bin/gcc
Please specify the CUDA SDK version you want to use, e.g. 7.0. [Leave empty to use system default]: 8.0
Please specify the location where CUDA 8.0 toolkit is installed. Refer to README.md for more details. [Default is /usr/local/cuda]: /usr/local/cuda-8.0
Please specify the Cudnn version you want to use. [Leave empty to use system default]:
Please specify the location where cuDNN  library is installed. Refer to README.md for more details. [Default is /usr/local/cuda-8.0]: /usr/local/cudnn
Please specify a list of comma-separated Cuda compute capabilities you want to build with.
You can find the compute capability of your device at: https://developer.nvidia.com/cuda-gpus.
Please note that each additional compute capability significantly increases your build time and binary size.
[Default is: "3.5,5.2"]: 3.5,5.2
........
INFO: All external dependencies fetched successfully.
Configuration finished
```

Then

```shell
bazel build --config=opt --config=cuda //tensorflow/tools/pip_package:build_pip_package
```
My desktop used about 40 minutes to compile it.
```shell
bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg
pip install /tmp/tensorflow_pkg/tensorflow-1.0.1-cp36-cp36m-linux_x86_64.whl
```

We have finished the installation. But we still need some hacks. It seems there is a bug in `anaconda3`.

```Shell
mv .pyenv/versions/anaconda3-4.3.0/lib/libstdc++.so.6 .pyenv/versions/anaconda3-4.3.0/lib/libstdc++.so.6.bak
cp ~/gcc54/lib64/libstdc++.so.6 .pyenv/versions/anaconda3-4.3.0/lib/
```

## Validation

Run

```shell
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
```

which shows

```shell
2017-03-25 03:16:08.263158: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:901] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2017-03-25 03:16:08.263366: I tensorflow/core/common_runtime/gpu/gpu_device.cc:887] Found device 0 with properties:
name: GeForce GTX 950
major: 5 minor: 2 memoryClockRate (GHz) 1.3165
pciBusID 0000:01:00.0
Total memory: 1.95GiB
Free memory: 1.84GiB
2017-03-25 03:16:08.263380: I tensorflow/core/common_runtime/gpu/gpu_device.cc:908] DMA: 0
2017-03-25 03:16:08.263384: I tensorflow/core/common_runtime/gpu/gpu_device.cc:918] 0:   Y
2017-03-25 03:16:08.263930: I tensorflow/core/common_runtime/gpu/gpu_device.cc:977] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce GTX 950, pci bus id: 0000:01:00.0)
```

## Reference

- [Installing Bazel](https://bazel.build/versions/master/docs/install.html)
- [How to Install TensorFlow on Fedora with CUDA GPU acceleration](https://testinggetsreal.com/2016/12/27/how-to-install-tensorflow-on-fedora-with-cuda-gpu-acceleration/)
- [Installing TensorFlow from Sources](https://www.tensorflow.org/install/install_sources)
- [Installing GCC](https://gcc.gnu.org/wiki/InstallingGCC)
- [“'CXXABI_1.3.8' not found” in tensorflow-gpu - install from source](http://stackoverflow.com/questions/39844772/cxxabi-1-3-8-not-found-in-tensorflow-gpu-install-from-source)
- [NVIDIA CUDA Installation Guide for Linux](http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)
