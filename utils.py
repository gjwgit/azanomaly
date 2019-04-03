# Endpoint URL can be found in the Azure portal.  for example:
# https://westus2.api.cognitive.microsoft.com
#

# Import the required libraries.

import os
import sys

# Defaults.

KEY_FILE = "private.py"
DEFAULT_REGION = "westus2"

def get_key():
    
    subscription_key = None
    region = DEFAULT_REGION

    # Prompt the user for the key and region and save into private.py
    # for future runs of the model. The contents of that file is:
    #
    # subscription_key = "a14d...ef24"
    # region = "southeastasia"

    if os.path.isfile(KEY_FILE) and os.path.getsize(KEY_FILE) != 0:
        print("""The following file has been found and is assumed to contain
an Azure Speech Services subscription key and region. We will load 
the file and use this information.

    """ + os.getcwd() + "/" + KEY_FILE)
        exec(open(KEY_FILE).read())
    else:
        print("""An Azure resource is required to access this service (and to run this
demo). See the README for details of a free subscription. Then you can
provide the key and the region information here.
""")
        sys.stdout.write("Please enter your Speech Services subscription key []: ")
        subscription_key = input()

        sys.stdout.write("Please enter your region [southeastasia]: ")
        region = input()
        if len(region) == 0: region = DEFAULT_REGION

        if len(subscription_key) > 0:
            assert subscription_key
            ofname = open(KEY_FILE, "w")
            ofname.write("""subscription_key = "{}"
region = "{}"
    """.format(subscription_key, region))
            ofname.close()

            print("""
I've saved that information into the file:

        """ + os.getcwd() + "/" + KEY_FILE)

        endpoint = "https://{}.api.cognitive.microsoft.com".format(region)
        return(subscription_key, endpoint)
