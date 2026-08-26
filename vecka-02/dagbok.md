kört fast på veckans python. förstod inte alls, men nu tror jag att jag dörstår bättre hur det fungerar

glömde kommatecken efter MAC-adresserna så dom la sig efter varandra på en lång rad.


**Dag 1**
Kört fast i hur man sätter upp ett nätverk på CPT, och vad man ska skriva in för kommandon för att göra uppgifterna, och vart man ska skriva in dom.

Jag kollade en video på hur man gör och förstår lite bättre.

gjorde om steg ett på första övningen igen men får inte till det med att sätta ip-adressen i command prompt(?) minns inte hur man skulle göra,
så jag satte ip, subnet och gateway och bara skrev en ip adress i IP configuration, men jag vet inte om det är rätt.
Men nu får jag fram resultat på alla tre ovan iallafall.

**diy-uppgift**

#felet: Hastigheten är 100 istället för 1000
------
#Felet var att jag anslutit till Fastethernet istället för Gigabitethernet0/1.
----
##Nu bytte jag till ett Gigabit-kort i laptopen för den hade inte det innan, men det verkar inte fungera ändå,
kan inte hitta en lösning, men jag går vidare.
-----
#drog ur kabeln och yes, mac adressen ligger kvar i minnet i 300 sekunder.

------
#stängde av nätverkskortet i laptopen, väntade fem minuter och kollade show mac address-table, och adressen var borta.
Aging, wipe:as efter fem minuter om switchen inte fått någotr livstecken från laptopen.
Går länken ner slänger switchen sina anteckningar om den porten på en gång. 
Aging gäller enheter som tystnar på en port som fortfarande är uppe.

------
