#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ opstfunctions.py              [Update: 2022-04-16 | 11:29 PM] #
#---[Info]------------------------------------------------------------------#
#  {The OmegaDSToolkit is a product of Delta_Society™ by MyMeepSQL}         #
#                                                                           #
#  The file wich include all functions                                      #
#  Language  ~  Python3                                                     #
#---[Author]----------------------------------------------------------------#
#  Thomas Pellissier ~ @MyMeepSQL                                           #
#  Copyright (C) 2022 MyMeepSQL - © Delta_Society™                          #
#---[Operating System]------------------------------------------------------#
#  Developed for linux                                                      #
#---[Licence]---------------------------------------------------------------#
#  GNU General Public License v3.0                                          #
#  -------------------------------                                          #
#                                                                           #
#  This program is free software; you can redistribute it and/or modify     #
#  it under the terms of the GNU General Public License as published by     #
#  the Free Software Foundation; either version 2 of the License, or        #
#  (at your option) any later version.                                      #
#                                                                           #
#  This program is distributed in the hope that it will be useful,          #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the             #
#  GNU General Public License for more details.                             #
#                                                                           #
#  You should have received a copy of the GNU General Public License along  #
#  with this program; if not, write to the Free Software Foundation, Inc.,  #
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.              #
#---------------------------------------------------------------------------#

# Import section
# try:
import os,sys,socket,urllib.request,subprocess,re,uuid,requests,json,psutil,GPUtil
from requests.exceptions import Timeout
from opstcolors import *
from opstversions import *
# except ModuleNotFoundError:
#     print()
#     criticalmsg = f"{B}[{W}CRITICAL{B}]{GR}   A current(s) module(s) was not installed, run the {B}opstsetup{W} for install it. ({B}sudo opstsetup install{W})\n"
#     sys.exit(criticalmsg)
# except NameError:
#     print()
#     criticalmsg = f"{B}[{W}CRITICAL{B}]{GR}   A current(s) module(s) was not installed, run the {B}opstsetup{W} for install it. ({B}sudo opstsetup install{W})\n"
#     sys.exit(criticalmsg)
####


# Functions
## Main functions
def abort():
    print()
    abortmsg = f"{R}[!]{GR}  User aborted\n"
    exit(abortmsg)

def criticalmsg():
    print()
    criticalmsg = f"{B}[{W}CRITICAL{B}]{GR}  A current(s) module(s) was not installed, run the {B}opstsetup{W} for install it. ({B}sudo opstsetup install{W})\n"
    exit(criticalmsg)
def not_linux():
    print()
    criticalmsg = f"{B}[{R}ERROR{B}]{R} You tried to run OPST on a non-linux machine. OPST can be run only on a Linux kernel.\n{W}"
    sys.exit(criticalmsg)

def connexion(host='https://google.com'):
    try:
        urllib.request.urlopen(host, timeout=10)    # Check if the user have an Internet connection
        return True
    except:
        return False


# Get the private IP of the machine (for show in the menu of OPST)
GET_IP_CMD ='hostname -I'
def run_cmd(cmd):
     return subprocess.check_output(cmd, shell=True).decode('utf-8')
privateIP = run_cmd(GET_IP_CMD)
####

# Get the public IP of the user on Internet (for show in the menu of OPST)
def getPublicIP():
    try:
        endpoint = 'https://ipinfo.io/json'
        response = requests.get(endpoint, verify = True, timeout=5)
        if response.status_code != 200:
            return 'Status:', response.status_code, 'Problem with the request. Exiting.'
        data = response.json()
        return data['ip']
    except Timeout:
        publicIP=f"{R}Not connected{W}"
        return publicIP
global publicIP
publicIP = getPublicIP()
####

# Get the MAC adress (for show in the menu of OPST)
global MAC_adress
MAC_adress= ':'.join(re.findall('..', '%012x' %uuid.getnode()))
###

# Get GPU details
def gpudetails():
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        global GPU_details_id
        global GPU_details_gpuName
        global GPU_details_load
        global GPU_details_freeMemory
        global GPU_details_usedMemory
        global GPU_details_totalMemoy
        global GPU_details_temperature
        global GPU_details_uuid 

        # get the GPU id
        GPU_details_id = gpu.id
        # name of GPU
        GPU_details_gpuName = gpu.name
        # get % percentage of GPU usage of that GPU
        GPU_details_load = f"{gpu.load*100}%"
        # get free memory in MB format
        GPU_details_freeMemory = f"{gpu.memoryFree}MB"
        # get used memory
        GPU_details_usedMemory = f"{gpu.memoryUsed}MB"
        # get total memory
        GPU_details_totalMemoy = f"{gpu.memoryTotal}MB"
        # get GPU temperature in Celsius
        GPU_details_temperature = f"{gpu.temperature} °C"
        GPU_details_uuid = gpu.uuid
####

def cls():
    os.system('clear')

def exitodst():
    exitodst = f"\n{bC}[{gC}Goodby{bC}]{r}\n"
    exit(exitodst)

def error():
    print(f"{bC}[{rC2}!{bC}]{bC}─[{gC}Choose a option{bC}]{r}")                 # if the user doesn't choose option
    input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to retry{bC}]{r}")      #

def y_or_n_error():
    print(f"{bC}[{rC2}!{bC}]{bC}─[{gC}Chose y or n{bC}]{r}")                     # If the user does not choose "y" or "n"
    input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to retry{bC}]{r}")       #

"""
=====================
Colors informations :
=====================
{R} = Option
{O} = Option's argument 
{G} = Option and argument (not with option, for exemple 'nmap 1.1.1.1', the '1.1.1.1' is a argument with no option)
{B} = Command (for exemple 'clear' or 'leave')
{P} = The eaqual caractere (=)
"""

# The help commands section

def mainpage_helpmsg():
    print(f"""
{GR}{D} _______ ______ _______ _______ {W}
{GR}{D}|       |   __ \     __|_     _|{W}{G}  OmegaPSToolkit {D}v{opstconsole_version}
{GR}{D}|   -   |    __/__     | |   |  {W}{D}  A massive penetration testing toolkit
{GR}{D}|_______|___|  |_______| |___|  {C}{D}  https://github.com/MyMeepSQL/OmegaPSToolkit{W}

All commands of the OmegaDSToolkit you can use is the main page

{B}COMMAND:{W}
    1           ::   Go to the Information Gathering page
    2           ::   Go to the Wireless Tools page
    3           ::   Go to the Usefull tools page
    cli         ::   Use the opstconsole like a CLI
    help        ::   Show this help message
    exit        ::   Exit opstconsole
    """)
    input(f"{bC}[{rC2}-{bC}]{bC}─[{gC}Press [ENTER] key to continue{bC}]{r}")
###


## CLI functions

### Info

def cli_infomsg():
    print(f"""
{GR}{D} _______ ______ _______ _______ {W}
{GR}{D}|       |   __ \     __|_     _|{W}{G}  OmegaPSToolkit CLI {D}v{opstconsole_cli_version}
{GR}{D}|   -   |    __/__     | |   |  {W}{D}  A massive penetration testing toolkit
{GR}{D}|_______|___|  |_______| |___|  {C}{D}  https://github.com/MyMeepSQL/OmegaPSToolkit{W}

{G}[>]{W} Some informations about the OmegaPSToolkit and other
{G}[*]{W} This is the small version, for all informations, run {B}fullinfo{W}

{C}Informations about OmegaPSToolkit{GR}:{W}

    {G}All OPST commands versions{GR}:{W}
        opstconsole             v{opstconsole_version}
        odstconsole CLI         v{opstconsole_cli_version}
        opstupdate              {opstupdate_version}
        opsthelp                v{opsthelp_version}
        odstsetup               {opstsetup_version}
        odstinstall-all         {opstinstallall_version}

    {G}Other informations{GR}:{W}
        GitHub page             {underscore}{C}https://github.com/MyMeepSQL/OmegaPSToolkit{W}

{C}Informations about author{GR}:{W}

    {G}General informations{GR}:{W}
        Author                  {italic}Thomas Pellissier{W}
        Codename                {G}@{W}MyMeepSQL{W} or {G}@{W}th300905{W}
        Email                   {P}thomas.pellissier@outlook.com{W} ({R}only for professional{W} or for {G}repport bugs of OmegaPSToolkit{W})
        Owner                   {italic}Copyright © 2021-2022 PSociety™{W}, {R}All rights reserved{W}.

{C}Ohter informations{GR}:{W}

    {G}Other versions{GR}:{W}
        Python's version        v{python_version}
        
    {G}System{GR}:{W}
        Operating System        {OS}
        Distribution / Release  {distribution}
""")


### Fullinfo
def TEST():
    print("GPU details:""")
    import GPUtil
    gpus = GPUtil.getGPUs()
    for gpu in gpus:

        # get the GPU id
        GPU_details_id = gpu.id
        # name of GPU
        GPU_details_gpuName = gpu.name
        # get % percentage of GPU usage of that GPU
        GPU_details_load = f"{gpu.load*100}%"
        # get free memory in MB format
        GPU_details_freeMemory = f"{gpu.memoryFree}MB"
        # get used memory
        GPU_details_usedMemory = f"{gpu.memoryUsed}MB"
        # get total memory
        GPU_details_totalMemoy = f"{gpu.memoryTotal}MB"
        # get GPU temperature in Celsius
        GPU_details_temperature = f"{gpu.temperature} °C"
        GPU_details_uuid = gpu.uuid

        print(rf"""
Card {GPU_details_id}:                                                                             /│\
    Name               {GPU_details_gpuName}                                        / │ \
    Total memory       {GPU_details_totalMemoy}                                                   /  │  \
    Free memory        {GPU_details_freeMemory}                                                      │
    Loaded memory      {GPU_details_load}
    Used memory        {GPU_details_usedMemory}                                                        │
    UUID               {GPU_details_uuid}                      │    Scroll up for the main informations
            """)

