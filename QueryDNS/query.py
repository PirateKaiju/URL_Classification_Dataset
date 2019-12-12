import sys
import dns.resolver
import pyasn
import socket
import csv
import tldextract
from urllib.parse import urlparse


def print_records(records):
    for record in records:
        print(record)


def getIp(actual_record):
    actual_ip = socket.gethostbyname(str(actual_record))  # ip of 1st the record
    return(actual_ip)

def getDomain(actual_url):
    '''print("Raw URL: " + actual_url)
    
    parsed = urlparse(actual_url).netloc
    
    print(parsed)

    domain = '.'.join(parsed.split('.')[1:])
    
    print("Domain: " + domain)'''

    print("Raw URL: " + actual_url)
    
    parsed = tldextract.extract(actual_url)
    
    print(parsed.domain + "." + parsed.suffix)

    domain = parsed.domain + "." + parsed.suffix
    
    print("Domain: " + domain)

    return domain

    

#TODO: ENABLE DEFAULT RESULT

resolver = dns.resolver.Resolver()

asndb = pyasn.pyasn("/home/antonio/NetBeansProjects/CloneProphilerV1/src/resources/ipasn_db_file.dat")  #  FULL FILENAME NECESSARY FOR JAVA
# print(asndb.lookup("8.8.8.8"))

url = ""

if (len(sys.argv)):
    # url = "google.com"
    url = sys.argv[1]  # passed url
    url = getDomain(url) #DISABLE IF NEEDED

#EXTRACTION 

arecords = []
mxrecords = []
nsrecords = []

ptrrecords = []

try:
    arecords = resolver.query(url, "A")
except: #TODO: DETAIL
    print("Problem extracting A records")
    arecords = []

try:
    mxrecords = resolver.query(url, "MX")
except:
    print("Problem extracting MX records")
    mxrecords = []

try:
    nsrecords = resolver.query(url, "NS")
except:
    print("Problem extracting NS records")
    nsrecords = []



try:
    pass
    #TODO: FIX THIS
    #ptrrecords = resolver.query(".".join(((str(arecords[0])).split("."))[::-1]) + ".in-addr.arpa", "PTR")
except :
    print("Problem extracting PTR records")
    ptrrecords = []

#arecords = resolver.query(url, "A")
#mxrecords = resolver.query(url, "MX")
#nsrecords = resolver.query(url, "NS")
# print(".".join((url.split("."))[::-1]) + ".in-addr.arpa")
# url = "216.58.202.206"  # Must come from "A"

#ptrrecords = [0, 0, 0]
#ptrrecords = resolver.query(".".join(((str(arecords[0])).split("."))[::-1]) + ".in-addr.arpa", "PTR")


#  print(arecords.rrset.ttl)

#  print(socket.gethostbyname(str(ptrrecords[0])))

#  Add try exception

#VALUES NEEDED: QUANTITIES OF A, MX AND NS , PTR_EQ_A

print("A:")
#print(getIp(arecords[0]))  # Fist IP
#print(asndb.lookup(getIp(arecords[0])))  # ASN of first IP //Only the ASN?
print_records(arecords)

print("MX:")
#print(getIp(mxrecords[0]))  # Fist IP
#print(asndb.lookup(getIp(mxrecords[0])))  # ASN of first IP 
print_records(mxrecords)

print("NS:")
#print(getIp(nsrecords[0]))  # Fist IP
#print(asndb.lookup(getIp(nsrecords[0])))  # ASN of first IP 
print_records(nsrecords)

print("PTR:")
#print(getIp(ptrrecords[0]))  # Fist IP
#print(asndb.lookup(getIp(ptrrecords[0])))  # ASN of first IP 
print_records(ptrrecords)

#print("PTR_EQ_A:") #FIRST PTR RECORD EQUALS FIRST A RECORD
#print(getIp(arecords[0]) == getIp(ptrrecords[0]))

ptr_eq_a = 0
'''if (getIp(arecords[0]) == getIp(ptrrecords[0])):
    ptr_eq_a = 1  # 1 TRUE 0 FALSE'''

with open ("/home/antonio/NetBeansProjects/CloneProphilerV1/src/resources/dns_res.csv", "a") as file: # File must be present
    writer = csv.writer(file, delimiter=',', quotechar='"')
    writer.writerow([len(arecords), len(mxrecords), len(nsrecords), ptr_eq_a])
    print("Written")

"""with open("res.txt", "w") as file:
    for record in arecords:
        file.write(str(record) + "\n")
    for record in mxrecords:
        file.write(str(record) + "\n")
    for record in nsrecords:
        file.write(str(record) + "\n")
    for record in ptrrecords:
        file.write(str(record) + "\n")"""
