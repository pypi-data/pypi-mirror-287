import os
import time
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

    def setup(self, command, script_path, time_slots):
        if not self.service_name:
            raise ValueError("Service name not set. Please call accounts() method first.")
        self._validate_paths(command, script_path)
        time_slots = [(self._parse_time(start), self._parse_time(end)) for start, end in time_slots]
        self._setup_reboot(command, script_path, time_slots)

    def deploy(self, command, script_path, time_slots):
        self._validate_paths(command, script_path)
        time_slots = [(self._parse_time(start), self._parse_time(end)) for start, end in time_slots]
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
        if self.username is None or self.password is None or self.service_name is None:
            raise PermissionError("Root privileges and service name are required to set up the reboot service. Please set the username, password, and service name using the accounts method.")

        if not self._verify_sudo():
            raise PermissionError("Invalid sudo password. Please check your credentials.")

        service_content = f"""
[Unit]
Description={self.service_name} Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 {os.path.abspath(__file__)} run {os.path.join(script_path, command)} {" ".join([f"{start}-{end}" for start, end in time_slots])}
WorkingDirectory={script_path}
Restart=always
User={self.username}

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

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        command = sys.argv[2]
        time_slots = [tuple(slot.split('-')) for slot in sys.argv[3:]]
        script_path = os.path.dirname(command)
        dm = DeployMaster()
        dm.deploy(os.path.basename(command), script_path, time_slots)
