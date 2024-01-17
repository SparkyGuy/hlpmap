import os


#print the ASCII art
def print_ascii(fn):
    f= open(fn,'r')
    print(''.join([line for line in f]))
print_ascii('hlpmap.txt')

print('\n          WELCOME TO THE HLPMAP v0.1')
print("\n")


print('1. SIMPLE PORT SCAN    ','6. PING SCAN')
print("\n")
print('2. OS SCAN             ','7. POPULAR PORTS SCAN' )
print("\n")
print('3. MULTIPLE IP SCAN    ','8. IP RANGES SCAN')
print("\n")
print('4. TEXT FILE SCAN      ','9. PORT RANGES SCAN') 
print("\n")
print('5. CVE DETECTION       ','10. DETECT SERVICES')


option = input ("\n \n SELECT A NUMBER: ")

match option:
    case "1":
        dom = input("write the domain or IP address: ")
        os.system("nmap " + dom)
    case "2":
        dom = input("write the domain or IP address: ")
        os.system("nmap -A -T4 " + dom)
    case "3":
        dom = input("write the domain or IP address separated by a space: ")
        os.system("nmap " + dom)
    case "4":
        dom = input("write the path of the file: ")
        os.system("nmap -iL " + dom)
    case "5":
        dom = input("write the domain or IP address: ")
        os.system("nmap -Pn --script vuln " + dom)
    case "6":
        dom = input("write the domain or IP address: ")
        os.system("nmap -sP " + dom)
    case "7":
        dom = input("write the domain or IP address: ")
        os.system("nmap --top-ports " + dom)
    case "8":
        dom = input("write the domain or IP address: ")
        os.system("nmap " + dom)
    case "9":
        dom = input("write the ports of the address separated by a dash: ")
        os.system("nmap -p " + dom)
    case "10":
        dom = input("write the domain or IP address: ")
        os.system("nmap -sV " + dom)
    case "":
        print_ascii('bye.txt')