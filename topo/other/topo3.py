#!/usr/bin/env python

# sudo mn --controller remote,ip=10.0.1.1,port=6653 --switch=ovsk,protocols=OpenFlow13 --custom topo2.py --topo=mytopo

from asyncio import protocols
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node, Link
from mininet.node import OVSKernelSwitch, UserSwitch, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.util import customClass
from mininet.link import TCLink
from mininet.term import makeTerm
from functools    import partial
from mininet.util import dumpNodeConnections


from mininet.topo import Topo


class MyTopo( Topo ):

    # Rate limit links to 10Mbps
    link = customClass({'tc': TCLink}, 'tc,bw=10')

    def build( net ):
    

        info( '*** Add switches\n')
        s1 = net.addSwitch('s1')
#        s2 = net.addSwitch('s2')
        s3 = net.addSwitch('s3')
        s4 = net.addSwitch('s4')
        s5 = net.addSwitch('s5')
        s6 = net.addSwitch('s6')

        info( '*** Add hosts\n')
        h1 = net.addHost('h1', cls=Host, ip='1.0.2.1',mac='00:01:00:00:00:37')
        h2 = net.addHost('h2', cls=Host, ip='1.0.2.2',mac='00:01:00:00:00:38')
        h3 = net.addHost('h3', cls=Host, ip='1.0.2.3',mac='00:01:00:00:00:39')
        h4 = net.addHost('h4', cls=Host, ip='1.0.2.4',mac='00:01:00:00:00:3a')
        h5 = net.addHost('h5', cls=Host, ip='1.0.2.5',mac='00:01:00:00:00:3b')

        info( '*** Add links\n')
        
        # switch and switch
        net.addLink(s6, s1)
#        net.addLink(s6, s2)
        net.addLink(s6, s4)
        net.addLink(s6, s5)
#        net.addLink(s1,s5)
#        net.addLink(s3, s2)
        net.addLink(s3, s4)

        # switch and host
        net.addLink(s1, h1)
        net.addLink(s3, h3)
        net.addLink(s4, h4)
        net.addLink(s5, h2)
        net.addLink(s5, h5)

        
topos = { 'mytopo': ( lambda: MyTopo() ) }
