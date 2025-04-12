# LTTng 2.13

cd /root/LTTng && cd lttng-modules-2.13.* && \
make && \
sudo make modules_install && \
sudo depmod -a

cd /root/LTTng && cd lttng-ust-2.13.* && \
./configure && \
make && \
sudo make install && \
sudo ldconfig

cd /root/LTTng && cd lttng-tools-2.13.* && \
./configure && \
make && \
sudo make install && \
sudo ldconfig