def cli_fullinfomsg():
    print(f"""
{GR}{D} ______  ______ _______ _______ {W}
{GR}{D}|       |   __ \     __|_     _|{W}{G}  OmegaPSToolkit {D}v{opsthelp_version} (opsthelp's version)
{GR}{D}|   -   |    __/__     | |   |  {W}{D}  A massive penetration testing toolkit
{GR}{D}|_______|___|  |_______| |___|  {C}{D}  https://github.com/MyMeepSQL/OmegaPSToolkit{W}

{G}[>]{W} All informations about OmegaPSToolkit and other{W}
{G}[*]{W} This is the biggest version, for less informations, run {B}info{W}

{C}Informations about OmegaPSToolkit{GR}:{W}

    {G}Main commands{GR}:{W}
        odstconsole                Start the current tool
        odstupdate                 Update OPST with the latest version from GitHub
        odsthelp                   Print this message and exit

    {G}Other commands (to install OPST the first time){GR}:{W}
        odstsetup                  Install all pip packages that OPST needs
        odstinstall-all            Update you system, copy OPST to {G}"{C}/usr/share/OmegaPSToolkit{G}"{W} and write all comamnds in {G}"{C}/usr/bin/{G}"{W}

    {G}All OPST commands versions{GR}:{W}
        opstconsole                v{opstconsole_version}
        odstconsole CLI            v{opstconsole_cli_version}
        opstupdate                 {opstupdate_version}
        opsthelp                   v{opsthelp_version}
        odstsetup                  {opstsetup_version}
        odstinstall-all            {opstinstallall_version}

    {G}Other informations{GR}:{W}
        GitHub page                {underscore}{C}https://github.com/MyMeepSQL/OmegaPSToolkit{W}
        Changelogs                 {underscore}{C}https://github.com/MyMeepSQL/OmegaPSToolkit/blob/main/CHANGLOG.md{W}

{C}Informations about author{GR}:{W}

    {G}General informations{GR}:{W}
        Author                     {italic}Thomas Pellissier{W}
        Codename                   {G}@{W}MyMeepSQL{W} or {G}@{W}th300905{W}
        Email                      {P}thomas.pellissier@outlook.com{W} ({R}only for professional{W} or for {G}repport bugs of OmegaPSToolkit{W})
        Owner                      {italic}Copyright © 2021-2022 PSociety™{W}, {R}All rights reserved{W}.

    {G}Other informations{GR}:{W}
        GitHub profile             {underscore}{C}https://github.com/MyMeepSQL{W}
        Twitter profile            {C}@{W}MyMeepSQL

{C}Ohter informations{GR}:{W}

    {G}Other versions{GR}:{W}
        Python's version           v{python_version}

    {G}Network{GR}:{W}
        Private IP                 {O}{privateIP}{W}        Public IP                  {O}{publicIP}{W}
        MAC adress                 {O}{MAC_adress}{W}

        {G}Details {W}({C}with all inrefaces{W}){GR}:{W} """)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"            Interface: {C}{interface_name}{W}")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"""                  IP Address:      {O}{address.address}{W}
                  Netmask:         {O}{address.netmask}{W}
                  Broadcast IP:    {O}{address.broadcast}{W}""")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"""                  MAC Address:     {O}{address.address}{W}
                  Netmask:         {O}{address.netmask}{W}
                  Broadcast MAC:   {O}{address.broadcast}{W}""")
    print(f"""
    {G}System{GR}:{W}
        Operating System           {OS}
        Distribution / Release     {distribution}
        PC's Name                  {my_system.node}
        Machine                    {my_system.machine}
        Processor                  {my_system.processor}""")

    print("GPU details:""")
    import GPUtil
    gpus = GPUtil.getGPUs()
    for gpu in gpus:

        # get the GPU id
        GPU_details_id = gpu.id
        # name of GPU
        GPU_details_gpuName = gpu.name
        # get % percentage of GPU usage of that GPU
        GPU_details_load = f"{gpu.load*100}%"
        # get free memory in MB format
        GPU_details_freeMemory = f"{gpu.memoryFree}MB"
        # get used memory
        GPU_details_usedMemory = f"{gpu.memoryUsed}MB"
        # get total memory
        GPU_details_totalMemoy = f"{gpu.memoryTotal}MB"
        # get GPU temperature in Celsius
        GPU_details_temperature = f"{gpu.temperature} °C"
        GPU_details_uuid = gpu.uuid

        print(rf"""
Card {GPU_details_id}:                                                                             /│\
    Name               {GPU_details_gpuName}                                        / │ \
    Total memory       {GPU_details_totalMemoy}                                                   /  │  \
    Free memory        {GPU_details_freeMemory}                                                      │
    Used memory        {GPU_details_usedMemory}                                                        │
    UUID               {GPU_details_uuid}                      │    Scroll up for the main informations
            """)
### Help

def cli_helpmsg():
    print(f"""
{GR}{D} _______ ______ _______ _______ {W}
{GR}{D}|       |   __ \     __|_     _|{W}{G}  OmegaPSToolkit CLI {D}v{opstconsole_cli_version}
{GR}{D}|   -   |    __/__     | |   |  {W}{D}  A massive penetration testing toolkit
{GR}{D}|_______|___|  |_______| |___|  {C}{D}  https://github.com/MyMeepSQL/OmegaPSToolkit{W}

All commands of the OmegaDSToolkit CLI you can use is the main page

{C}COMMAND{GR}:{W}
    ping        ::  Send ICMP ECHO_REQUEST to network hosts
    nslookup    ::  Query Internet name servers interactively
    netstat     ::  Print network connections, routing tables, interface 
                      statistics, masquerade connections, and multicast memberships
    whois       ::  Client for the whois directory service
    traceroute  ::  Print the route packets trace to network host

{C}{D}OTHER COMMAND{GR}:{W}
    help        ::  Show this help message
    info        ::  Show informations about OSPT and other informations ({R}small version{W})
    fullinfo    ::  Show more informations ({R}largest version{W})
    clear       ::  Clear the terminal
    reset       ::  Reset to come back to the basic menu ({R}CLI{W})
    leave       ::  Exit opstconsole's CLI version ({R}return to opstconsole{W})
    exit        ::  Exit opstconsole
""")


### Ping command

def cli_ping_help():
    print(f"""
{G}Usage{GR}:
  {W} [{R}options{W}] <{G}destination{W}>

{C}Options{GR}:{W}
  <{G}destination{W}>         dns name or ip address
  -{R}a{W}                    use audible ping
  -{R}A{W}                    use adaptive ping
  -{R}B{W}                    sticky source address
  -{R}c{W} <{O}count{W}>            stop after <count> replies
  -{R}D{W}                    print timestamps
  -{R}d{W}                    use SO_DEBUG socket option
  -{R}f{W}                    flood ping
  -{R}h{W}                    print help and exit
  -{R}I{W} <{O}interface{W}>        either interface name or address
  -{R}i{W} <{O}interval{W}>         seconds between sending each packet
  -{R}L{W}                    suppress loopback of multicast packets
  -{R}l{W} <{O}preload{W}>          send <preload> number of packages while waiting replies
  -{R}m{W} <{O}mark{W}>             tag the packets going out
  -{R}M{W} <{O}pmtud opt{W}>        define mtu discovery, can be one of <do|dont|want>
  -{R}n{W}                    no dns name resolution
  -{R}O{W}                    report outstanding replies
  -{R}p{W} <{O}pattern{W}>          contents of padding byte
  -{R}q{W}                    quiet output
  -{R}Q{W} <{O}tclass{W}>           use quality of service <tclass> bits
  -{R}s{W} <{O}size{W}>             use <size> as number of data bytes to be sent
  -{R}S{W} <{O}size{W}>             use <size> as SO_SNDBUF socket option value
  -{R}t{W} <{O}ttl{W}>              define time to live
  -{R}U{W}                    print user-to-user latency
  -{R}v{W}                    verbose output
  -{R}V{W}                    print version and exit
  -{R}w{W} <{O}deadline{W}>         reply wait <deadline> in seconds
  -{R}W{W} <{O}timeout{W}>          time to wait for response

{C}IPv4 options{GR}:{W}
  -{R}4{W}                    use IPv4
  -{R}b{W}                    allow pinging broadcast
  -{R}R{W}                    record route
  -{R}T{W} <{O}timestamp{W}>        define timestamp, can be one of <tsonly|tsandaddr|tsprespec>

{C}IPv6 options{GR}:{W}
  -{R}6{W}                    use IPv6
  -{R}F{W} <{O}flowlabel{W}>        define flow label, default is random
  -{R}N{W} <{O}nodeinfo opt{W}>     use icmp6 node info query, try <help> as argument

{C}Commands{GR}:{W}
  {B}clear{W}                 clear the terminal
  {B}leave{W}                 leave the ping tool
  {B}man ping{W}              get all details about ping command

{C}Exemple{GR}:{W}
  -{R}c {O}4 {G}1.1.1.1{W}
  -{R}q {G}google.com{W}
  -{R}c {O}4 {G}https://duckduckgo.com{W}
""")


### Traceroute command

