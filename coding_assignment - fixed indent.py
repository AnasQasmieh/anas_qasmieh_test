# Implement a function that converts a mapping of IPs to hostnames into a mapping of hostnames to IPs.
# You may assume all IPs are singular IPv4 IPs, not IP ranges.
# You may assume that the IPs and Hostnames are all strings.
# Results should be output as a python dictionary with string keys and list values.
# If an input dictionary of hostnames to IPs is provided to an optional named variable "existing_hosts", then the results should be merged with the dictionary.
# If there is a conflict (existing host name), the new list should be concatenated to the end of the existing list, excluding any repeated IPs.
# Include a proper docstring

# Also include a list of test cases for your function in separate file "test_cases.txt". The test cases should cover any edge cases you identity. You need not code the test cases.

# Your code should be able to be imported. We will import your python module and test the convert_mapping function against tests of our own.
# Make sure your code doesn't have syntax errors.
# We will be using python 3.6+

# Expected solution time limit: 1hrs. Please try to turn your solution in before then.
# Keep in mind that there is no singular correct solution.
# This assignment is designed is to gauge your skills and give us an idea of how you approach tasks relevant to the Software Developer role.  
# We encourage you to move forward with your assumptions and add the necessary context for us as comments to let us understand those assumptions.
# If your solution is not functional due to syntax errors, please take some time to fix those before submitting.
# We will not consider answers that python 3.6+ will not load.

# To aid you in testing, we have provided another file, tester.py
# Execute that file using python to simulate what our own test script will do
# Example: `python tester.py`
# That script should then output some data indicating if your solution functioned as expected.
# Keep in mind that our script will test more test cases than just the example provided in that file
# That script will also warn you if your python version is lower than the python versions we may test with (3.6+).

# This is your chance to impress us. Send your best code forward. All the best!

#Template
def convert_mapping(ips_to_hosts, existing_hosts={}): #NOTE: "existing_hosts" should be modified to be an optional variable
    """
    Convert a mapping of IPs to hostnames into a mapping of hostnames to IPs. Merge with existing mapping of hostnames to IPs, if provided.
	Parameters:
		# ips_to_hosts (dict): IPs to hosts mapping to convert.
		# existing_hosts (dict): Existing hostnames to IPs mapping to merge with output.
	Returns:
		# (dict): Updated hostnames to IPs mapping.
    """
    #implement your solution here
    if ips_to_hosts == {}:
        return existing_hosts
	
    new_known_hosts = dict()
    for ip in ips_to_hosts:
        host = ips_to_hosts[ip]
        if host not in new_known_hosts.keys():
            new_known_hosts[host] = [ip]
        else:
            new_known_hosts[host].append(ip)
	
    if existing_hosts == {}:
        return new_known_hosts
	
    for key_new in new_known_hosts:
        if key_new in existing_hosts.keys():
            known_ips_set = set(existing_hosts[key_new])
            new_ips_set = set(new_known_hosts[key_new])
            existing_hosts[key_new] = existing_hosts[key_new] + list(new_ips_set - known_ips_set)
        else:
            existing_hosts[key_new] = new_known_hosts[key_new]
	
    return existing_hosts

#For example inputs and outputs check accompanying tester.py