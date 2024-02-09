import scapy.all as scapy
from optparse import OptionParser

def get_user_input():
    optparser=OptionParser()
    optparser.add_option("-i","--iface",dest="iface")
    return optparser.parse_args()
    
def listen(iface):
    scapy.sniff(iface=iface,store=False,prn=analyze_packets)
    
def analyze_packets(packets):
    packets.show()

(user_input,arguments)=get_user_input()
iface=user_input.iface
listen(iface)
