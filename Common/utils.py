def getVT_APIKey():
    # Read the line in the file VT_APIKey and store as a variable called VT_APIKey
    VT_APIKey = open('VT_APIKey', 'r').readline().strip()
    print('VT_APIKey: ' + VT_APIKey)
    return VT_APIKey