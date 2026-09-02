***vad ni såg***
***vad ni trodde först***
***vad ni kontrollerade*** 
***vad felet var***
***och hur ni skulle ha rättat det***



Krabba 1
***vad ni såg***
Lampan på switchen lyser inte. Show interfaces status visar notconnect på porten.

***vad ni trodde först***
Antingen så fungerar inte kabeln eller porten. 

***vad ni kontrollerade*** 
Loggar in på switchen och kollar på den portens interface vad det står.
Den är avstängd.
I terminalen skriver jag- int g0/1 
sedan- no shutdown
sedan- wr
kontrollerar igen i interface om det tog, om porten nu är på eller fortfarande av.

***vad felet var***
Felet är oftast att kabeln är trasig eller sitter i fel port, eller så är enheten i andra änden avstängd.

***och hur ni skulle ha rättat det***
Jag tror att jag gjorde rätt, om porten är trasig så måste jag märka det också så att inte nästa person använder den trasiga porten. Alternativt om kabeln var problemet får jag byta kabel.



Krabba 2

***vad ni såg***
Anslutningen fungerar, men överföringar tar orimligt lång tid. I loggen
syns raden %CDP-4-DUPLEX_MISMATCH, och räknarna stiger i bägge ändarna.

***vad ni trodde först***
Att det är en duplex mismatch, att hastigheten är olika på de olika portarna.

***vad ni kontrollerade*** 
***vad felet var***
***och hur ni skulle ha rättat det***








