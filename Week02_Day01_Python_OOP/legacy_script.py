# Legacy Infrastructure Script (Non-OOP)

# Database Servers
db1_name = "DB-Master"
db1_ip = "192.168.1.10"
db1_status = "running"
db1_cpu_cores = 8

db2_name = "DB-Replica"
db2_ip = "192.168.1.11"
db2_status = "stopped"
db2_cpu_cores = 4

# Web Servers
web1_name = "Web-Frontend"
web1_ip = "192.168.1.20"
web1_status = "running"

def start_server(name, ip, status):
    if status == "running":
        print(f"[{name}] is already running at {ip}.")
        return "running"
    else:
        print(f"[{name}] Starting server at {ip}...")
        return "running"

def stop_server(name, ip, status):
    if status == "stopped":
        print(f"[{name}] is already stopped.")
        return "stopped"
    else:
        print(f"[{name}] Stopping server at {ip}...")
        return "stopped"

def show_db_info(name, ip, status, cores):
    print(f"Database: {name} | IP: {ip} | Status: {status} | Cores: {cores}")

# --- Execution ---
print("--- Infrastructure Status ---")
show_db_info(db1_name, db1_ip, db1_status, db1_cpu_cores)
show_db_info(db2_name, db2_ip, db2_status, db2_cpu_cores)

print("\n--- Maintenance Actions ---")
db2_status = start_server(db2_name, db2_ip, db2_status)
web1_status = stop_server(web1_name, web1_ip, web1_status)