def cli_traceroute_help():
    print(f"""
{G}Usage{GR}:{W}
  [ -{R}46dFITnreAUDV{W} ] [ -{R}f {O}first_ttl{W} ] [ -{R}g {O}gate{W},... ] [ -{R}i {O}device{W} ] [ -{R}m max_ttl{W} ] 
  [ -{R}N {O}squeries{W} ] [ -{R}p {O}port{W} ] [ -{R}t {O}tos{W} ] [ -{R}l {O}flow_label{W} ] [ -{R}w {O}MAX{W},{O}HERE{W},{O}NEAR{W} ] 
  [ -{R}q {O}nqueries{W} ] [ -{R}s {O}src_addr{W} ] [ -{R}z {O}sendwait{W} ] [ --{R}fwmark{P}={O}num{W} ] {B}host{W} [ {O}packetlen{W} ]

{C}Options{GR}:{W}
  -{R}4{W}                            Use IPv4
  -{R}6{W}                            Use IPv6
  -{R}d{W}  --{R}debug{W}                   Enable socket level debugging
  -{R}F{W}  --{R}dont-fragment{W}           Do not fragment packets
  -{R}f{W} {O}first_ttl{W}  --{R}first{P}={O}first_ttl{W}
                                Start from the first_ttl hop (instead from 1)
  -{R}g{W} {O}gate{W},...  --{R}gateway{P}={O}gate{W},...
                                Route packets through the specified gateway
                                (maximum 8 for IPv4 and 127 for IPv6)
  -{R}I{W}  --{R}icmp{W}                    Use ICMP ECHO for tracerouting
  -{R}T{W}  --{R}tcp{W}                     Use TCP SYN for tracerouting (default port is 80)
  -{R}i{W} {O}device{W}  --{R}interface{P}={O}device{W}
                                Specify a network interface to operate with
  -{R}m{W} {O}max_ttl{W}  --{R}max-hops{P}={O}max_ttl{W}
                                Set the max number of hops (max TTL to be
                                reached). Default is 30
  -{R}N{W} {O}squeries{W}  --{R}sim-queries{P}={O}squeries{W}
                                Set the number of probes to be tried
                                simultaneously (default is 16)
  -{R}n{W}                            Do not resolve IP addresses to their domain names
  -{R}p{W} {O}port{W}  --{R}port{P}={O}port{W}          Set the destination port to use. It is either
                                initial udp port value for "default" method
                                (incremented by each probe, default is 33434), or
                                initial seq for "icmp" (incremented as well,
                                default from 1), or some constant destination
                                port for other methods (with default of 80 for
                                "tcp", 53 for "udp", etc.)
  -{R}t{W} {O}tos{W}  --{R}tos{P}={O}tos{W}             Set the TOS (IPv4 type of service) or TC (IPv6
                                traffic class) value for outgoing packets
  -{R}l{W} {O}flow_label{W}  --{R}flowlabel{P}={O}flow_label{W}
                                Use specified flow_label for IPv6 packets
  -{R}w{W} {O}MAX{W},{O}HERE{W},{O}NEAR{W}  --{R}wait{P}={O}MAX{W},{O}HERE{W},{O}NEAR{W}
                                Wait for a probe no more than HERE (default 3)
                                times longer than a response from the same hop,
                                or no more than NEAR (default 10) times than some
                                next hop, or MAX (default 5.0) seconds (float
                                point values allowed too)
  -{R}q{W} {O}nqueries{W}  --{R}queries{P}={O}nqueries{W}
                                Set the number of probes per each hop. Default is
                                3
  -{R}r{W}                            Bypass the normal routing and send directly to a
                                host on an attached network
  -{R}s{W} {O}src_addr{W}  --{R}source{P}={R}src_addr{W}
                                Use source src_addr for outgoing packets
  -{R}z{W} {O}sendwait{W}  --{R}sendwait{P}={O}sendwait{W}
                                Minimal time interval between probes (default 0).
                                If the value is more than 10, then it specifies a
                                number in milliseconds, else it is a number of
                                seconds (float point values allowed too)
  -{R}e{W}  --{R}extensions{W}              Show ICMP extensions (if present), including MPLS
  -{R}A{W}  --{R}as-path-lookups{W}         Perform AS path lookups in routing registries and
                                print results directly after the corresponding
                                addresses
  -{R}M{W} {O}name{W}  --{R}module{P}={O}name{W}        Use specified module (either builtin or external)
                                for traceroute operations. Most methods have
                                their shortcuts (`-I' means `-M icmp' etc.)
  -{R}O{W} {O}OPTS{W},...  --{R}options{P}={O}OPTS{W},...
                                Use module-specific option OPTS for the
                                traceroute module. Several OPTS allowed,
                                separated by comma. If OPTS is "help", print info
                                about available options
  --{R}sport{P}={R}num{W}                   Use source port num for outgoing packets. Implies
                                `-N 1'
  --{R}fwmark{P}={R}num{W}                  Set firewall mark for outgoing packets
  -{R}U{W}  --{R}udp{W}                     Use UDP to particular port for tracerouting
                                (instead of increasing the port per each probe),
                                default port is 53
  -{R}UL{W}                           Use UDPLITE for tracerouting (default dest port
                                is 53)
  -{R}D{W}  --{R}dccp{W}                    Use DCCP Request for tracerouting (default port
                                is 33434)
  -{R}P {O}prot{W}  --{R}protocol{P}={O}prot{W}      Use raw packet of protocol prot for tracerouting
  --{R}mtu{W}                         Discover MTU along the path being traced. Implies
                                `-F -N 1'
  --{R}back{W}                        Guess the number of hops in the backward path and
                                print if it differs
  -{R}V{W}  --{R}version{W}                 Print version info and exit
  --{R}help{W}                        Read this help and exit

{C}Arguments{GR}:{W}
+ {G}host{W}                          The host to traceroute to
  {O}packetlen{W}                     The full packet length (default is the length of an IP
                                header plus 40). Can be ignored or increased to a minimal
                                allowed value

{C}Commands{GR}:{W}
  {B}clear{W}                         Clear the terminal
  {B}leave{W}                         leave the {R}traceroute{W} tool
  {B}man traceroute{W}                get all details about {R}traceroute{W} command

{C}Exemple{GR}:{W}
  -{R}n{W} {G}8.8.8.8{W}
  -{R}n{W} -{R}p{W} {O}61600{W} {G}google.com{W}
""")



### NSLooukup

def cli_nslookup_help():
    print(f"""
{R}[!]{W}    The 'help' command is not yet implemented.
""")


### Whois

def cli_whois_help():
    print(f"""
{G}Usage{GR}:{W}
  [{R}OPTION{W}]... {G}OBJECT{W}...

  -{R}h {O}HOST{W}, --{R}host {O}HOST{W}   connect to server HOST
  -{R}p {O}PORT{W}, --{R}port {O}PORT{W}   connect to PORT
  -{R}I{W}                     query whois.iana.org and follow its referral
  -{R}H{W}                     hide legal disclaimers
      --{R}verbose{W}        explain what is being done
      --{R}help{W}           display this help and exit
      --{R}version{W}        output version information and exit

These flags are supported by whois.ripe.net and some RIPE-like servers:
  -{R}l{W}                     find the one level less specific match
  -{R}L{W}                     find all levels less specific matches
  -{R}m{W}                     find all one level more specific matches
  -{R}M{W}                     find all levels of more specific matches
  -{R}c{W}                     find the smallest match containing a mnt-irt attribute
  -{R}x{W}                     exact match
  -{R}b{W}                     return brief IP address ranges with abuse contact
  -{R}B{W}                     turn off object filtering (show email addresses)
  -{R}G{W}                     turn off grouping of associated objects
  -{R}d{W}                     return DNS reverse delegation objects too
  -{R}i {O}ATTR{W}[,{R}ATTR{W}]...      do an inverse look-up for specified ATTRibutes
  -{R}T {O}TYPE{W}[,{R}TYPE{W}]...      only look for objects of TYPE
  -{R}K{W}                     only primary keys are returned
  -{R}r{W}                     turn off recursive look-ups for contact information
  -{R}R{W}                     force to show local copy of the domain object even
                       if it contains referral
  -{R}a{W}                     also search all the mirrored databases
  -{R}s {O}SOURCE{W}[,{O}SOURCE{W}]...  search the database mirrored from SOURCE
  -{R}g {O}SOURCE:FIRST-LAST{W}   find updates from SOURCE from serial FIRST to LAST
  -{R}t {O}TYPE{W}                request template for object of TYPE
  -{R}v {O}TYPE{W}                request verbose template for object of TYPE
  -{R}q{W} [{R}version{W}|{R}sources{W}|{R}types{W}]  query specified server info
""")


## Netstat

def cli_netstat_help():
    print(f"""
{G}Usage{GR}:{W}
   [-{R}vWeenNcCF{W}] [<Af>] -{R}r{W}        ( netstat -{R}V{W}|--{R}version{W}|-{R}h{W}|--{R}help{W} )
   [-{R}vWnNcaeol{W}] [<Socket> ...]
   ( [-{R}vWeenNac{W}] -{R}i{W} | [-{R}cnNe{W}] -{R}M{W} | -{R}s{W} [-{R}6tuw{W}] )

        -{R}r{W}, --{R}route{W}              display routing table
        -{R}i{W}, --{R}interfaces{W}         display interface table
        -{R}g{W}, --{R}groups{W}             display multicast group memberships
        -{R}s{W}, --{R}statistics{W}         display networking statistics (like SNMP)
        -{R}M{W}, --{R}masquerade{W}         display masqueraded connections

        -{R}v{W}, --{R}verbose{W}            be verbose
        -{R}W{W}, --{R}wide{W}               don't truncate IP addresses
        -{R}n{W}, --{R}numeric{W}            don't resolve names
        --{R}numeric-hosts{W}          don't resolve host names
        --{R}numeric-ports{W}          don't resolve port names
        --{R}numeric-users{W}          don't resolve user names
        -{R}N{W}, --{R}symbolic{W}           resolve hardware names
        -{R}e{W}, --{R}extend{W}             display other/more information
        -{R}p{W}, --{R}programs{W}           display PID/Program name for sockets
        -{R}o{W}, --{R}timers{W}             display timers
        -{R}c{W}, --{R}continuous{W}         continuous listing

        -{R}l{W}, --{R}listening{W}          display listening server sockets
        -{R}a{W}, --{R}all{W}                display all sockets (default: connected)
        -{R}F{W}, --{R}fib{W}                display Forwarding Information Base (default)
        -{R}C{W}, --{R}cache{W}              display routing cache instead of FIB
        -{R}Z{W}, --{R}context{W}            display SELinux security context for sockets

  <Socket>=(-{R}t{W}|--{R}tcp{W}) (-{R}u{W}|--{R}udp{W}) (-{R}U{W}|--{R}udplite{W}) (-{R}S{W}|--{R}sctp{W}) (-{R}w{W}|--{R}raw{W})
           (-{R}x{W}|--{R}unix{W}) --{R}ax25{W} --{R}ipx{W} --{R}netrom{W}

  <AF>=Use '-6|-4' or '-A <af>' or '--<af>'; default: inet
  List of possible address families (which support routing):
    inet (DARPA Internet) inet6 (IPv6) ax25 (AMPR AX.25)
    netrom (AMPR NET/ROM) ipx (Novell IPX) ddp (Appletalk DDP)
    x25 (CCITT X.25)
""")
####


# The man help commands section

## Traceroute

