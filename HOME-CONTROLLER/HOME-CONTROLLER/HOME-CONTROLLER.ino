#include "DHT.h"        // including the library of DHT11 temperature and humidity sensor
#include <ESP8266WiFi.h>  
#include <WiFiClient.h> 
#include <ESP8266HTTPClient.h>
#include "UrlEncode.h"
#include "ArduinoJson-5.13.5/ArduinoJson.h"

WiFiClient wifiClient;

const char* ssid     = "sys41x4";         // The SSID (name) of the Wi-Fi network you want to connect to
const char* password = "116c3fa2dbb";     // The password of the Wi-Fi network

const char* server_domain = "192.168.211.179";
const char* cmd_fetch_endpoint = "/fetch_home_controller_command";
const char* cmd_push_endpoint = "/push_home_controller_response";
#define DHTTYPE DHT11   // DHT 11

#define dht_dpin 2
DHT dht(dht_dpin, DHTTYPE);

void setup(void)
{ 
  dht.begin();
  Serial.begin(9600);
  WiFi.begin(ssid, password);             // Connect to the network
  Serial.print("Connecting to ");
  Serial.print(ssid); Serial.println(" ...");
  int i = 0;
  while (WiFi.status() != WL_CONNECTED) { // Wait for the Wi-Fi to connect
    delay(1000);
    Serial.print(++i); Serial.print(' ');
  }
  Serial.println('\n');
  Serial.println("Connection established!");  
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP()); 

  Serial.print("Server Domain: ");
  Serial.println(server_domain);

  
  
  delay(2000);

}
void loop() {

    char *fetch_data_url;
    asprintf(&fetch_data_url, "http://%s%s", server_domain, cmd_fetch_endpoint);
    
    HTTPClient http;    //Declare object of class HTTPClient
    http.begin(wifiClient, fetch_data_url);     //Specify request destination
//    http.begin(wifiClient, "http://192.168.211.179/fetch_home_controller_command");     //Specify request destination
    int httpCode = http.GET();            //Send the request
    String payload = http.getString();
    Serial.println(payload);
    
    free(fetch_data_url);
    
    if(httpCode == 200){
    // Allocate JsonBuffer
    // Use arduinojson.org/assistant to compute the capacity.
    const size_t capacity = JSON_OBJECT_SIZE(3) + JSON_ARRAY_SIZE(2) + 60;
    DynamicJsonBuffer jsonBuffer(capacity);
  
   // Parse JSON object
    JsonObject& root = jsonBuffer.parseObject(payload);
    if (!root.success()){
      Serial.println(F("Parsing failed!"));
      return;
    }
    
    if (root["DATA_SET"]!=NULL){
      char *response;
      if((root["DATA_SET"].as<int>())==1){
//        char response[] = ;
        asprintf(&response, "BEDROOM_LIGHT_TURNED_ON");
      }
      else if((root["DATA_SET"].as<int>())==2){
//        char response[] = ;
        asprintf(&response, "BEDROOM_LIGHT_TURNED_OFF");
      }
      else if((root["DATA_SET"].as<int>())==3){
//        char *response;
        Serial.println("Getting Humidity");
        asprintf(&response, "BEDROOM_HUMIDITY_:_%f_percent", dht.readHumidity());
        Serial.println(urlEncode(response));
      }
      else if((root["DATA_SET"].as<int>())==4){
//        char *response;
        asprintf(&response, "BEDROOM_TEMPERATURE_:_%f_C", dht.readTemperature());
      }
      else{
//        char response[] = ;
        asprintf(&response, "COMMAND_NOT_AVAILABLE");
      }
//      strcpy(str4, str5);
      char *push_data_url;
//      asprintf(&push_data_url, "http://%s%s/%s", server_domain, cmd_push_endpoint, urlEncode(response));
      asprintf(&push_data_url, "http://%s%s/%s", server_domain, cmd_push_endpoint, response);
      
      HTTPClient http_2;    //Declare object of class HTTPClient
      http_2.begin(wifiClient, push_data_url);     //Specify request destination
      int httpCode = http_2.GET();            //Send the request
      String payload = http_2.getString();
      
      free(push_data_url);
      
      http_2.end();  //Close connection
      
      free(response);
    }
  }
  else
  {
    Serial.println("Error in response");
  }
  http.end();  //Close connection

  
  delay(2000);

//    delay(2000);
}
