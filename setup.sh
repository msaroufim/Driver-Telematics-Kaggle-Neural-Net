sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y dist-upgrade
sudo apt-get -y install git make python-dev python-setuptools libblas-dev gfortran g++ python-pip python-numpy python-scipy liblapack-dev
sudo apt-get install pkg-config
sudo apt-get install freetype*
sudo apt-get install libfreetype6-dev libpng-dev
sudo pip install matplotlib
sudo pip install "ipython[all]"
sudo apt-get install screen
sudo pip install --upgrade git+git://github.com/Theano/Theano.git
wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1204/x86_64/cuda-repo-ubuntu1204_5.5-0_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1204_5.5-0_amd64.deb
sudo apt-get update
sudo apt-get install cuda
#THEANO_FLAGS=floatX=float32,device=gpu0 python /usr/local/lib/python2.7/dist-packages/theano/misc/check_blas.py
git clone git://github.com/lisa-lab/pylearn2.git
cd pylearn2
sudo python setup.py develop
cd ..
echo "export PATH=/usr/local/cuda-5.5/bin:$PATH" >> .bashrc
echo "export LD_LIBRARY_PATH=/usr/local/cuda-5.5/lib64:$LD_LIBRARY_PATH" >> .bashrc
echo "export PYLEARN2_DATA_PATH=/home/ubuntu/data" >> .bashrc
source .bashrc	
mkdir -p data/mnist/
cd data/mnist/
wget http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
gunzip train-images-idx3-ubyte.gz
wget http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
gunzip train-labels-idx1-ubyte.gz
wget http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
gunzip t10k-images-idx3-ubyte.gz
wget http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
gunzip t10k-labels-idx1-ubyte.gz
cd ../..
echo '[global]
floatX = float32
device = gpu0

[nvcc]
fastmath = True' > .theanorc
