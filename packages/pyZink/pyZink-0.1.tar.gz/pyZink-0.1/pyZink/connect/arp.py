from scapy.all import Ether, ARP, srp

def arp_client(target_ip, exit_interface, target_mac = None) -> None:
    # Based on script by thebear132
    if not target_mac:
        print("Paramter target_mac not set, defaulting to broadcast target (MAC Address: ff:ff:ff:ff:ff:ff)")
        target_mac = "ff:ff:ff:ff:ff:ff"

    arp_request = Ether(dst=target_mac) / ARP(pdst=target_ip)
    print(f"\n[{exit_interface}] Sent ARP Request to {target_mac}: Who has {target_ip}")
    result = srp(arp_request, timeout=2, iface=exit_interface, verbose=False)
    answered, _ = result

    for _, receive in answered:
        print(f"[{exit_interface}] Got ARP Reply: {receive.psrc} is on {receive.hwsrc}")
    if not answered:
        print(f"[{exit_interface}] Timeout: Got no ARP Reply for {target_ip} sent to {target_mac}")

if __name__ == "__main__":
    arp_client("1.1.1.1", exit_interface="Wi-Fi")