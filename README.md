# Cattack
A educational LFI exploit tool that works on severely misconfigured systems.

## DISCLAIMERS
This script is the digital equivalent of a fireworks display in a library. 
It is not meant to be stealthy, subtle, or remotely covert. It's as conspicuous as 
a marching band in a monastery. Tread with caution, and remember, with great power 
comes great responsibility to not do something monumentally stupid and irresponsible.
This was inspired by the tryhackme "dogcat" room, check it out one day, it's unique.

This script is aimed at educating. It should only be used for educational purposes, it is meant to teach you to some extent, the theory and practices used to set up LFI exploits. This does not cover everything, and the range of attack is very limited, making it great for education, mostly because it only works on old versions of apache2, and you would have to have many misconfigurations for it to become a very dangerous possibilty. Dispite these benefits, there is still a chance it could be used for harm, and I do not condone these actions, you are responsible for your own actions and if you misuse this, you could face legal issues.

All credit to "Pentestmonkey" for the php reverse shell.

Now that the first disclaimer is over, let's move over to the legal side of things:

This tool may be used for legal purposes only.  Users take full responsibility for any actions performed using this tool.
The author accepts no liability for damage caused by this tool.
If these terms are not acceptable to you, then do not use this tool.




                                                                                                    
                                                              .................:*+.....                 
                                                         . ..  ..=@@@@@@@@@@@@@@@#@@...                 
                                                        .....=@@@@@@@@@@@@@@@@@@@@:.                    
                                                  . .....=%@@@@@@@@@@@@@@@@@@@@@.                       
                                                  ...+@@@@@@@@@@@@@@@@@@@@@@@@@@#                       
                                               ...#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*                       
                                         ......+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                       
                                         ....@@@@@@@@@@@@@@@@@@@@@@@@@....@@@@@@.                       
                                         ..#@@@@@@@@@@@@@@@@@@@@@@@@@%......:#@@@:..                    
                                         .@@@@@@@@@@@@@@@@@@@@@@@@@@@+..+@@@@@@@@@=.                    
                                      ...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=......                    
                                      ..*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-. ... ...                    
                                      .:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+...                             
                                      .@@@@@@@@@@@@@@@@@@@@@@@@@@:*#....                                
                                      -@@@@@@@@@@@@@@@@@@@@@@@@@+. .....                                
    _______________________________...@@@@@@@@@@@@@@@@@@@@@@@@@@:.______________________.                
                                   ..+@@@@@@@@@@@@@@@@@@@@@@@@@@:.                       .               
                                   ..@@@@@@@@@@@@@@@@@@@@@@:@@@@*.                        .              
                                   .+@@@@@@@@@@@@@@@@@@@@@..%@@@@.                         .             
                                   .@@@@@@@@@@@@@@@@@@@@@....@@@@.                          .            
                 *@@%.....      ...-@@@@@@@@@@@@@@@@@@@@@@@%-.@@@@@+....                     .           
                 :@@@@@@+.... .:+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@...                      .          
                 ...#@@@@@@@@@@@@@@@=....::----------::::::::....:::....                       .         
                      ...--===:...                                                              .        
                      ............                                                               .       
    ..............................................................................................
      #####                                          ###                                          |
     #     #   ##   ##### #####   ##    ####  #    # ###                                          |
     #        #  #    #     #    #  #  #    # #   #  ###                                          |
     #       #    #   #     #   #    # #      ####    #                                           |
     #       ######   #     #   ###### #      #  #                                                |
     #     # #    #   #     #   #    # #    # #   #  ###                                          |
      #####  #    #   #     #   #    #  ####  #    # ###                                          |
    ______________________________________________________________________________________________|                                           

The not-so-subtle LFI exploit, inspired by the dogcat room in tryhackme.com with it's unique LFI vulnerability.

## Installation

This has only been tested for linux, so I'm going to leave it for linux (for now, come back later!):

### Linux ###
The very first thing you should do (as always) is download the repository via git:

    git clone https://github.com/ethicalhacker7192/Cattack

After you have cloned the repository, navigate into the repository and download the 'requests' module via pip, and you're good to go!:

    cd Cattack
    python3 -m pip install requests
    python3 Cattack.py

Please use this for only educational purposes, you are responsible for your own actions.