def cli_traceroute_manhelp():
    print(f"""
    {G}NAME{GR}:{W}
       traceroute - print the route packets trace to network host

{C}SYNOPSIS{GR}:{W}
        [-{R}46dFITUnreAV{W}] [-{R}f {O}first_ttl{W}] [-{R}g {O}gate{W},{O}...{W}]
        [-{R}i {O}device{W}] [-{R}m {O}max_ttl{W}] [-{R}p {O}port{W}] [-{R}s {O}src_addr{W}]
        [-{R}q {O}nqueries{W}] [-{R}N {O}squeries{W}] [-{R}t {O}tos{W}]
        [-{R}l {O}flow_label{W}] [-{R}w {O}waittimes{W}] [-{R}z {O}sendwait{W}] [-{R}UL{W}] [-{R}D{W}]
        [-{R}P {O}proto{W}] [--{R}sport{P}={O}port{W}] [-{R}M {O}method] [-{R}O {O}mod_options{W}]
        [--{R}mtu{W}] [--{R}back{W}]
        {G}host{W} [{O}packet_len{W}]

{C}DESCRIPTION{GR}:{W}
       traceroute tracks the route packets taken from an IP network on their way to a given host. It utilizes the IP protocol's time to live (TTL) field
       and attempts to elicit an ICMP TIME_EXCEEDED response from each gateway along the path to the host.

       traceroute6 is equivalent to traceroute -{R}6{W}

       tcptraceroute is equivalent to traceroute -{R}T{W}

       lft , the Layer Four Traceroute, performs a TCP traceroute, like traceroute -T , but attempts to provide compatibility with the original such im‐
       plementation, also called "lft".

       The  only  required  parameter  is the name or IP address of the destination host .  The optional packet_len`gth is the total size of the probing
       packet (default 60 bytes for IPv4 and 80 for IPv6). The specified size can be ignored in some situations or increased up to a minimal value.

       This program attempts to trace the route an IP packet would follow to some internet host by launching probe packets with a  small  ttl  (time  to
       live) then listening for an ICMP "time exceeded" reply from a gateway.  We start our probes with a ttl of one and increase by one until we get an
       ICMP "port unreachable" (or TCP reset), which means we got to the "host", or hit a max (which defaults to 30 hops). Three probes (by default) are
       sent at each ttl setting and a line is printed showing the ttl, address of the gateway and round trip time of each probe. The address can be fol‐
       lowed by additional information when requested. If the probe answers come from different gateways, the address of each responding system will  be
       printed.  If there is no response within a certain timeout, an "*" (asterisk) is printed for that probe.

       After  the trip time, some additional annotation can be printed: !H, !N, or !P (host, network or protocol unreachable), !S (source route failed),
       !F (fragmentation needed), !X (communication administratively prohibited), !V (host precedence violation), !C (precedence cutoff in  effect),  or
       !<num> (ICMP unreachable code <num>).  If almost all the probes result in some kind of unreachable, traceroute will give up and exit.

       We  don't want the destination host to process the UDP probe packets, so the destination port is set to an unlikely value (you can change it with
       the -p flag). There is no such a problem for ICMP or TCP tracerouting (for TCP we use half-open technique, which prevents our probes to  be  seen
       by applications on the destination host).

       In  the modern network environment the traditional traceroute methods can not be always applicable, because of widespread use of firewalls.  Such
       firewalls filter the "unlikely" UDP ports, or even ICMP echoes.  To solve this, some additional tracerouting methods are  implemented  (including
       tcp),  see LIST OF AVAILABLE METHODS below. Such methods try to use particular protocol and source/destination port, in order to bypass firewalls
       (to be seen by firewalls just as a start of allowed type of a network session).

{C}COMMANDS{GR}:{W}

       {B}help{W}
           Print help info and exit.

       {B}clear{W}
           Clear the terminal (the {R}cls{W} (the windows clear command) command can't be run)

       {B}leave{W}
           Leave the traceroute tool

       {B}man traceroute{W}
           Show this message and exit

{C}OPTIONS{GR}:{W}
       -{R}4, -{R}6{W} Explicitly force IPv4 or IPv6 tracerouting. By default, the program will try to resolve the name given, and choose the appropriate  proto‐
              col automatically. If resolving a host name returns both IPv4 and IPv6 addresses, traceroute will use IPv4.

       -{R}I{W}, --{R}icmp{W}
              Use ICMP ECHO for probes

       -{R}T{W}, --{R}tcp{W}
              Use TCP SYN for probes

       -{R}d{W}, --{R}debug{W}
              Enable socket level debugging (when the Linux kernel supports it)

       -{R}F{W}, --{R}dont-fragments{W}
              Do not fragment probe packets. (For IPv4 it also sets DF bit, which tells intermediate routers not to fragment remotely as well).

              Varying  the size of the probing packet by the packet_len command line parameter, you can manually obtain information about the MTU of in‐
              dividual network hops. The --mtu option (see below) tries to do this automatically.

              Note, that non-fragmented features (like -F or --mtu) work properly since the Linux kernel 2.6.22 only.  Before that version, IPv6 was al‐
              ways  fragmented, IPv4 could use the once the discovered final mtu only (from the route cache), which can be less than the actual mtu of a
              device.

       -{R}f{W} {O}first_ttl{W}, --{R}first{P}={O}first_ttl{W}
              Specifies with what TTL to start. Defaults to 1.

       -{R}g{W} {O}gateway{W}, --{R}gateway{P}={O}gateway{W}
              Tells traceroute to add an IP source routing option to the outgoing packet that tells the network to route the packet through  the  speci‐
              fied  gateway  (most  routers  have  disabled source routing for security reasons).  In general, several gateway's is allowed (comma sepa‐
              rated). For IPv6, the form of num,addr,addr...  is allowed, where num is a route header type (default is type 2). Note the  type  0  route
              header is now deprecated (rfc5095).

       -{R}i{W} {O}interface{W}, --{R}interface{P}={O}interface{W}
              Specifies  the  interface through which traceroute should send packets. By default, the interface is selected according to the routing ta‐
              ble.

       -{R}m{W} {O}max_ttl{W}, --{R}max-hops{P}={O}max_ttl{W}
              Specifies the maximum number of hops (max time-to-live value) traceroute will probe. The default is 30.

       -{R}N {O}squeries{W}, --{R}sim-queries{P}={O}squeries{W}
              Specifies the number of probe packets sent out simultaneously.  Sending several probes concurrently can speed up traceroute  considerably.
              The default value is 16.
              Note  that  some  routers and hosts can use ICMP rate throttling. In such a situation specifying too large number can lead to loss of some
              responses.

       -{R}n{W}     Do not try to map IP addresses to host names when displaying them.

       -{R}p {O}port{W}, --{R}port{P}={O}port{W}
              For UDP tracing, specifies the destination port base traceroute will use (the destination port number will be incremented by each probe).
              For ICMP tracing, specifies the initial ICMP sequence value (incremented by each probe too).
              For TCP and others specifies just the (constant) destination port to connect. When using  the  tcptraceroute  wrapper,  -p  specifies  the
              source port.

       -{R}t {O}tos{W}, --{R}tos{P}={O}tos{W}
              For IPv4, set the Type of Service (TOS) and Precedence value. Useful values are 16 (low delay) and 8 (high throughput). Note that in order
              to use some TOS precedence values, you have to be super user.
              For IPv6, set the Traffic Control value.

       -{R}l {O}flow_label{W}, --{R}flowlabel{P}={O}flow_label{W}
              Use specified flow_label for IPv6 packets.

       -{R}w {O}max{W}[,{O}here{W},{O}near{W}], --{R}wait{P}={O}max{W}[,{O}here{W},{O}near{W}]{W}
              Determines how long to wait for a response to a probe.

              There are three (in general) float values separated by a comma (or a slash).  Max specifies the maximum time (in seconds, default 5.0)  to
              wait, in any case.

              Traditional  traceroute  implementation  always  waited whole max seconds for any probe. But if we already have some replies from the same
              hop, or even from some next hop, we can use the round trip time of such a reply as a hint to determine the  actual  reasonable  amount  of
              time to wait.

              The  optional here (default 3.0) specifies a factor to multiply the round trip time of an already received response from the same hop. The
              resulting value is used as a timeout for the probe, instead of (but no more than) max.  The optional near (default 10.0) specifies a simi‐
              lar factor for a response from some next hop.  (The time of the first found result is used in both cases).

              First,  we  look  for the same hop (of the probe which will be printed first from now).  If nothing found, then look for some next hop. If
              nothing found, use max.  If here and/or near have zero values, the corresponding computation is skipped.
              Here and near are always set to zero if only max is specified (for compatibility with previous versions).

       -{R}q {O}nqueries{W}, --{R}queries{P}={O}nqueries{W}
              Sets the number of probe packets per hop. The default is 3.

       -{R}r{W}     Bypass the normal routing tables and send directly to a host on an attached network.  If the host is not on a  directly-attached  network,
              an error is returned.  This option can be used to ping a local host through an interface that has no route through it.

       -{R}s {O}source_addr{W}, --{R}source{P}={O}source_addr{W}
              Chooses  an  alternative  source  address. Note that you must select the address of one of the interfaces.  By default, the address of the
              outgoing interface is used.

       -{R}z {O}sendwait{W}, --{R}sendwait{P}={O}sendwait{W}
              Minimal time interval between probes (default 0).  If the value is more than 10, then it specifies a number in milliseconds, else it is  a
              number of seconds (float point values allowed too).  Useful when some routers use rate-limit for ICMP messages.

       -{R}e{W}, --{R}extensions{W}
              Show  ICMP extensions (rfc4884). The general form is CLASS/TYPE: followed by a hexadecimal dump.  The MPLS (rfc4950) is shown parsed, in a
              form: MPLS:L=label,E=exp_use,S=stack_bottom,T=TTL (more objects separated by / ).

       -{R}A{W}, --{R}as-path-lookups{W}
              Perform AS path lookups in routing registries and print results directly after the corresponding addresses.

       -{R}V{W}, --{R}version{W}
              Print the version and exit.

       There are additional options intended for advanced usage (such as alternate trace methods etc.):

       --{R}sport{P}={O}port{W}
              Chooses the source port to use. Implies -N 1 -w 5 .  Normally source ports (if applicable) are chosen by the system.

       --{R}fwmark{P}={O}mark{W}
              Set the firewall mark for outgoing packets (since the Linux kernel 2.6.25).

       -{R}M {O}method{W}, --{R}module{P}={O}name{W}
              Use specified method for traceroute operations. Default traditional udp method has name default, icmp (-I) and tcp (-T)  have  names  icmp
              and tcp respectively.
              Method-specific options can be passed by -O .  Most methods have their simple shortcuts, (-I means -M icmp, etc).

       -{R}O {O}option{W}, --{R}options{P}={O}options{W}
              Specifies  some  method-specific  option. Several options are separated by comma (or use several -O on cmdline).  Each method may have its
              own specific options, or many not have them at all.  To print information about available options, use -O help.

       -{R}U{W}, --{R}udp{W}
              Use UDP to particular destination port for tracerouting (instead of increasing the port per each probe). Default port is 53 (dns).

       -{R}UL{W}    Use UDPLITE for tracerouting (default port is 53).

       -{R}D{W}, --{R}dccp{W}
              Use DCCP Requests for probes.

       -{R}P {O}protocol{W}, --{R}protocol{P}={O}protocol{W}
              Use raw packet of specified protocol for tracerouting. Default protocol is 253 (rfc3692).

       --{R}mtu{W}  Discover MTU along the path being traced. Implies -F -N 1.  New mtu is printed once in a form of F=NUM at the first probe of a  hop  which
              requires such mtu to be reached. (Actually, the correspond "frag needed" icmp message normally is sent by the previous hop).

              Note,  that  some  routers might cache once the seen information on a fragmentation. Thus you can receive the final mtu from a closer hop.
              Try to specify an unusual tos by -t , this can help for one attempt (then it can be cached there as well).
              See -F option for more info.

       --{R}back{W} Print the number of backward hops when it seems different with the forward direction. This number is guessed  in  assumption  that  remote
              hops  send reply packets with initial ttl set to either 64, or 128 or 255 (which seems a common practice). It is printed as a negate value
              in a form of '-NUM' .

{C}LIST OF AVAILABLE METHODS{GR}:{W}
       In general, a particular traceroute method may have to be chosen by -M name, but most of the methods have their simple cmdline switches (you  can
       see them after the method name, if present).

   {C}{D}default{W}
       The traditional, ancient method of tracerouting. Used by default.

       Probe packets are udp datagrams with so-called "unlikely" destination ports.  The "unlikely" port of the first probe is 33434, then for each next
       probe it is incremented by one. Since the ports are expected to be unused, the destination host normally returns "icmp unreach port" as  a  final
       response.  (Nobody knows what happens when some application listens for such ports, though).

       This method is allowed for unprivileged users.

   {C}{D}icmp{W}       -{R}I
       Most usual method for now, which uses icmp echo packets for probes.
       If you can ping(8) the destination host, icmp tracerouting is applicable as well.

       This  method  may  be  allowed for unprivileged users since the kernel 3.0 (IPv4, for IPv6 since 3.11), which supports new dgram icmp (or "ping")
       sockets. To allow such sockets, sysadmin should provide net/ipv4/ping_group_range sysctl range to match any group of the user.
       Options:

       raw    Use only raw sockets (the traditional way).
              This way is tried first by default (for compatibility reasons), then new dgram icmp sockets as fallback.

       dgram  Use only dgram icmp sockets.

   {C}{D}tcp{W}        -{R}T
       Well-known modern method, intended to bypass firewalls.
       Uses the constant destination port (default is 80, http).

       If some filters are present in the network path, then most probably any "unlikely" udp ports (as for default method) or even icmp echoes (as  for
       icmp)  are  filtered,  and  whole tracerouting will just stop at such a firewall.  To bypass a network filter, we have to use only allowed proto‐
       col/port combinations. If we trace for some, say, mailserver, then more likely -T -p 25 can reach it, even when -I can not.

       This method uses well-known "half-open technique", which prevents applications on the destination host from seeing our probes at all.   Normally,
       a tcp syn is sent. For non-listened ports we receive tcp reset, and all is done. For active listening ports we receive tcp syn+ack, but answer by
       tcp reset (instead of expected tcp ack), this way the remote tcp session is dropped even without the application ever taking notice.

       There is a couple of options for tcp method:

       syn,ack,fin,rst,psh,urg,ece,cwr
              Sets specified tcp flags for probe packet, in any combination.

       flags{P}={O}num
              Sets the flags field in the tcp header exactly to num.

       ecn    Send syn packet with tcp flags ECE and CWR (for Explicit Congestion Notification, rfc3168).

       sack,timestamps,window_scaling
              Use the corresponding tcp header option in the outgoing probe packet.

       sysctl Use current sysctl (/proc/sys/net/*) setting for the tcp header options above and ecn.  Always set by default, if nothing else specified.

       mss=num
              Use value of num for maxseg tcp header option (when syn).

       info   Print tcp flags of final tcp replies when the target host is reached.  Allows to determine whether an application  listens  the  port  and
              other useful things.

       Default options is syn,sysctl.

   {C}{D}tcpconn{W}
       An  initial  implementation of tcp method, simple using connect(2) call, which does full tcp session opening. Not recommended for normal use, be‐
       cause a destination application is always affected (and can be confused).

   {C}{D}udp{W}        -{R}U{W}
       Use udp datagram with constant destination port (default 53, dns).
       Intended to bypass firewall as well.

       Note, that unlike in tcp method, the correspond application on the destination host always receive our probes (with random data),  and  most  can
       easily  be confused by them. Most cases it will not respond to our packets though, so we will never see the final hop in the trace. (Fortunately,
       it seems that at least dns servers replies with something angry).

       This method is allowed for unprivileged users.

   {C}{D}udplite{W}    -{R}UL{W}
       Use udplite datagram for probes (with constant destination port, default 53).

       This method is allowed for unprivileged users.
       Options:

       {R}coverage{P}={O}num{W}
              Set udplite send coverage to num.

   {C}{D}dccp{W}    -{R}D{W}
       Use DCCP Request packets for probes (rfc4340).

       This method uses the same "half-open technique" as used for TCP.  The default destination port is 33434.

       Options:

       {R}service{P}={O}num{W}
              Set DCCP service code to num (default is 1885957735).

   {C}{D}raw{W}        -{R}P {O}proto{W}
       Send raw packet of protocol proto.
       No protocol-specific headers are used, just IP header only.
       Implies -{R}N {O}1 -{R}w {O}5 .
       Options:

       {R}protocol{P}={O}proto{W}
              Use IP protocol proto (default 253).

{C}NOTES{GR}:{W}
       To speed up work, normally several probes are sent simultaneously.  On the other hand, it creates a "storm of packages", especially in the  reply
       direction.  Routers  can throttle the rate of icmp responses, and some of replies can be lost. To avoid this, decrease the number of simultaneous
       probes, or even set it to 1 (like in initial traceroute implementation), i.e.  -N 1

       The final (target) host can drop some of the simultaneous probes, and might even answer only the latest ones. It can lead to  extra  "looks  like
       expired"  hops  near  the  final hop. We use a smart algorithm to auto-detect such a situation, but if it cannot help in your case, just use -N 1
       too.

       For even greater stability you can slow down the program's work by -z option, for example use -z 0.5 for half-second pause between probes.

       To avoid an extra waiting, we use adaptive algorithm for timeouts (see -w option for more info). It can lead to premature expiry (especially when
       response  times differ at times) and printing "*" instead of a time. In such a case, switch this algorithm off, by specifying -w with the desired
       timeout only (for example, -w 5).

       If some hops report nothing for every method, the last chance to obtain something is to use ping -R command (IPv4, and for nearest 8 hops only).
""")


