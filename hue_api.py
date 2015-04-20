'''
Created on Apr 15, 2014

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
import rest

class HueBridge:
    '''
    A class representing a Philips HUE bridge
    '''
    def __init__(self, url):
        
        #remove trailing slashes
        if(url[-1]=='/'):
            url = url[:-1]
        
        #store the base api url
        self.url = url
        
        #build the devices url
        self.lights_url = self.url+"/lights"
        
    def getAllLights(self):
        '''
        Provides a dictionary of all available devices and capabilities
        '''
        return rest.send(url = self.lights_url, headers = {'Accept':'application/json'})
    
    def setHue(self, light_id, hue):
        #compose the specific light url
        url_to_call = self.lights_url+"/"+str(light_id)+"/state"
        #set the given hue value
        body = '{ "on" : true, "hue" : %d}'%hue
        #send the request
        rest.send('PUT', url_to_call, body, { 'Content-Type':'application/json' })