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
        self._setup_reboot(command, script_path, time_slots)
        while True:
            current_time = datetime.now().time()
            if any(start <= current_time <= end for start, end in time_slots):
                self.run_command(command, script_path)
            time.sleep(60)

    def run_command(self, command, script_path):
        full_command = f"{os.path.join(script_path, command)}"
        process = subprocess.Popen(full_command, shell=True, preexec_fn=os.setsid)
        while True:
            if process.poll() is not None:
                process = subprocess.Popen(full_command, shell=True, preexec_fn=os.setsid)
            time.sleep(60)

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

        service_content = f"""
[Unit]
Description=daddy-ai DeployMaster Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 {os.path.join(script_path, command)}
WorkingDirectory={script_path}
Restart=always
User={self.username}

[Install]
WantedBy=multi-user.target
"""

        service_file_path = '/etc/systemd/system/daddy-ai-deploymaster.service'
        try:
            self._run_with_sudo(f'echo "{service_content}" > {service_file_path}')
            self._run_with_sudo('systemctl daemon-reload')
            self._run_with_sudo('systemctl enable daddy-ai-deploymaster.service')
            self._run_with_sudo('systemctl start daddy-ai-deploymaster.service')
            print("Service setup completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error setting up service: {e}")
            raise

    def _run_with_sudo(self, command):
        full_command = f"echo '{self.password}' | sudo -S bash -c '{command}'"
        result = subprocess.run(full_command, shell=True, capture_output=True, text=True, check=True)
        if result.stderr:
            print(f"Warning: {result.stderr}")
        return result.stdout
