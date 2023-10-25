# Tyler Sabin
# CNE330 – Fall Quarter 10/14/2023
# Source Brian Huang
# Source Zak Rubin

#Your router assigns even IP addresses to Windows machines, and odd IP addresses to Linux machines.
#Write a function, ip_to_operating_system that takes the last octet of an IP address (0-255) and returns “Linux” or
#“Windows” If a user enters 0, report “Router”

def ip_to_operating_system(octet):
    # your code here
    if 0 == octet:
        return "Router"
    elif octet % 2 == 0:
        return "Windows"
    else:
        return "Linux"

print(ip_to_operating_system(182))
print(ip_to_operating_system(42))
print(ip_to_operating_system(-1))
print(ip_to_operating_system(782))
print(ip_to_operating_system(1))