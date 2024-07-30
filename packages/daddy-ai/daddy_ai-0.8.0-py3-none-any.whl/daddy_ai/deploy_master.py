import os
import time
import subprocess
from datetime import datetime
from getpass import getpass

class DeployMaster:
    def __init__(self):
        self.username = None
        self.password = None

    def accounts(self, username, password):
        self.username = username
        self.password = password

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
        full_command = f"{os.path.join(script_path, command)}"
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
        if self.username is None or self.password is None:
            raise PermissionError("Root privileges are required to set up the reboot service. Please set the username and password using the accounts method.")

        # Create a systemd service file to run this script on reboot
        service_content = f"""
[Unit]
Description=daddy-ai DeployMaster Service
After=network.target

[Service]
ExecStart={os.path.join(script_path, command)}
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
            self._run_with_sudo(service_content, service_file_path)

    def _run_with_sudo(self, service_content, service_file_path):
        service_content_escaped = service_content.replace('"', '\\"').replace('\n', '\\n')
        cmd = f"echo '{self.password}' | sudo -S bash -c 'echo \"{service_content_escaped}\" > {service_file_path}'"
        subprocess.run(cmd, shell=True, check=True)
        subprocess.run(f"echo '{self.password}' | sudo -S systemctl daemon-reload", shell=True, check=True)
        subprocess.run(f"echo '{self.password}' | sudo -S systemctl enable daddy-ai-deploymaster.service", shell=True, check=True)
        subprocess.run(f"echo '{self.password}' | sudo -S systemctl start daddy-ai-deploymaster.service", shell=True, check=True)
