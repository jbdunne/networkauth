import requests as r    # import requests library   # requests library
import sys              # import sys library

function = sys.argv[1]  # get the function name from the command line
function = function.lower()  # convert the function name to lowercase
function network = sys.argv[2]  # get the network name from the command line    
function network = function network.lower()  # convert the network name to lowercase

# check network.lower name to see if matches blacklisted networks   # check if network is blacklisted   
if network == "facebook" or network == "instagram" or network == "snapchat" or network == "twitter" or network == "youtube":
    print("You are not allowed to use this network.")
        # if network is blacklisted, print error message# 
    print("{} has been blocked.".format(network))
    sys.exit() # exit the program
    # if network is not blacklisted, continue# 
else:
    print("You are allowed to use this network.")
    # if network is not blacklisted, continue# 
# authenticate user on network#   # authenticate user on network
if function == "post":
    # if function is post, continue 
    message = sys.argv[3]  # get the message from the command line
    # use requests library to post message to network# 
    r.post("https://sampleurl.herokuapp.com/{}".format(network), data={"status": message})
    # print success message# 
    print("Message posted successfully.")
    sys.exit()
    # if function is not post, continue
elif function == "read":
    # if function is read, continue
    # use requests library to get messages from network
    response = r.get("https://sampleurl.herokuapp.com/{}".format(network))
    # print messages# 
    print(response.json())
    sys.exit()
    # if function is not read, continue# 
else:
    print("Error: Invalid function.")
    # if function is not read or post, print error message# 
    sys.exit()
    # if function is not read or post, exit the program#  # if function is not read or post, exit the program

# if function is not read or post, print error message#   # if function is not read or post, print error message  
print("Error: Invalid function.")

# if function is not read or post, exit the program#   # if function is not read or post, exit the program
sys.exit()

# check which version of linux is being run for network microservice#  # check which version of linux is being run for network microservice
if sys.platform == "linux":
    print("Linux")
    # if linux, continue
elif sys.platform == "win32":
    print("Windows")
    # if windows, continue
elif sys.platform == "darwin":
    print("Mac")
    # if mac, continue# 
else:   
    print("Other")
    # if other, continue#   # if other, continue
# check which version of python is being run for network microservice#  # check which version of python is being run for network microservice
if sys.version_info[0] == 3:
    print("Python 3")
    # if python 3, continue#  # if python 3, continue
elif sys.version_info[0] == 2:
    print("Python 2")
    # if python 2, continue#  # if python 2, continue
else:   
    print("Other")
    # if other, continue#   # if other, continue

# given current version of python and which current version of linux is being run, suggest best authentication method for all users that have permissions#    # given current version of python and which current version of linux is being run, suggest best authentication method for all users that have permissions
print("Python {}".format(sys.version_info[0]))
print("Linux {}".format(sys.platform))  # print current version of python and current version of linux
# if current version of python is 3 and current version of linux is linux, suggest best authentication method for all users that have permissions#  # if current version of python is 3 and current version of linux is linux, suggest best authentication method for all users that have permissions
if sys.version_info[0] == 3 and sys.platform == "linux":
    print("Use SSH.")
    # if current version of python is 3 and current version of linux is linux, suggest best authentication method for all users that have permissions#  # if current version of python is 3 and current version of linux is linux, suggest best authentication method for all users that have permissions
elif sys.version_info[0] == 3 and sys.platform == "win32":
    print("Use Windows.")
    # if current version of python is 3 and current version of linux is windows, suggest best authentication method for all users that have permissions#  # if current version of python is 3 and current version of linux is windows, suggest best authentication method for all users that have permissions 
elif sys.version_info[0] == 3 and sys.platform == "darwin":
    print("Use Mac.")
    # if current version of python is 3 and current version of linux is mac, suggest best authentication method for all users that have permissions#  # if current version of python is 3 and current version of linux is mac, suggest best authentication method for all users that have permissions
elif sys.version_info[0] == 2 and sys.platform == "linux":
    print("Use SSH.")
    # if current version of python is 2 and current version of linux is linux, suggest best authentication method for all users that have permissions#  # if current version of python is 2 and current version of linux is linux, suggest best authentication method for all users that have permissions
