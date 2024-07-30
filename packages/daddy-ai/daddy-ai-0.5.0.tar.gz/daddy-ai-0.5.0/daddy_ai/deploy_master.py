import os
import time
import subprocess
from datetime import datetime
from getpass import getpass

class DeployMaster:
    def __init__(self):
        pass

    def deploy(self, command, script_path, time_slots):
        self._validate_paths(command, script_path)
        time_slots = [(self._parse_time(start), self._parse_time(end)) for start, end in time_slots]
        self._setup_reboot(command, script_path, time_slots)  # Set up the script to start on reboot
        while True:
            current_time = datetime.now().time()
            if any(start <= current_time <= end for start, end in time_slots):
                self.run_command(command, script_path)
            time.sleep(60)  # Check every minute

    def run_command(self, command, script_path):
        full_command = f"python3 {os.path.join(script_path, command)}"
        process = subprocess.Popen(full_command, shell=True, preexec_fn=os.setsid)
        while True:
            if process.poll() is not None:  # Process finished
                process = subprocess.Popen(full_command, shell=True, preexec_fn=os.setsid)
            time.sleep(60)  # Check every minute

    def _parse_time(self, time_str):
        return datetime.strptime(time_str, "%H:%M:%S").time()

    def _validate_paths(self, command, script_path):
        if not os.path.exists(script_path):
            raise FileNotFoundError(f"The specified script path does not exist: {script_path}")
        if not os.path.isfile(os.path.join(script_path, command)):
            raise FileNotFoundError(f"The specified command file does not exist at the given path: {os.path.join(script_path, command)}")

    def _setup_reboot(self, command, script_path, time_slots):
        # Create a systemd service file to run this script on reboot
        service_content = f"""
[Unit]
Description=daddy-ai DeployMaster Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 -c 'from daddy_ai.deploy_master import DeployMaster; setup = DeployMaster(); setup.deploy("{command}", "{script_path}", {time_slots})'
Restart=always
User=root

[Install]
WantedBy=multi-user.target
"""

        service_file_path = '/etc/systemd/system/daddy-ai-deploymaster.service'
        try:
            with open(service_file_path, 'w') as service_file:
                service_file.write(service_content)
            subprocess.run(['sudo', 'systemctl', 'daemon-reload'], check=True)
            subprocess.run(['sudo', 'systemctl', 'enable', 'daddy-ai-deploymaster.service'], check=True)
            subprocess.run(['sudo', 'systemctl', 'start', 'daddy-ai-deploymaster.service'], check=True)
        except PermissionError:
            print("Root privileges are required to set up the reboot service.")

