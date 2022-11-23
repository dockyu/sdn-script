#!/usr/bin/env python

# sudo mn --controller remote,ip=10.0.1.1,port=30000 --switch=ovsk,protocols=OpenFlow13 --custom topo.py --topo=mytopo

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
        s2 = net.addSwitch('s2')
        s3 = net.addSwitch('s3')
        s4 = net.addSwitch('s4')
        s5 = net.addSwitch('s5')
        s6 = net.addSwitch('s6')
        s7 = net.addSwitch('s7')
        s8 = net.addSwitch('s8')
        s9 = net.addSwitch('s9')
        s10 = net.addSwitch('s10')
        s11 = net.addSwitch('s11')
        s12 = net.addSwitch('s12')
        s13 = net.addSwitch('s13')
        s14 = net.addSwitch('s14')
        s15 = net.addSwitch('s15')

        info( '*** Add hosts\n')
        h1 = net.addHost('h1', cls=Host, ip='1.0.2.1',mac='00:01:00:00:00:37')
        h2 = net.addHost('h2', cls=Host, ip='1.0.2.2',mac='00:01:00:00:00:38')
        h3 = net.addHost('h3', cls=Host, ip='1.0.2.3',mac='00:01:00:00:00:39')
        h4 = net.addHost('h4', cls=Host, ip='1.0.2.4',mac='00:01:00:00:00:3a')
        h5 = net.addHost('h5', cls=Host, ip='1.0.2.5',mac='00:01:00:00:00:3b')
        h6 = net.addHost('h6', cls=Host, ip='1.0.2.6',mac='00:01:00:00:00:3c')
        h7 = net.addHost('h7', cls=Host, ip='1.0.2.7',mac='00:01:00:00:00:3d')
        h8 = net.addHost('h8', cls=Host, ip='1.0.2.8',mac='00:01:00:00:00:3e')
        h9 = net.addHost('h9', cls=Host, ip='1.0.2.9',mac='00:01:00:00:00:3f')
        h10 = net.addHost('h10', cls=Host, ip='1.0.2.10',mac='00:01:00:00:00:40')
        h11 = net.addHost('h11', cls=Host, ip='1.0.2.11',mac='00:01:00:00:00:41')
        h12 = net.addHost('h12', cls=Host, ip='1.0.2.12',mac='00:01:00:00:00:42')
        h13 = net.addHost('h13', cls=Host, ip='1.0.2.13',mac='00:01:00:00:00:43')
        h14 = net.addHost('h14', cls=Host, ip='1.0.2.14',mac='00:01:00:00:00:44')
        h15 = net.addHost('h15', cls=Host, ip='1.0.2.15',mac='00:01:00:00:00:45')
        h16 = net.addHost('h16', cls=Host, ip='1.0.2.16',mac='00:01:00:00:00:46')

        info( '*** Add links\n')
        
        # s1 switch 
        net.addLink(s1, s2)
        net.addLink(s1, s3)
        # s2 switch
        net.addLink(s2,s4)
        net.addLink(s2,s5)
        # s3 switch 
        net.addLink(s3, s6)
        net.addLink(s3, s7)
        # s4 switch
        net.addLink(s4,s8)
        net.addLink(s4,s9)
        net.addLink(s4,s5)
        # s5 switch
        net.addLink(s5,s10)
        net.addLink(s5,s11)
        net.addLink(s5,s6)
        # s6 switch
        net.addLink(s6,s12)
        net.addLink(s6,s13)
        net.addLink(s6,s7)
        # s7 switch
        net.addLink(s7, s14)
        net.addLink(s7, s15)
        # s8 switch
        net.addLink(s8, h2)
        net.addLink(s8, h1)
        # s9 switch
        net.addLink(s9, h3)
        net.addLink(s9, h4)
        # s10 switch
        net.addLink(s10, h5)
        net.addLink(s10, h6)
        # s11 switch
        net.addLink(s11, h7)
        net.addLink(s11, h8)
        # s12 switch
        net.addLink(s12, h9)
        net.addLink(s12, h10)
        # s13 switch
        net.addLink(s13, h11)
        net.addLink(s13, h12)
        # s14 switch
        net.addLink(s14, h13)
        net.addLink(s14, h14)
        # s15 switch
        net.addLink(s15, h15)
        net.addLink(s15, h16)

        
topos = { 'mytopo': ( lambda: MyTopo() ) }