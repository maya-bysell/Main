device_1 = "SW-Nordvik-1"
model_1 = "WS-C3560G-48TS"
role_1 = "Switch, access"

device_2 = "R-Nordvik-1"
model_2 = "CISCO2951"
role_2 = "Router, lager 3"

device_3 = "SW-maya"
model_3 = "tp-link-3"
role_3 = "Router, lager 3"

print("UTRUSTNINGSLISTA")
print("-" * 52)

print(f"{device_1:<16}{model_1:<20}{role_1}")
print(f"{device_2:<16}{model_2:<20}{role_2}")
print(f"{device_3:<16}{model_3:<20}{role_3}")

print("-" * 52)
print("Antal enheter: 3")