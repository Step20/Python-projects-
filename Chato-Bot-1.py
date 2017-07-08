import random
import time
import subprocess

print( "=============================================================================================================================")
print("""\

      ::::::::  :::    :::     ::: ::::::::::: ::::::::          :::::::::   :::::::: :::::::::::       :::     :::   ::: 
    :+:    :+: :+:    :+:   :+: :+:   :+:    :+:    :+:         :+:    :+: :+:    :+:    :+:           :+:     :+: :+:+:  
   +:+        +:+    +:+  +:+   +:+  +:+    +:+    +:+         +:+    +:+ +:+    +:+    +:+           +:+     +:+   +:+   
  +#+        +#++:++#++ +#++:++#++: +#+    +#+    +:+         +#++:++#+  +#+    +:+    +#+           +#+     +:+   +#+    
 +#+        +#+    +#+ +#+     +#+ +#+    +#+    +#+         +#+    +#+ +#+    +#+    +#+            +#+   +#+    +#+     
#+#    #+# #+#    #+# #+#     #+# #+#    #+#    #+#         #+#    #+# #+#    #+#    #+#             #+#+#+#     #+#      
########  ###    ### ###     ### ###     ########          #########   ########     ###               ###     #######    
                                                                                          
                    """)
print("=============================================================================================================================")
print(" ")
greetUser = ['hi', 'hello'];
timeUser = ['time', 'whats the time'];
urlUser1 = ['goto youtube'];
urlUser2 = ['goto google'];
urlUser3 = ['goto website'];
openUser1 = ['open firefox'];

greetBot = ['Bot: Hello sir', 'Bot: Master Welcome!'];
elseBot = ['Bot: Type something!', 'Bot: Try again!'];

def talking():
  while True:
    talkEnter = input("You:");
    if talkEnter in greetUser :
     print (random.choice(greetBot))
     
    elif talkEnter in timeUser:
     print("Bot: " + time.ctime())
    
	
		
    else:
     print (random.choice(elseBot))
  	
talking()
