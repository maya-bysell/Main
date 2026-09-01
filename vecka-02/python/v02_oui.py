vendors = {
    "a4:c3:f0": "Intel", 
    "3c:d9:2b": "Hewlett-Packard", 
    "00:1a:a1": "Cisco Systems", 
    "f8:9e:28": "Cisco Meraki",
    "ac:16:15": "Apple, Inc.",
    "e0:55:3d": "Cisco Meraki",
} 

addresses = [ 
    "a4:c3:f0:11:3a:b7", 
    "3c:d9:2b:d2:11:88", 
    "8c:85:90:44:12:0e", 

    #egen
    "f8:9e:28:74:0c:09",
    "e0:55:3d:e1:27:c0",
    "ac:16:15:a2:98:62",
] 

for address in addresses: 
    prefix = address[0:8] 
    if prefix in vendors: 
        name = vendors[prefix] 
    else: 
        name = "okänd tillverkare" 

    print(f"{address} -> {name}")



PS C:\Users\Maya\Documents\python> & C:\Users\Maya\.local\bin\python3.14.exe c:/Users/Maya/Documents/python/.pyyy
a4:c3:f0:11:3a:b7 -> Intel
3c:d9:2b:d2:11:88 -> Hewlett-Packard
8c:85:90:44:12:0e -> okänd tillverkare
f8:9e:28:74:0c:09 -> Cisco Meraki
e0:55:3d:e1:27:c0 -> Cisco Meraki
ac:16:15:a2:98:62 -> Apple, Inc.
PS C:\Users\Maya\Documents\python>

<img width="833" height="924" alt="Image" src="https://github.com/user-attachments/assets/48d9958c-ccc8-43e0-8a05-228f75246e29" />