## Whois

def cli_whois_manhelp():
    print(f"""
    {G}NAME{GR}:{W}
       whois - client for the whois directory service

{C}SYNOPSIS{GR}:{W}
       whois  [  (  -h  |  --host  )  HOST  ]  [  (  -p  |  --port  )  PORT  ] [ -abBcdGHIKlLmMrRx ] [ -g SOURCE:FIRST-LAST ] [ -i ATTR[,ATTR]... ] [ -s
       SOURCE[,SOURCE]... ] [ -T TYPE[,TYPE]... ] [ --verbose ] OBJECT

       whois -q KEYWORD

       whois -t TYPE

       whois -v TYPE

       whois --help

       whois --version

{C}DESCRIPTION{GR}:{W}
       whois searches for an object in a RFC 3912 database.

       This version of the whois client tries to guess the right server to ask for the specified object. If no guess can be  made  it  will  connect  to
       whois.networksolutions.com for NIC handles or whois.arin.net for IPv4 addresses and network names.

{C}OPTIONS{GR}:{W}
       -h HOST, --host=HOST
               Connect to HOST.

       -H      Do not display the legal disclaimers that some registries like to show you.

       -p PORT, --port=PORT
               Connect to PORT.

       -I      First  query whois.iana.org and then follow its referral to the whois server authoritative for that request. This works for IP addresses,
               AS numbers and domains.  BEWARE: this implies that the IANA server will receive your complete query.

       --verbose
               Be verbose.

       --help  Display online help.

       --version
               Display the program version.

       Other options are flags understood by whois.ripe.net and some other RIPE-like servers:

       -a      Also search all the mirrored databases.

       -b      Return brief IP address ranges with abuse contact.

       -B      Disable objects filtering. (Show the e-mail addresses.)

       -c      Return the smallest IP address range with a reference to an irt object.

       -d      Return the reverse DNS delegation object too.

       -g SOURCE:FIRST-LAST
               Search updates from SOURCE database between FIRST and LAST update serial number. It is useful to obtain Near Real Time Mirroring stream.

       -G      Disable grouping of associated objects.

       -i ATTR[,ATTR]...
               Inverse-search objects having associated attributes.  ATTR is the attribute name, while the positional OBJECT argument is  the  attribute
               value.

       -K      Return primary key attributes only. An exception is the members attribute of set objects, which is always returned. Another exception are
               all attributes of the objects organisation, person and role, that are never returned.

       -l      Return the one level less specific object.

       -L      Return all levels of less specific objects.

       -m      Return all one level more specific objects.

       -M      Return all levels of more specific objects.

       -q KEYWORD
               Return information about the server.  KEYWORD can be version for the server version, sources for the list of database  sources  or  types
               for the list of supported object types.

       -r      Disable recursive lookups for contact information.

       -R      Disable following referrals and force showing the object from the local copy in the server.

       -s SOURCE[,SOURCE]...
               Request the server to search for objects mirrored from SOURCE.  Sources are delimited by comma, and the order is significant.  Use the -q
               sources parameter to obtain a list of valid sources.

       -t TYPE Return the template for a object of TYPE.

       -T TYPE[,TYPE]...
               Restrict the search to objects of TYPE.  Multiple types are separated by a comma.

       -v TYPE Return the verbose template for a object of TYPE.

       -x      Search for only exact match on network address prefix.

{C}NOTES{GR}:{W}
       When querying the Verisign gTLDs (e.g. .com, .net...) thin registry servers for a domain, the program will automatically prepend the domain  key‐
       word to only show domain records.  The nameserver or registrar keywords must be used to show other kinds of records.

       When querying whois.arin.net for IPv4 or IPv6 networks, the CIDR netmask length will be automatically removed from the query string.

       When querying whois.nic.ad.jp for AS numbers, the program will automatically convert the request in the appropriate format, inserting a space af‐
       ter the string AS.

       When querying whois.denic.de for domain names and no other flags have been specified, the program will automatically add the flag -T dn.

       When querying whois.dk-hostmaster.dk for domain names and no other flags have been  specified,  the  program  will  automatically  add  the  flag
       --show-handles.

       RIPE-specific  command  line options are ignored when querying non-RIPE servers. This may or may not be the behaviour intended by the user.  When
       using non-standard query parameters then the command line options which are not to be interpreted by the client  must  follow  the  --  separator
       (which marks the beginning of the query string).

       If  the  /etc/whois.conf configuration file exists, it will be consulted to find a server before applying the normal rules. Each line of the file
       should contain a regular expression to be matched against the query text and the whois server to use, separated by white space.  IDN domains must
       use the ACE format.

       The whois protocol does not specify an encoding for characters which cannot be represented by ASCII and implementations vary wildly.  If the pro‐
       gram knows that a specific server uses a certain encoding, if needed it will transcode the server output to the encoding specified by the current
       system locale.

       Command line arguments will always be interpreted accordingly to the current system locale and converted to the IDN ASCII Compatible Encoding.

{C}FILES{GR}:{W}
       /etc/whois.conf

{C}ENVIRONMENT{GR}:{W}
       LANG   When  querying  whois.nic.ad.jp and whois.jprs.jp English text is requested unless the LANG or LC_MESSAGES environment variables specify a
              Japanese locale.

       WHOIS_OPTIONS
              A list of options which will be evaluated before the ones specified on the command line.

       WHOIS_SERVER
              This server will be queried if the program cannot guess where some kind of objects are located.  If  the  variable  does  not  exist  then
              whois.arin.net will be queried.

{C}SEE ALSO{GR}:{W}
       whois.conf(5).

       RFC 3912: WHOIS Protocol Specification.

       RIPE Database Query Reference Manual: <http://www.ripe.net/data-tools/support/documentation/ripe-database-query-reference-manual>

{C}BUGS{GR}:{W}
       The  program may have buffer overflows in the command line parser: be sure to not pass untrusted data to it.  It should be rewritten to use a dy‐
       namic strings library.

{C}HISTORY{GR}:{W}
       This program closely tracks the user interface of the whois client developed at RIPE by Ambrose Magee and others on the base of the original  BSD
       client.

{C}AUTHOR{GR}:{W}
       Whois  and this man page were written by Marco d'Itri <md@linux.it> and are licensed under the terms of the GNU General Public License, version 2
       or higher.
""")


