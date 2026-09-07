import ipaddress

# Byt ut mot det nat du vill rakna pa.
text = "192.168.1.128/26"

# Modulen ipaddress gor rakningen at dig.
net = ipaddress.ip_network(text, strict=False)

# Alla adresser du kan ge till en enhet.
usable = list(net.hosts())

print(f"Nat: {net.network_address}")
print(f"Natmask: {net.netmask}")
print(f"Broadcast: {net.broadcast_address}")
print(f"Forsta adress: {usable[0]}")
print(f"Sista adress: {usable[-1]}")
print(f"Antal enheter: {len(usable)}")

# 192.168.1.64/26 och 192.168.1.100/26 får samma adress-resultat på grund av att om man letar efter var siffran 100 hamnar i blocket,
# så ser man att 100 landar precis mitt emellan 64 och 127. Den tillhör alltså Subnät 2.
# När en dator eller router ska räkna ut vilket nätverk den tillhör, så "rensar" den bort dator-bitarna och tittar bara på nätverksbitarna. 
# gör man den uträkningen på 192.168.1.100/26, så blir svaret 192.168.1.64/26
## hejhej