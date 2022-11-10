from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
from mininet.link import TCLink



class MyTopo( Topo ):
    
    def __init__( self ):
        Topo.__init__(self)

        A = self.addHost('A')
        B  = self.addHost('B')
        C  = self.addHost('C')
        D  = self.addHost('D')
        R1 = self.addSwitch('R1')
        R2 = self.addSwitch('R2')

        #add links
        self.addLink(A, R1, cls = TCLink, bw = 1000, delay = '1ms')
        self.addLink(D, R1, cls = TCLink, bw = 1000, delay = '1ms')
        self.addLink(B, R2, cls = TCLink, bw = 1000, delay = '1ms')
        self.addLink(C, R2, cls = TCLink, bw = 1000, delay = '1ms')
        self.addLink(R1, R2, cls = TCLink, bw = 500, delay = '10ms')

def Test():
    topo = MyTopo()
    net = Mininet(topo=topo)
    net.start()
    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    CLI(net)
    net.stop()

if __name__ == '__main__':
    Test()