## NSLookup

def cli_nslookup_manhelp():
    print(f"""
    {G}NAME{GR}:{W}
       nslookup - query Internet name servers interactively

{C}SYNOPSIS{GR}:{W}
       nslookup [-option] [name | -] [server]

{C}DESCRIPTION{GR}:{W}
       Nslookup is a program to query Internet domain name servers.  Nslookup has two modes: interactive and non-interactive. Interactive mode allows
       the user to query name servers for information about various hosts and domains or to print a list of hosts in a domain. Non-interactive mode is
       used to print just the name and requested information for a host or domain.

{C}COMMANDS{GR}:{W}
       clear
           Clear the terminal (the {R}cls{W} (the windows clear command) command can't be run)

       leave
           Leave the nslookup tool

       man nslookup
           Show this message and exit

{C}ARGUMENTS{GR}:{W}
       Interactive mode is entered in the following cases:

        1. when no arguments are given (the default name server will be used)

        2. when the first argument is a hyphen (-) and the second argument is the host name or Internet address of a name server.

       Non-interactive mode is used when the name or Internet address of the host to be looked up is given as the first argument. The optional second
       argument specifies the host name or address of a name server.

       Options can also be specified on the command line if they precede the arguments and are prefixed with a hyphen. For example, to change the
       default query type to host information, and the initial timeout to 10 seconds, type:

           nslookup -query=hinfo  -timeout=10

       The -version option causes nslookup to print the version number and immediately exits.

{C}INTERACTIVE COMMANDS{GR}:{W}
       host [server]
           Look up information for host using the current default server or using server, if specified. If host is an Internet address and the query
           type is A or PTR, the name of the host is returned. If host is a name and does not have a trailing period, the search list is used to qualify
           the name.

           To look up a host not in the current domain, append a period to the name.

       server domain

       lserver domain
           Change the default server to domain; lserver uses the initial server to look up information about domain, while server uses the current
           default server. If an authoritative answer can't be found, the names of servers that might have the answer are returned.

       {G}root{W}
           not implemented

       {G}finger{W}
           not implemented

       {G}ls{W}
           not implemented

       {G}view{W}
           not implemented

       {G}help{W}
           not implemented

       {G}?{W}
           not implemented

       {G}exit{W}
           Exits the program.

       {G}set keyword[=value]{W}
           This command is used to change state information that affects the lookups. Valid keywords are:

           all
               Prints the current values of the frequently used options to set. Information about the current default server and host is also printed.

           class=value
               Change the query class to one of:

               IN
                   the Internet class

               CH
                   the Chaos class

               HS
                   the Hesiod class

               ANY
                   wildcard

               The class specifies the protocol group of the information.

               (Default = IN; abbreviation = cl)

           [no]debug
               Turn on or off the display of the full response packet and any intermediate response packets when searching.

               (Default = nodebug; abbreviation = [no]deb)

           [no]d2
               Turn debugging mode on or off. This displays more about what nslookup is doing.

               (Default = nod2)

           domain=name
               Sets the search list to name.

           [no]search
               If the lookup request contains at least one period but doesn't end with a trailing period, append the domain names in the domain search
               list to the request until an answer is received.

               (Default = search)

           port=value
               Change the default TCP/UDP name server port to value.

               (Default = 53; abbreviation = po)

           querytype=value

           type=value
               Change the type of the information query.

               (Default = A and then AAAA; abbreviations = q, ty)

               Note: It is only possible to specify one query type, only the default behavior looks up both when an alternative is not specified.

           [no]recurse
               Tell the name server to query other servers if it does not have the information.

               (Default = recurse; abbreviation = [no]rec)

           ndots=number
               Set the number of dots (label separators) in a domain that will disable searching. Absolute names always stop searching.

           retry=number
               Set the number of retries to number.

           timeout=number
               Change the initial timeout interval for waiting for a reply to number seconds.

           [no]vc
               Always use a virtual circuit when sending requests to the server.

               (Default = novc)

           [no]fail
               Try the next nameserver if a nameserver responds with SERVFAIL or a referral (nofail) or terminate query (fail) on such a response.

               (Default = nofail)

{C}RETURN VALUES{GR}:{W}
       nslookup returns with an exit status of 1 if any query failed, and 0 otherwise.

{C}IDN SUPPORT{GR}:{W}
       If nslookup has been built with IDN (internationalized domain name) support, it can accept and display non-ASCII domain names.  nslookup
       appropriately converts character encoding of domain name before sending a request to DNS server or displaying a reply from the server. If you'd
       like to turn off the IDN support for some reason, define the IDN_DISABLE environment variable. The IDN support is disabled if the variable is set
       when nslookup runs or when the standard output is not a tty.

{C}FILES{GR}:{W}
       /etc/resolv.conf

{C}SEE ALSO{GR}:{W}
       dig(1), host(1), named(8).

{C}AUTHOR{GR}:{W}
       Internet Systems Consortium, Inc.

{C}COPYRIGHT{GR}:{W}
       Copyright © 2004-2007, 2010, 2013-2020 Internet Systems Consortium, Inc. ("ISC")
""")


## Ping

