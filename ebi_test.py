import sys
import requests
import json
import string
#import dumper

# Variable declaration
arg_dict = {
   '--total_count' : ['page','totalElements'],
   '--acc'         : ['_embedded','samples'],
   '--attr'        : ['_embedded','samples']
}

ARG = ""

########### Processing input arguments and forming URL ############
if sys.argv[1] == '--acc':
   ARG = "?filter="+string.replace(sys.argv[1], '--', '')+":"+sys.argv[2]
elif sys.argv[1] == '--attr':   
   ARG = "?text="
   for args in sys.argv[2:]:
      ARG += "&filter="+string.replace(sys.argv[1], '--', '')+":"+args
   ARG += "&size=5795298"

main_url = "https://www.ebi.ac.uk/biosamples/samples"
url = main_url+ARG          # Prepare URL

#print "URL : "+url

#####################    Functions   ###############################
# Defining function to connect the REST API and fetch the requested data
def connect_api (arg):
   myResponse = requests.get(arg, verify=True)
   # If API call success, response code will be 200
   if(myResponse.ok):
      # Loading the response data into a dict variable
      jsonResponse = json.loads(myResponse.content)
      jsonData = jsonResponse[arg_dict[sys.argv[1]][0]][arg_dict[sys.argv[1]][1]]
      #print dumper.dump(jsonResponse[arg_dict[sys.argv[1]][0]][arg_dict[sys.argv[1]][1]])
      return jsonData
   else:
      # If response code is not 200, print the resulting http error code with description
      myResponse.raise_for_status()


# Function to fetch each records of JSON data and process it based on the requirement
def fetch_content(Content):
   # Preparing the list to print
   out = []
   if type(Content) is int:
      out.append("Total count of samples : "+str(Content))
      return out
   elif type(Content) is list and sys.argv[1] == '--acc':
      for item in Content:
         key =  ""
         if ('sample name' in item["characteristics"]):
            key = item["characteristics"]["sample name"] 
         else: 
            key = item["characteristics"]["secondary description"]        
         for name in key:
            if "Sample name" in name["text"]:
               out.append(name["text"])
            else:
               out.append("Sample name is: "+name["text"])
         return out
   elif type(Content) is list and sys.argv[1] == '--attr':
      print "Accession\tAttribute:Value pairs"
      args = (", ".join(sys.argv[2:]))
      for item in Content:
         out.append(item["accession"]+"\t"+args)
      return out

######################  Main program ########################################## 

DataContent  = connect_api (url)            # Function call to connect REST API
out = fetch_content(DataContent)    # Function call to process the JSON output data
for out_items in out:
   print out_items
