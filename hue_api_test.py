'''
Created on Apr 20, 2015

@author: bonino

Copyright (c) 2015 Dario Bonino
 
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
 
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
'''
import math
from hue_api import HueBridge


def computeHue(value,max_value):
    hue_red = 65535
    hue_green = 25500
    #drive the hue with colors depending on the current power, use simple learning of maximum value
    ratio = 1
    if(max_value > 0):
        ratio = min(1, value / max_value) 
    #compute the current hue
    return int(math.floor(hue_green+(hue_red-hue_green)*ratio))

def main():
    #the bridge id
    bridge = HueBridge("http://192.168.1.100/api/python-hue")
    #set the hue for the first lamp
    lamp_id = 3
    
    # the string to render as speech, initially empty
    string = ""
    while (string != "exit"):
        # get the next input
        string = raw_input("Insert a number between 0 and 255 (or type 'exit'):\n>")
        
        # if the given string is "exit" interrupt the loop and say goodbye
        if(string == "exit"):
            print "Goodbye!"
        else:
            try:
                #get the requested hue
                req_hue = int(string)
                #compute the actual hue
                hue = computeHue(req_hue, 255.0);
                #debug
                print ("Hue:%s"%hue)
                #set the hue
                bridge.setHue(lamp_id,hue)
            except:
                pass
    
    
    
if __name__ == '__main__':
    main()