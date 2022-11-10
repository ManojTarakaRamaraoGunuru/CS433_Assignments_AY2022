from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections



class MyTopo( Topo ):
    
    def __init__( self ):
        Topo.__init__(self)

        lh = self.addHost('h1')
        rh = self.addHost('h2')
        ls = self.addSwitch('s1')
        rs = self.addSwitch('s2')

        #add links
        self.addLink(lh, ls)
        self.addLink(ls, rs)
        self.addLink(rs, rh)

def Test():
    topo = MyTopo()
    net = Mininet(topo=topo)
    net.start()
    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    Test()