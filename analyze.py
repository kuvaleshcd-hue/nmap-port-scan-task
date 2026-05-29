# Nmap Result Analyzer
with open("scan_results.txt") as f:
    lines = f.readlines()

print("=== OPEN PORTS FOUND ===")
for line in lines:
    if "/tcp" in line and "open" in line:
        port = line.split("/")[0].strip()
        service = line.split()[-1].strip()
        print(f"Port {port} -> {service}")

print("\n=== RISK ANALYSIS ===")
risks = {
    "3306": ("MySQL", "HIGH", "Restrict to localhost only"),
    "5000": ("UPnP", "MEDIUM", "Disable if not needed"),
    "7000": ("AFS3", "MEDIUM", "Block externally"),
    "49152": ("Unknown", "HIGH", "Investigate and close immediately")
}
for port, (service, risk, rec) in risks.items():
    print(f"Port {port} | {service} | Risk: {risk} | Fix: {rec}")
