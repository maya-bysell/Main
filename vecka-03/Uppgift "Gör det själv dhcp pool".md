***Uppgift utförd i CPT****

192.168.1.164/26

Nätadress: 192.168.1.64 
Broadcastadress: 192.168.1.127
Totalt adressintervall: 192.168.1.64 till 192.168.1.127
Användbart adressintervall (för enheter): 192.168.1.65 till 192.168.1.126
.
.
.
<img width="628" height="356" alt="Image" src="https://github.com/user-attachments/assets/9feeca30-6835-4b76-8baf-b751dbd6842d" />
Router> enable
Router# configure terminal
Router(config)# interface gigabitEthernet 0/0
Router(config-if)# ip address 192.168.1.65 255.255.255.192
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)# exit
.
.
.


Router# show ip interface brief

Leta efter ditt interface (t.ex. GigabitEthernet0/0) i listan. Kontrollera att det står 192.168.1.65 under IP-address, och att status står som up (i båda kolumnerna).
.
.
.

Router# configure terminal
Router(config)# ip dhcp excluded-address 192.168.1.65 192.168.1.79
Router(config)# ip dhcp pool MIN_POOL
Router(config-dhcp)# network 192.168.1.64 255.255.255.192
Router(config-dhcp)# default-router 192.168.1.65
Router(config-dhcp)# exit
.
.
.

Datorn ska nu automatiskt få en adress. Eftersom vi exkluderade upp till .79, ska datorn få den första lediga adressen direkt efter, 
det vill säga 192.168.1.80 med nätmasken 255.255.255.192 och gateway 192.168.1.65.
.
.
.


Gå in på datorns IP Configuration igen. Ändra tillbaka till Static (så att du kan redigera).
Behåll IP-adressen 192.168.1.80 men ändra Subnet Mask manuellt till 255.255.255.0.
Öppna Command Prompt på datorn och skriv ping 192.168.1.65.
Når den fortfarande gatewayen? Ja, pinget kommer att lyckas.
När du ändrar datorns nätmask till /24 (255.255.255.0) tror datorn att dess eget nätverk sträcker sig hela vägen från .0 till .255.
Eftersom routerns IP (.65) ligger inom detta intervall, tror datorn att routern befinner sig på exakt samma lokala nätverk som den själv.
Datorn skickar därför ut ett lokalt ARP-rop och skickar paketet direkt. 
Routern (som fortfarande har kvar sin /26-mask) ser också adressen .80 som en del av sitt eget nätverk (som ju sträcker sig till .127),
och svarar därför på pinget utan problem.
.
.
.

  

  Gör två tester från datorns Command Prompt:Testa att pinga en annan server/dator i samma nät (t.ex. en annan PC på adress .81).
  Testa att pinga en adress på internet (t.ex. 8.8.8.8).



  Når den fortfarande servern i samma nät? Ja.Varför: En dator behöver aldrig en gateway för att prata med enheter på sitt eget lokala nätverk. 
  Den använder bara enhetens MAC-adress för att skicka trafiken direkt via switchen.


  Når den internet? Nej.Varför: Så fort en dator ska skicka ett paket till en IP-adress som ligger utanför dess eget subnät, 
  måste den skicka paketet till sin "Default Gateway" (routern) som agerar dörr ut till resten av världen. 
  Utan en inskriven gateway-adress vet datorn inte vart den ska skicka paketet, och trafiken stoppas direkt på datorn.

  
  
