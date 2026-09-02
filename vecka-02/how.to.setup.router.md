Sätt upp en topologi.

<img width="436" height="322" alt="image" src="https://github.com/user-attachments/assets/8193699e-9d81-4147-b1df-a47b551b4d8c" />

Börja konfigurera router med följande kommandon.
-
-
-

<img width="445" height="210" alt="image" src="https://github.com/user-attachments/assets/8b01c21e-6874-489c-afd1-c67b3c6fccde" />

Router> enable -> går från usermode till priviledged mode

Router# configure terminal - or - conf t -> Med detta kan du ändra inställningar i routern

Router(config)# Hostname RT-01-Maya -> Byter namn till routern.

RT-01-Maya(config)# exit ->  tar dig tillbaka till priviledged mode

RT-01-Maya# write memory -> sparar running-configuration till startup-configuration

-
-
-

<img width="620" height="163" alt="image" src="https://github.com/user-attachments/assets/7e8d502c-677a-4b74-a174-ccb86299db35" />

RT-01-Maya# interface g0/0   -> interface talar om att du vill hantera ett nätverkskort. g0/0 är kortkommandot för GigabitEthernet 0/0, vilket är portens specifika namn och nummer.

RT-01-Maya(config-if)# ip address 192.168.10.1 255.255.255.0   -> I detta läge kan du tex, ge porten en IP-adress, ändra hastighet/beskrivning på porten eller starta porten med kommandot no shutdown.

RT-01-Maya(config-if)# no shutdown   -> Konfigurerar att porten aldrig ska 'gå ner'

-
-
-

<img width="525" height="239" alt="image" src="https://github.com/user-attachments/assets/005fa259-82a6-4a0c-96c6-5e8b57f16f5e" />
<img width="427" height="214" alt="image" src="https://github.com/user-attachments/assets/05ef6575-2c0c-48f0-a3e2-0623eaaee72b" />


RT-01-Maya(config-if)# -> Nu ska vi konfigurera DHCP

RT-01-Maya(config-if)#ip dhcp pool lan -> talar om för enheten att den ska agera DHCP-server och förbereda en samling (pool) av IP-adresser som kan delas ut till anslutna klienter i det lokala nätverket (LAN)

RT-01-Maya(dhcp-config)#ip dhcp excluded-address 192.168.10.1 192.168.10.9 -> talar om för routern att inte dela ut IP-adresser i intervallet från 192.168.10.1 till 192.168.10.9

RT-01-Maya(dhcp-config)#network 192.168.10.0 255.255.255.0 -> Anger intervallet för IP-adresser som routern kan dela ut till DHCP-klienter (adresserna 192.168.10.1 till 192.168.10.254). 255.255.255.0: Tillämpar en /24-subnätmask som definierar värdintervallet för denna pool.

RT-01-Maya(dhcp-config)#default-router 192.168.10.1 -> bestämmer routerns default ip-adress. Klienterna får veta att all trafik som ska till internet eller ett annat nätverk måste skickas till 192.168.10.1.

RT-01-Maya(dhcp-config)#dns-server 8.8.8.8 -> talar om för routern att använda Googles publika DNS-server med IP-adressen 8.8.8.8 för att översätta webbadresser till IP-adresser. En DNS-server översätter domännamn till IP-adresser så att din dator vet vart den ska skicka trafiken.

wr - för att spara konfigurationen

-
-
-
<img width="751" height="225" alt="image" src="https://github.com/user-attachments/assets/12da1fb7-b6bb-4be5-9c41-9be7c2056505" />


Gå in på en dator, och sedan på IP konfiguration - för att se att dhcp konfigurationen gått igenom och fungerar- vilket man kan se här att den gjorde.

-
-
-
<img width="541" height="407" alt="image" src="https://github.com/user-attachments/assets/75875272-9fb0-436b-9bec-826f234ef049" />

Här pingar jag i samma dators command prompt, som skickar ett paket till switchen - för att jag sedan ska kunna se IP-adressen i MAC-tabellen.

-
-
-
<img width="447" height="152" alt="image" src="https://github.com/user-attachments/assets/8573bd78-15ac-48d0-9b21-c6c7d1fa8495" />

Här går jag in i switchen och ändrar namn. 

-
-
-
<img width="340" height="125" alt="image" src="https://github.com/user-attachments/assets/88340366-1112-49cb-a6fe-f8dc3cf51e06" />

SW-01-Maya#show mac address-table -> Här kan vi nu se datorns MAC-adress. Med detta kommando får du se alla enheter kopplat till switchen(nu har jag bara pingat en adress).Du kan också se hur tabellen har fått adressen (Dynamsikt eller statiskt) samt vilken port.

-
-
-
<img width="565" height="314" alt="image" src="https://github.com/user-attachments/assets/d8ef08f5-88b3-41c4-b63f-e611e8bfc782" />


SW-01-Maya#show interfaces status -> visar alla portar, om de är connected eller inte, duplex-mode, och vilken hastighet porten har.








