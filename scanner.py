import sys
import time
import threading
from queue import Queue
from scapy.all import *
from colorama import init, Fore

# Initialize colorama for colored output
init()

# Lock to ensure text doesn't overlap when printing
print_lock = threading.Lock()

def get_target():
    """Validates user input."""
    if len(sys.argv) != 2:
        print(f"{Fore.RED}[!] Usage: python scanner.py <Target IP>{Fore.RESET}")
        print(f"{Fore.YELLOW}[*] Example: python scanner.py 192.168.1.1{Fore.RESET}")
        sys.exit(1)
    return sys.argv[1]

def scan_port(target_ip, port):
    """
    Performs a TCP SYN Scan (Stealth Scan).
    1. Sends SYN packet.
    2. Listens for SYN-ACK (Open) or RST (Closed).
    3. Never completes the handshake (Stealthier than full connect).
    """
    try:
        src_port = RandShort() # Randomize source port
        
        # Craft the SYN packet
        packet = IP(dst=target_ip)/TCP(sport=src_port, dport=port, flags="S")
        
        # Send and wait 1s for response (verbose=0 hides scapy junk text)
        response = sr1(packet, timeout=1, verbose=0)

        if response:
            if response.haslayer(TCP):
                flags = response.getlayer(TCP).flags
                
                # 0x12 is SYN-ACK (Port is OPEN)
                if flags == 0x12:
                    with print_lock:
                        print(f"{Fore.GREEN}[+] Port {port:<5} is OPEN  (Service: {socket.getservbyport(port, 'tcp')}){Fore.RESET}")
                    
                    # Send RST to close connection politely
                    rst_packet = IP(dst=target_ip)/TCP(sport=src_port, dport=port, flags="R")
                    send(rst_packet, verbose=0)
                
                # 0x14 is RST-ACK (Port is CLOSED) - Do nothing
                elif flags == 0x14:
                    pass 

    except KeyboardInterrupt:
        sys.exit()
    except Exception:
        pass # Ignore errors for cleaner output

def worker(target_ip, q):
    """The worker thread function."""
    while True:
        port = q.get()
        scan_port(target_ip, port)
        q.task_done()

def main():
    target_ip = get_target()
    
    print(f"\n{Fore.CYAN}--- STARTING STEALTH SYN SCAN ON {target_ip} ---{Fore.RESET}")
    print(f"{Fore.CYAN}--- SCANNING TOP 1000 PORTS ---{Fore.RESET}\n")
    
    # Create Queue and Threads
    q = Queue()
    
    # Spawn 50 threads (adjust this number based on your CPU)
    for _ in range(50):
        t = threading.Thread(target=worker, args=(target_ip, q))
        t.daemon = True
        t.start()
    
    # Add ports 1-1000 to the queue
    for port in range(1, 1001):
        q.put(port)
    
    # Wait for threads to finish
    q.join()
    
    print(f"\n{Fore.CYAN}--- SCAN COMPLETE ---{Fore.RESET}")

if __name__ == "__main__":
    main()
