from easysnmp import Session

session = Session(hostname='192.168.1.1', community='public', version=2)
iface_status = session.get('.1.3.6.1.2.1.2.2.1.8.1')
print(iface_status.value)