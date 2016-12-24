Title: The Installation of Shadowsocks on Ubuntu Server
Category: Unix/Linux
Date: 2016-2-10
Modified: 2016-2-10
Tags: Ubuntu Server

# Environment
- Ubuntu Server 14.04
- With apt-get, python2, pip2, vim
- I use shadowsocks-python

My Ubuntu Server has apt-get, python2 and vim initially. Thus, I installed pip by apt-get.
```
apt-get install python-pip
```

# Installation
With the environment, it is very convenient to install shadowsocks.
```
pip install shadowsocks
```

# Basic Configuration
There is only one configuration json-file. It does not matter what you put it in and name it with *.js or *.json. Here I put it in /etc/shadowsocks/config.json
```
mkdir /etc/shadowsocks
cd /etc/shadowsocks
vim config.json
```
Then, input according to the documentation:(Basic)
```
{
    "server":"100.000.000.00",
    "server_port":8388,
    "local_port":1080,
    "password":"123456",
    "timeout":600,
    "method":"aes-256-cfb"
}
```
Replace 100.000.000.00 with your Server IP.
Note that aes-256-cfb needs addtional tools like this: (Maybe it can also be installed by pip)
```
apt-get install python-m2crypto
```

# Setup

## Test
ssserver is installed with shadowsocks. (I guess its meaning is shadow-socks-server)
You can test shadowsocks like this:
```
ssserver -c /etc/shadowsocks/config.json
```
Do not close the Terminal, and you can test if shadowsocks works normally.
## Formal Setup
When it works normally, you can enter:
```
nohup ssserver -c /etc/shadowsocks/config.json &gt; log&amp;
```
Or  jusr auto-setup when starting (I prefer it).
Add this line into /etc/rc.local
```
/usr/local/bin/ssserver -c /etc/shadowsocks/config.js -d start
```
Then reboot the vps:
```
reboot
```

# Multiple users
The basic configuration is just for single-user. If you want to share shadowsocks with your friends, you can assign specfic port and password to them.
```
{
    "server":"100.000.000.00",
    "timeout":600,
    "method":"aes-256-cfb",
    "port_password":
    {
        "8388":"123456",
        "8389":"654321"
    },
    "_comment":
    {
        "8388": "user1",
        "8389": "user2"
    }
}
```
"user1" and "user2" can be arbitrary. Actually, the port is one's username and port_password is one's password.