def cli_ping_manhelp():
    print(f"""

    {G}Usage{GR}:{W} [{R}options{W}] <{R}destination{W}>

{C}NAME{GR}:{W}
       ping - send ICMP ECHO_REQUEST to network hosts

{C}SYNOPSIS{GR}:{W}
       ping [-aAbBdDfhLnOqrRUvV46] [-c count] [-F flowlabel] [-i interval] [-I interface] [-l preload] [-m mark] [-M pmtudisc_option]
            [-N nodeinfo_option] [-w deadline] [-W timeout] [-p pattern] [-Q tos] [-s packetsize] [-S sndbuf] [-t ttl] [-T timestamp option] [hop...]
            <destination>

{C}DESCRIPTION{GR}:{W}
       ping uses the ICMP protocol's mandatory ECHO_REQUEST datagram to elicit an ICMP ECHO_RESPONSE from a host or gateway. ECHO_REQUEST datagrams
       (“pings”) have an IP and ICMP header, followed by a struct timeval and then an arbitrary number of “pad” bytes used to fill out the packet.

       ping works with both IPv4 and IPv6. Using only one of them explicitly can be enforced by specifying -4 or -6.

       ping can also send IPv6 Node Information Queries (RFC4620). Intermediate hops may not be allowed, because IPv6 source routing was deprecated
       (RFC5095).

{C}COMMAND{GR}:{W}
       clear
           Clear the terminal (the {R}cls{W} (the windows clear command) command can't be run)

       leave
           Leave the ping tool

       man ping
           Show this message and exit

{C}OPTIONS{GR}:{W}
       -4
           Use IPv4 only.

       -6
           Use IPv6 only.

       -a
           Audible ping.

       -A
           Adaptive ping. Interpacket interval adapts to round-trip time, so that effectively not more than one (or more, if preload is set) unanswered
           probe is present in the network. Minimal interval is 200msec for not super-user. On networks with low rtt this mode is essentially equivalent
           to flood mode.

       -b
           Allow pinging a broadcast address.

       -B
           Do not allow ping to change source address of probes. The address is bound to one selected when ping starts.

       -c count
           Stop after sending count ECHO_REQUEST packets. With deadline option, ping waits for count ECHO_REPLY packets, until the timeout expires.

       -d
           Set the SO_DEBUG option on the socket being used. Essentially, this socket option is not used by Linux kernel.

       -D
           Print timestamp (unix time + microseconds as in gettimeofday) before each line.

       -f
           Flood ping. For every ECHO_REQUEST sent a period “.” is printed, while for ever ECHO_REPLY received a backspace is printed. This provides a
           rapid display of how many packets are being dropped. If interval is not given, it sets interval to zero and outputs packets as fast as they
           come back or one hundred times per second, whichever is more. Only the super-user may use this option with zero interval.

       -F flow label
           IPv6 only. Allocate and set 20 bit flow label (in hex) on echo request packets. If value is zero, kernel allocates random flow label.

       -h
           Show help.

       -i interval
           Wait interval seconds between sending each packet. The default is to wait for one second between each packet normally, or not to wait in
           flood mode. Only super-user may set interval to values less than 0.2 seconds.

       -I interface
           interface is either an address, or an interface name. If interface is an address, it sets source address to specified interface address. If
           interface in an interface name, it sets source interface to specified interface. NOTE: For IPv6, when doing ping to a link-local scope
           address, link specification (by the '%'-notation in destination, or by this option) can be used but it is no longer required.

       -l preload
           If preload is specified, ping sends that many packets not waiting for reply. Only the super-user may select preload more than 3.

       -L
           Suppress loopback of multicast packets. This flag only applies if the ping destination is a multicast address.

       -m mark
           use mark to tag the packets going out. This is useful for variety of reasons within the kernel such as using policy routing to select
           specific outbound processing.

       -M pmtudisc_opt
           Select Path MTU Discovery strategy.  pmtudisc_option may be either do (prohibit fragmentation, even local one), want (do PMTU discovery,
           fragment locally when packet size is large), or dont (do not set DF flag).

       -N nodeinfo_option
           IPv6 only. Send ICMPv6 Node Information Queries (RFC4620), instead of Echo Request. CAP_NET_RAW capability is required.

           {G}help{GR}:{W}
               Show help for NI support.

           {G}name{GR}:{W}
               Queries for Node Names.

           {G}ipv6{GR}:{W}
               Queries for IPv6 Addresses. There are several IPv6 specific flags.

               ipv6-global
                   Request IPv6 global-scope addresses.

               ipv6-sitelocal
                   Request IPv6 site-local addresses.

               ipv6-linklocal
                   Request IPv6 link-local addresses.

               ipv6-all
                   Request IPv6 addresses on other interfaces.

           {G}ipv4{GR}:{W}
               Queries for IPv4 Addresses. There is one IPv4 specific flag.

               ipv4-all
                   Request IPv4 addresses on other interfaces.

           {G}subject-ipv6=ipv6addr{GR}:{W}
               IPv6 subject address.

           {G}subject-ipv4=ipv4addr{GR}:{W}
               IPv4 subject address.

           {G}subject-name=nodename{GR}:{W}
               Subject name. If it contains more than one dot, fully-qualified domain name is assumed.

           {G}subject-fqdn=nodename{GR}:{W}
               Subject name. Fully-qualified domain name is always assumed.

       -n
           Numeric output only. No attempt will be made to lookup symbolic names for host addresses.

       -O
           Report outstanding ICMP ECHO reply before sending next packet. This is useful together with the timestamp -D to log output to a diagnostic
           file and search for missing answers.

       -p pattern
           You may specify up to 16 “pad” bytes to fill out the packet you send. This is useful for diagnosing data-dependent problems in a network. For
           example, -p ff will cause the sent packet to be filled with all ones.

       -q
           Quiet output. Nothing is displayed except the summary lines at startup time and when finished.

       -Q tos
           Set Quality of Service -related bits in ICMP datagrams.  tos can be decimal (ping only) or hex number.

           In RFC2474, these fields are interpreted as 8-bit Differentiated Services (DS), consisting of: bits 0-1 (2 lowest bits) of separate data, and
           bits 2-7 (highest 6 bits) of Differentiated Services Codepoint (DSCP). In RFC2481 and RFC3168, bits 0-1 are used for ECN.

           Historically (RFC1349, obsoleted by RFC2474), these were interpreted as: bit 0 (lowest bit) for reserved (currently being redefined as
           congestion control), 1-4 for Type of Service and bits 5-7 (highest bits) for Precedence.

       -r
           Bypass the normal routing tables and send directly to a host on an attached interface. If the host is not on a directly-attached network, an
           error is returned. This option can be used to ping a local host through an interface that has no route through it provided the option -I is
           also used.

       -R
           ping only. Record route. Includes the RECORD_ROUTE option in the ECHO_REQUEST packet and displays the route buffer on returned packets. Note
           that the IP header is only large enough for nine such routes. Many hosts ignore or discard this option.

       -s packetsize
           Specifies the number of data bytes to be sent. The default is 56, which translates into 64 ICMP data bytes when combined with the 8 bytes of
           ICMP header data.

       -S sndbuf
           Set socket sndbuf. If not specified, it is selected to buffer not more than one packet.

       -t ttl
           ping only. Set the IP Time to Live.

       -T timestamp option
           Set special IP timestamp options.  timestamp option may be either tsonly (only timestamps), tsandaddr (timestamps and addresses) or tsprespec
           host1 [host2 [host3 [host4]]] (timestamp prespecified hops).

       -U
           Print full user-to-user latency (the old behaviour). Normally ping prints network round trip time, which can be different f.e. due to DNS
           failures.

       -v
           Verbose output.

       -V
           Show version and exit.

       -w deadline
           Specify a timeout, in seconds, before ping exits regardless of how many packets have been sent or received. In this case ping does not stop
           after count packet are sent, it waits either for deadline expire or until count probes are answered or for some error notification from
           network.

       -W timeout
           Time to wait for a response, in seconds. The option affects only timeout in absence of any responses, otherwise ping waits for two RTTs.

       When using ping for fault isolation, it should first be run on the local host, to verify that the local network interface is up and running.
       Then, hosts and gateways further and further away should be “pinged”. Round-trip times and packet loss statistics are computed. If duplicate
       packets are received, they are not included in the packet loss calculation, although the round trip time of these packets is used in calculating
       the minimum/average/maximum/mdev round-trip time numbers.

       Population standard deviation (mdev), essentially an average of how far each ping RTT is from the mean RTT. The higher mdev is, the more variable
       the RTT is (over time). With a high RTT variability, you will have speed issues with bulk transfers (they will take longer than is strictly
       speaking necessary, as the variability will eventually cause the sender to wait for ACKs) and you will have middling to poor VoIP quality.

       When the specified number of packets have been sent (and received) or if the program is terminated with a SIGINT, a brief summary is displayed.
       Shorter current statistics can be obtained without termination of process with signal SIGQUIT.

       If ping does not receive any reply packets at all it will exit with code 1. If a packet count and deadline are both specified, and fewer than
       count packets are received by the time the deadline has arrived, it will also exit with code 1. On other error it exits with code 2. Otherwise it
       exits with code 0. This makes it possible to use the exit code to see if a host is alive or not.

       This program is intended for use in network testing, measurement and management. Because of the load it can impose on the network, it is unwise
       to use ping during normal operations or from automated scripts.

{C}ICMP PACKET DETAILS{GR}:{W}
       An IP header without options is 20 bytes. An ICMP ECHO_REQUEST packet contains an additional 8 bytes worth of ICMP header followed by an
       arbitrary amount of data. When a packetsize is given, this indicated the size of this extra piece of data (the default is 56). Thus the amount of
       data received inside of an IP packet of type ICMP ECHO_REPLY will always be 8 bytes more than the requested data space (the ICMP header).

       If the data space is at least of size of struct timeval ping uses the beginning bytes of this space to include a timestamp which it uses in the
       computation of round trip times. If the data space is shorter, no round trip times are given.

{C}DUPLICATE AND DAMAGED PACKETS{GR}:{W}
       ping will report duplicate and damaged packets. Duplicate packets should never occur, and seem to be caused by inappropriate link-level
       retransmissions. Duplicates may occur in many situations and are rarely (if ever) a good sign, although the presence of low levels of duplicates
       may not always be cause for alarm.

       Damaged packets are obviously serious cause for alarm and often indicate broken hardware somewhere in the ping packet's path (in the network or
       in the hosts).

{C}TRYING DIFFERENT DATA PATTERNS{GR}:{W}
       The (inter)network layer should never treat packets differently depending on the data contained in the data portion. Unfortunately,
       data-dependent problems have been known to sneak into networks and remain undetected for long periods of time. In many cases the particular
       pattern that will have problems is something that doesn't have sufficient “transitions”, such as all ones or all zeros, or a pattern right at the
       edge, such as almost all zeros. It isn't necessarily enough to specify a data pattern of all zeros (for example) on the command line because the
       pattern that is of interest is at the data link level, and the relationship between what you type and what the controllers transmit can be
       complicated.

       This means that if you have a data-dependent problem you will probably have to do a lot of testing to find it. If you are lucky, you may manage
       to find a file that either can't be sent across your network or that takes much longer to transfer than other similar length files. You can then
       examine this file for repeated patterns that you can test using the -p option of ping.

{C}TTL DETAILS{GR}:{W}
       The TTL value of an IP packet represents the maximum number of IP routers that the packet can go through before being thrown away. In current
       practice you can expect each router in the Internet to decrement the TTL field by exactly one.

       The TCP/IP specification states that the TTL field for TCP packets should be set to 60, but many systems use smaller values (4.3 BSD uses 30, 4.2
       used 15).

       The maximum possible value of this field is 255, and most Unix systems set the TTL field of ICMP ECHO_REQUEST packets to 255. This is why you
       will find you can “ping” some hosts, but not reach them with telnet(1) or ftp(1).

       In normal operation ping prints the TTL value from the packet it receives. When a remote system receives a ping packet, it can do one of three
       things with the TTL field in its response:

           • Not change it; this is what Berkeley Unix systems did before the 4.3BSD Tahoe release. In this case the TTL value in the received packet
           will be 255 minus the number of routers in the round-trip path.

           • Set it to 255; this is what current Berkeley Unix systems do. In this case the TTL value in the received packet will be 255 minus the
           number of routers in the path from the remote system to the pinging host.

           • Set it to some other value. Some machines use the same value for ICMP packets that they use for TCP packets, for example either 30 or 60.
           Others may use completely wild values.

{C}BUGS{GR}:{W}
           • Many Hosts and Gateways ignore the RECORD_ROUTE option.

           • The maximum IP header length is too small for options like RECORD_ROUTE to be completely useful. There's not much that can be done about
           this, however.

           • Flood pinging is not recommended in general, and flood pinging the broadcast address should only be done under very controlled conditions.

{C}SEE ALSO{GR}:{W}
       ip(8), ss(8).

{C}HISTORY{GR}:{W}
       The ping command appeared in 4.3BSD.

       The version described here is its descendant specific to Linux.

       As of version s20150815, the ping6 binary doesn't exist anymore. It has been merged into ping. Creating a symlink named ping6 pointing to ping
       will result in the same funcionality as before.

{C}SECURITY{GR}:{W}
       ping requires CAP_NET_RAW capability to be executed 1) if the program is used for non-echo queries (See -N option), or 2) if kernel does not
       support non-raw ICMP sockets, or 3) if the user is not allowed to create an ICMP echo socket. The program may be used as set-uid root.

{C}AVAILABILITY{GR}:{W}
       ping is part of iputils package.
""")


## Netstat