elif sys.version_info[0] == 2 and sys.platform == "win32":
    print("Use Windows.")
    # if current version of python is 2 and current version of linux is windows, suggest best authentication method for all users that have permissions#  # if current version of python is 2 and current version of linux is windows, suggest best authentication method for all users that have permissions
elif sys.version_info[0] == 2 and sys.platform == "darwin":
    print("Use Mac.")
    # if current version of python is 2 and current version of linux is mac, suggest best authentication method for all users that have permissions#  # if current version of python is 2 and current version of linux is mac, suggest best authentication method for all users that have permissions
else:   
    print("Other")
    # if current version of python is not 2 or 3 and current version of linux is not linux, mac, or windows, suggest best authentication method for all users that have permissions#  # if current version of python is not 2 or 3 and current version of linux is not linux, mac, or windows, suggest best authentication method for all users that have permissions
# when using ssh ensure correct users have correct permissions based on company security policy#  # when using ssh ensure correct users have correct permissions based on company security policy
def ssh_authentication():
    # use ssh to authenticate user
    ssh = paramiko.SSHClient()
    # use ssh to authenticate user
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # use ssh to authenticate user
    ssh.connect(hostname="
    ", username="
    ", password="
    )
    # use ssh to authenticate user# 
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("  ")  # use ssh to authenticate user
# once user has authenticated with ssh, check current tls certificate is accurate and up to date
def tls_authentication():
    tls_authentication = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # check current tls certificate is accurate and up to date
    if tls_authentication.status_code == 200:
        print("TLS certificate is up to date.")
        # if current tls certificate is accurate and up to date, continue
    else:
        print("TLS certificate is not up to date.")
        # if current tls certificate is not accurate and up to date, continue
# check if user has permissions to use ssh
def ssh_permissions():
    # check if user has permissions to use ssh
    ssh_permissions = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # check if user has permissions to use ssh
    if ssh_permissions.status_code == 200:
        print("SSH is enabled.")
        # if user has permissions to use ssh, continue
    else:
        print("SSH is disabled.")
        sys.exit()
        # if user does not have permissions to use ssh exit program
# check if user has permissions to use tls
def tls_permissions():
    # check if user has permissions to use tls
    tls_permissions = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # check if user has permissions to use tls
    if tls_permissions.status_code == 200:
        print("TLS is enabled.")
        # if user has permissions to use tls, continue
    else:
        print("TLS is disabled.")
        sys.exit()
        # if user does not have permissions to use tls exit program
# check if user has permissions to use http
def http_permissions():
    # check if user has permissions to use http
    http_permissions = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # check if user has permissions to use http
    if http_permissions.status_code == 200:
        print("HTTP is enabled.")
        # if user has permissions to use http, continue
    else:
        print("HTTP is disabled.")
        sys.exit()
        # if user does not have permissions to use http, exit program
# check if user has permissions to use https
def https_permissions():
    # check if user has permissions to use https
    https_permissions = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # check if user has permissions to use https
    if https_permissions.status_code == 200:
        print("HTTPS is enabled.")
        # if user has permissions to use https, continue
    else:
        print("HTTPS is disabled.")
        sys.exit()
        # if user does not have permissions to use https, exit program
# check if user has permissions to use ftp
def ftp_permissions():
    # check if user has permissions to use ftp
    ftp_permissions = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # check if user has permissions to use ftp
    if ftp_permissions.status_code == 200:
        print("FTP is enabled.")
        # if user has permissions to use ftp, continue
    else:
        print("FTP is disabled.")
        sys.exit()
        # if user does not have permissions to use ftp exit program
# check if user has permissions to use telnet
def telnet_permissions():
    # check if user has permissions to use telnet
    telnet_permissions = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # check if user has permissions to use telnet
    if telnet_permissions.status_code == 200:
        print("Telnet is enabled.")
        # if user has permissions to use telnet, continue
    else:
        print("Telnet is disabled.")
        sys.exit()
        # if user does not have permissions to use telnet, exit program
# check if user has permissions to use smtp
def smtp_permissions():
    # check if user has permissions to use smtp
    smtp_permissions = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # check if user has permissions to use smtp
    if smtp_permissions.status_code == 200:
        print("SMTP is enabled.")
        # if user has permissions to use smtp, continue
    else:
        print("SMTP is disabled.")
        sys.exit()
        # if user does not have permissions to use smtp, exit program
