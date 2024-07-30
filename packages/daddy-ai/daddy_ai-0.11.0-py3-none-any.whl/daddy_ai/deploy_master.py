import os
import subprocess
from datetime import datetime
import getpass

class DeployMaster:
    def __init__(self):
        self.username = None
        self.password = None
        self.service_name = None

    def accounts(self, username, password, service_name):
        self.username = username
        self.password = password
        self.service_name = f"{service_name}-daddy-ai"

    def deploy(self, command, script_path, time_slots):
        if not self.service_name:
            raise ValueError("Service name not set. Please call accounts() method first.")
        self._validate_paths(command, script_path)
        time_slots = [(self._parse_time(start), self._parse_time(end)) for start, end in time_slots]
        self._setup_service(command, script_path, time_slots)

    def _parse_time(self, time_str):
        return datetime.strptime(time_str, "%H:%M:%S").time()

    def _validate_paths(self, command, script_path):
        full_path = os.path.join(script_path, command)
        if not os.path.isfile(full_path):
            raise FileNotFoundError(f"The specified script does not exist: {full_path}")

    def _setup_service(self, command, script_path, time_slots):
        if self.username is None or self.password is None or self.service_name is None:
            raise PermissionError("Root privileges and service name are required. Please set the username, password, and service name using the accounts method.")

        if not self._verify_sudo():
            raise PermissionError("Invalid sudo password. Please check your credentials.")

        service_content = f"""
[Unit]
Description={self.service_name} Service
After=network.target

[Service]
ExecStart=/bin/bash -c 'while true; do current_time=$(date +%H:%M:%S); for slot in {" ".join([f"{start}-{end}" for start, end in time_slots])}; do IFS=- read start_time end_time <<< "$slot"; if [[ "$current_time" > "$start_time" && "$current_time" < "$end_time" ]]; then /usr/bin/python3 {os.path.join(script_path, command)}; fi; done; sleep 60; done'
WorkingDirectory={script_path}
Restart=always
RestartSec=10
User=root

[Install]
WantedBy=multi-user.target
"""

        service_file_path = f'/etc/systemd/system/{self.service_name}.service'
        try:
            self._run_with_sudo(f'echo "{service_content}" > {service_file_path}')
            self._run_with_sudo('systemctl daemon-reload')
            self._run_with_sudo(f'systemctl enable {self.service_name}.service')
            self._run_with_sudo(f'systemctl start {self.service_name}.service')
            print(f"Service '{self.service_name}' setup completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error setting up service: {e}")
            raise

    def _verify_sudo(self):
        try:
            self._run_with_sudo('true')
            return True
        except subprocess.CalledProcessError:
            return False

    def _run_with_sudo(self, command):
        full_command = f"echo '{self.password}' | sudo -S bash -c '{command}'"
        result = subprocess.run(full_command, shell=True, capture_output=True, text=True, check=True)
        if result.stderr:
            print(f"Warning: {result.stderr}")
        return result.stdout
