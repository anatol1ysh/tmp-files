If you are really sure you want to disable swapping (note: this is not recommended, even where you are pretty sure that physical RAM is more than enough), follow these steps:
1. run swapoff -a: this will immediately disable swap
2. remove any swap entry from /etc/fstab
3. reboot the system. If the swap is gone, good. If, for some reason, it is still here, you had to remove the swap partition. Repeat steps 1 and 2 and, after that, use fdisk or parted to remove the (now unused) swap partition. Use great care here: removing the wrong partition will have disastrous effects!