import ipaddress

def parse(value:str):
    return ipaddress.ip_address(value.strip())

def classify(value:str):
    ip=parse(value)
    return {"version":ip.version,"private":ip.is_private,"loopback":ip.is_loopback,"multicast":ip.is_multicast,"global":ip.is_global}
