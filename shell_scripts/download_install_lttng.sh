# LTTng 2.13
cd /root/LTTng && rm -rf *

cd /root/LTTng && wget https://lttng.org/files/lttng-modules/lttng-modules-latest-2.13.tar.bz2 && \
tar -xf lttng-modules-latest-2.13.tar.bz2 && \ 
cd lttng-modules-2.13.* && \
make && \
sudo make modules_install && \
sudo depmod -a

cd /root/LTTng && wget https://lttng.org/files/lttng-ust/lttng-ust-latest-2.13.tar.bz2 && \
tar -xf lttng-ust-latest-2.13.tar.bz2 && \
cd lttng-ust-2.13.* && \
./configure && \
make && \
sudo make install && \
sudo ldconfig

cd /root/LTTng && wget https://lttng.org/files/lttng-tools/lttng-tools-latest-2.13.tar.bz2 && \
tar -xf lttng-tools-latest-2.13.tar.bz2 && \
cd lttng-tools-2.13.* && \
./configure && \
make && \
sudo make install && \
sudo ldconfig