def cli_netstat_manhelp():
    print(f"""
{G}NAME{GR}:{W}
       netstat - Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships

{C}SYNOPSIS{GR}:{W}
       netstat  [address_family_options]  [--tcp|-t]  [--udp|-u]  [--udplite|-U]  [--sctp|-S]  [--raw|-w] [--l2cap|-2] [--rfcomm|-f] [--listening|-l] [--all|-a] [--numeric|-n] [--numeric-hosts] [--numeric-ports] [--numeric-users] [--symbolic|-N]
       [--extend|-e[--extend|-e]] [--timers|-o] [--program|-p] [--verbose|-v] [--continuous|-c] [--wide|-W]

       netstat (--route|-r) [address_family_options] [--extend|-e[--extend|-e]] [--verbose|-v] [--numeric|-n] [--numeric-hosts] [--numeric-ports] [--numeric-users] [--continuous|-c]

       netstat (--interfaces|-i) [--all|-a] [--extend|-e[--extend|-e]] [--verbose|-v] [--program|-p] [--numeric|-n] [--numeric-hosts] [--numeric-ports] [--numeric-users] [--continuous|-c]

       netstat (--groups|-g) [--numeric|-n] [--numeric-hosts] [--numeric-ports] [--numeric-users] [--continuous|-c]

       netstat (--masquerade|-M) [--extend|-e] [--numeric|-n] [--numeric-hosts] [--numeric-ports] [--numeric-users] [--continuous|-c]

       netstat (--statistics|-s) [--tcp|-t] [--udp|-u] [--udplite|-U] [--sctp|-S] [--raw|-w]

       netstat (--version|-V)

       netstat (--help|-h)

       address_family_options:

       [-4|--inet] [-6|--inet6] [--protocol=(inet,inet6,unix,ipx,ax25,netrom,ddp,bluetooth, ... ) ] [--unix|-x] [--inet|--ip|--tcpip] [--ax25] [--x25] [--rose] [--ash] [--bluetooth] [--ipx] [--netrom] [--ddp|--appletalk] [--econet|--ec]

{C}NOTES{GR}:{W}
       This program is mostly obsolete.  Replacement for netstat is ss.  Replacement for netstat -r is ip route.  Replacement for netstat -i is ip -s link.  Replacement for netstat -g is ip maddr.

{C}DESCRIPTION{GR}:{W}
       Netstat prints information about the Linux networking subsystem.  The type of information printed is controlled by the first argument, as follows:

   (none)
       By default, netstat displays a list of open sockets.  If you don't specify any address families, then the active sockets of all configured address families will be printed.

   --route, -r
       Display the kernel routing tables. See the description in route(8) for details.  netstat -r and route -e produce the same output.

   --groups, -g
       Display multicast group membership information for IPv4 and IPv6.

   --interfaces, -i
       Display a table of all network interfaces.

   --masquerade, -M
       Display a list of masqueraded connections.

   --statistics, -s
       Display summary statistics for each protocol.

{C}OPTIONS{GR}:{W}
   --verbose, -v
       Tell the user what is going on by being verbose. Especially print some useful information about unconfigured address families.

   --wide, -W
       Do not truncate IP addresses by using output as wide as needed. This is optional for now to not break existing scripts.

   --numeric, -n
       Show numerical addresses instead of trying to determine symbolic host, port or user names.

   --numeric-hosts
       shows numerical host addresses but does not affect the resolution of port or user names.

   --numeric-ports
       shows numerical port numbers but does not affect the resolution of host or user names.

   --numeric-users
       shows numerical user IDs but does not affect the resolution of host or port names.

   --protocol=family, -A
       Specifies the address families (perhaps better described as low level protocols) for which connections are to be shown.  family is a comma (',') separated list of address family keywords like inet, inet6, unix, ipx, ax25, netrom,  econet,
       ddp, and bluetooth.  This has the same effect as using the --inet|-4, --inet6|-6, --unix|-x, --ipx, --ax25, --netrom, --ddp, and --bluetooth options.

       The address family inet (Iv4) includes raw, udp, udplite and tcp protocol sockets.

       The address family bluetooth (Iv4) includes l2cap and rfcomm protocol sockets.

   -c, --continuous
       This will cause netstat to print the selected information every second continuously.

   -e, --extend
       Display additional information.  Use this option twice for maximum detail.

   -o, --timers
       Include information related to networking timers.

   -p, --program
       Show the PID and name of the program to which each socket belongs.

   -l, --listening
       Show only listening sockets.  (These are omitted by default.)

   -a, --all
       Show both listening and non-listening sockets.  With the --interfaces option, show interfaces that are not up

   -F
       Print routing information from the FIB.  (This is the default.)

   -C
       Print routing information from the route cache.

{C}OUTPUT{GR}:{W}
   Active Internet connections (TCP, UDP, UDPLite, raw)
   Proto
       The protocol (tcp, udp, udpl, raw) used by the socket.

   Recv-Q
       Established: The count of bytes not copied by the user program connected to this socket.  Listening: Since Kernel 2.6.18 this column contains the current syn backlog.

   Send-Q
       Established: The count of bytes not acknowledged by the remote host.  Listening: Since Kernel 2.6.18 this column contains the maximum size of the syn backlog.

   Local Address
       Address  and  port  number  of the local end of the socket.  Unless the --numeric (-n) option is specified, the socket address is resolved to its canonical host name (FQDN), and the port number is translated into the corresponding service
       name.

   Foreign Address
       Address and port number of the remote end of the socket.  Analogous to "Local Address".

   State
       The state of the socket. Since there are no states in raw mode and usually no states used in UDP and UDPLite, this column may be left blank. Normally this can be one of several values:

       ESTABLISHED
              The socket has an established connection.

       SYN_SENT
              The socket is actively attempting to establish a connection.

       SYN_RECV
              A connection request has been received from the network.

       FIN_WAIT1
              The socket is closed, and the connection is shutting down.

       FIN_WAIT2
              Connection is closed, and the socket is waiting for a shutdown from the remote end.

       TIME_WAIT
              The socket is waiting after close to handle packets still in the network.

       CLOSE  The socket is not being used.

       CLOSE_WAIT
              The remote end has shut down, waiting for the socket to close.

       LAST_ACK
              The remote end has shut down, and the socket is closed. Waiting for acknowledgement.

       LISTEN The socket is listening for incoming connections.  Such sockets are not included in the output unless you specify the --listening (-l) or --all (-a) option.

       CLOSING
              Both sockets are shut down but we still don't have all our data sent.

       UNKNOWN
              The state of the socket is unknown.

   User
       The username or the user id (UID) of the owner of the socket.

   PID/Program name
       Slash-separated pair of the process id (PID) and process name of the process that owns the socket.  --program causes this column to be included.  You will also need superuser privileges to see this information on sockets  you  don't  own.
       This identification information is not yet available for IPX sockets.

   Timer
       (this needs to be written)

   Active UNIX domain Sockets
   Proto
       The protocol (usually unix) used by the socket.

   RefCnt
       The reference count (i.e. attached processes via this socket).

   Flags
       The  flags  displayed is SO_ACCEPTON (displayed as ACC), SO_WAITDATA (W) or SO_NOSPACE (N).  SO_ACCECPTON is used on unconnected sockets if their corresponding processes are waiting for a connect request. The other flags are not of normal
       interest.

   Type
       There are several types of socket access:

       SOCK_DGRAM
              The socket is used in Datagram (connectionless) mode.

       SOCK_STREAM
              This is a stream (connection) socket.

       SOCK_RAW
              The socket is used as a raw socket.

       SOCK_RDM
              This one serves reliably-delivered messages.

       SOCK_SEQPACKET
              This is a sequential packet socket.

       SOCK_PACKET
              Raw interface access socket.

       UNKNOWN
              Who ever knows what the future will bring us - just fill in here :-)

   State
       This field will contain one of the following Keywords:

       FREE   The socket is not allocated

       LISTENING
              The socket is listening for a connection request.  Such sockets are only included in the output if you specify the --listening (-l) or --all (-a) option.

       CONNECTING
              The socket is about to establish a connection.

       CONNECTED
              The socket is connected.

       DISCONNECTING
              The socket is disconnecting.

       (empty)
              The socket is not connected to another one.

       UNKNOWN
              This state should never happen.

   PID/Program name
       Process ID (PID) and process name of the process that has the socket open.  More info available in Active Internet connections section written above.

   Path
       This is the path name as which the corresponding processes attached to the socket.

   Active IPX sockets
       (this needs to be done by somebody who knows it)

   Active NET/ROM sockets
       (this needs to be done by somebody who knows it)

   Active AX.25 sockets
       (this needs to be done by somebody who knows it)

{C}FILES{GR}:{W}
       /etc/services -- The services translation file

       /proc -- Mount point for the proc filesystem, which gives access to kernel status information via the following files.

       /proc/net/dev -- device information

       /proc/net/raw -- raw socket information

       /proc/net/tcp -- TCP socket information

       /proc/net/udp -- UDP socket information

       /proc/net/udplite -- UDPLite socket information

       /proc/net/igmp -- IGMP multicast information

       /proc/net/unix -- Unix domain socket information

       /proc/net/ipx -- IPX socket information

       /proc/net/ax25 -- AX25 socket information

       /proc/net/appletalk -- DDP (appletalk) socket information

       /proc/net/nr -- NET/ROM socket information

       /proc/net/route -- IP routing information

       /proc/net/ax25_route -- AX25 routing information

       /proc/net/ipx_route -- IPX routing information

       /proc/net/nr_nodes -- NET/ROM nodelist

       /proc/net/nr_neigh -- NET/ROM neighbours

       /proc/net/ip_masquerade -- masqueraded connections

       /sys/kernel/debug/bluetooth/l2cap -- Bluetooth L2CAP information

       /sys/kernel/debug/bluetooth/rfcomm -- Bluetooth serial connections

       /proc/net/snmp -- statistics

{C}SEE ALSO{GR}:{W}
       route(8), ifconfig(8), iptables(8), proc(5) ss(8) ip(8)

{C}BUGS{GR}:{W}
       Occasionally strange information may appear if a socket changes as it is viewed. This is unlikely to occur.

{C}AUTHORS{GR}:{W}
       The netstat user interface was written by Fred Baumgarten <dc6iq@insu1.etec.uni-karlsruhe.de>, the man page basically by Matt Welsh <mdw@tc.cornell.edu>. It was updated by  Alan  Cox  <Alan.Cox@linux.org>,  updated  again  by  Tuan  Hoang
       <tqhoang@bigfoot.com>. The man page and the command included in the net-tools package is totally rewritten by Bernd Eckenfels <ecki@linux.de>.  UDPLite options were added by Brian Micek <bmicek@gmail.com>
""")