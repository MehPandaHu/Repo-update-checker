YAML update checker : 


%%% Replace this URL with the URL of the YAML file you want to monitor  %%%

Summary : 

Fetches the Latest Content: It retrieves the latest version of the YAML file from a specified URL.

Reads the Last Known Content: It reads the previously stored content from a local file (last_content.txt).

Parses the YAML Content: It extracts the DestinationHostname values from the YAML content.

Compares Content: It compares the newly fetched DestinationHostname values with the previously stored values.

Detects and Displays Updates: If there are new hostnames added to the DestinationHostname list, it prints these newly added hostnames to the console.

Updates Stored Content: It updates the local file with the latest DestinationHostname values.
