import os
import subprocess
from datetime import datetime, timedelta
import getpass
import tempfile

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
ExecStart=/usr/bin/python3 {os.path.join(script_path, command)}
WorkingDirectory={script_path}
Restart=always
RestartSec=10
User={self.username}
StandardOutput=append:/home/devl/daddy_ai_service.log
StandardError=append:/home/devl/daddy_ai_service_error.log

[Install]
WantedBy=multi-user.target
"""

        timer_content = ""
        for i, (start, end) in enumerate(time_slots):
            timer_content += f"""
[Timer{self.service_name}{i}]
OnCalendar=*-*-* {start}..{end}
Unit={self.service_name}.service
"""

        service_file_path = f'/etc/systemd/system/{self.service_name}.service'
        timer_file_path = f'/etc/systemd/system/{self.service_name}.timer'

        try:
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
                temp_file.write(service_content)
                temp_file_path = temp_file.name

            self._run_with_sudo(f'mv {temp_file_path} {service_file_path}')
            self._run_with_sudo('systemctl daemon-reload')
            self._run_with_sudo(f'systemctl enable {self.service_name}.service')

            with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
                temp_file.write(timer_content)
                temp_file_path = temp_file.name

            self._run_with_sudo(f'mv {temp_file_path} {timer_file_path}')
            self._run_with_sudo('systemctl daemon-reload')
            self._run_with_sudo(f'systemctl enable {self.service_name}.timer')
            self._run_with_sudo(f'systemctl start {self.service_name}.timer')
            print(f"Service '{self.service_name}' setup completed successfully.")
            
            # Check service status
            status = self._run_with_sudo(f'systemctl status {self.service_name}.service')
            print(f"Service status:\n{status}")
            
        except subprocess.CalledProcessError as e:
            print(f"Error setting up service: {e}")
            raise
        finally:
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)

    def _verify_sudo(self):
        try:
            password = getpass.getpass("Enter sudo password: ")
            full_command = f"echo '{password}' | sudo -S true"
            subprocess.run(full_command, shell=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def _run_with_sudo(self, command):
        full_command = f"echo '{self.password}' | sudo -S {command}"
        result = subprocess.run(full_command, shell=True, capture_output=True, text=True, check=True)
        if result.stderr:
            print(f"Warning: {result.stderr}")
        return result.stdout