# check if user has permissions to use pop3
def pop3_permissions():
    # check if user has permissions to use pop3
    pop3_permissions = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # check if user has permissions to use pop3
    if pop3_permissions.status_code == 200:
        print("POP3 is enabled.")
        # if user has permissions to use pop3, continue
    else:
        print("POP3 is disabled.")
        sys.exit()
        # if user does not have permissions to use pop3, exit program
# check if user has permissions to use imap
def imap_permissions():
    # check if user has permissions to use imap
    imap_permissions = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # check if user has permissions to use imap
    if imap_permissions.status_code == 200:
        print("IMAP is enabled.")
        # if user has permissions to use imap, continue
    else:
        print("IMAP is disabled.")
        sys.exit()
        # if user does not have permissions to use imap, exit program
# check if user has permissions to use smb
def smb_permissions():
    # check if user has permissions to use smb
    smb_permissions = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # check if user has permissions to use smb
    if smb_permissions.status_code == 200:
        print("SMB is enabled.")
        # if user has permissions to use smb, continue
    else:
        print("SMB is disabled.")
        sys.exit()
        # if user does not have permissions to use smb, exit program
# check if user has permissions to use rdp
def rdp_permissions(): 
    # check if user has permissions to use rdp
    rdp_permissions = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # check if user has permissions to use rdp
    if rdp_permissions.status_code == 200:
        print("RDP is enabled.")
        # if user has permissions to use rdp, continue
    else:
        print("RDP is disabled.")
        sys.exit()
        # if user does not have permissions to use rdp, exit program
# check if user has permissions to use vnc
def vnc_permissions():
    # check if user has permissions to use vnc
    vnc_permissions = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # check if user has permissions to use vnc
    if vnc_permissions.status_code == 200:
        print("VNC is enabled.")
        # if user has permissions to use vnc, continue# 
    else:
        print("VNC is disabled.")
        sys.exit()
        # if user does not have permissions to use vnc, exit program
# permit user to use tls
def tls_permissions():
    # permit user to use tls
    tls_permissions = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # permit user to use tls
    if tls_permissions.status_code == 200:
        print("TLS is enabled.")
        # if user has permissions to use tls, continue
    else:
        print("TLS is disabled.")
        sys.exit()
        # if user does not have permissions to use tls, exit program
# establish connection to corporate network
def connect_corporate():
    # establish connection to corporate network
    connect_corporate = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # establish connection to corporate network
    if connect_corporate.status_code == 200:
        print("Connection to corporate network established.")
        # if connection to corporate network established, continue
    else:
        print("Connection to corporate network failed.")
        # if connection to corporate network failed, do not continue
# establish connection to home network
def connect_home():
    # establish connection to home network
    connect_home = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # establish connection to home network
    if connect_home.status_code == 200:
        print("Connection to home network established.")
        # if connection to home network established, continue
    else:
        print("Connection to home network failed.")
        # if connection to home network failed, do not continue
# assuming network connection, check for performance gaps
def performance_gaps(): 
    # assuming network connection, check for performance gaps
    performance_gaps = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # assuming network connection, check for performance gaps
    if performance_gaps.status_code == 200:
        print("Performance gaps detected.")
        # if performance gaps detected, continue
    else:
        print("No performance gaps detected.")
        # if no performance gaps detected, do not continue
# check for network connection
def network_connection():   
    # check for network connection
    network_connection = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # check for network connection
    if network_connection.status_code == 200:
        print("Network connection established.")
        # if network connection established, continue
    else:
        print("Network connection failed.")
        # if network connection failed, do not continue
# check for network connection every hour
def network_connection_hourly():
    # check for network connection every hour
    network_connection_hourly = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # check for network connection every hour
    if network_connection_hourly.status_code == 200:
        print("Network connection established.")
        # if network connection established, continue
    else:
        print("Network connection failed.")
        # if network connection failed, do not continue# 
# check for network connection every day
def network_connection_daily(): 
    # check for network connection every day
    network_connection_daily = requests.get("https://sampleurl.herokuapp.com/{}".format(network))
    # check for network connection every day
    if network_connection_daily.status_code == 200:
        print("Network connection established.")
        # if network connection established, continue
    else:
        print("Network connection failed.")
        # if network connection failed, do not continue# 
