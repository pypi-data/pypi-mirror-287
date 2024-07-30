import os
import time
import subprocess
from datetime import datetime

class DeployMaster:
    def __init__(self):
        pass

    def deploy(self, command, time_slots):
        time_slots = [(self._parse_time(start), self._parse_time(end)) for start, end in time_slots]
        self._setup_reboot(command, time_slots)  # Set up the script to start on reboot
        while True:
            current_time = datetime.now().time()
            if any(start <= current_time <= end for start, end in time_slots):
                self.run_command(command)
            time.sleep(60)  # Check every minute

    def run_command(self, command):
        process = subprocess.Popen(command, shell=True)
        while True:
            if process.poll() is not None:  # Process finished
                process = subprocess.Popen(command, shell=True)
            time.sleep(60)  # Check every minute

    def _parse_time(self, time_str):
        return datetime.strptime(time_str, "%H:%M:%S").time()

    def _setup_reboot(self, command, time_slots):
        # Create a systemd service file to run this script on reboot
        service_content = f"""
        [Unit]
        Description=DeployMaster Service
        After=network.target

        [Service]
        ExecStart=/usr/bin/python3 -c 'from daddy_ai.deploy_master import DeployMaster; setup = DeployMaster(); setup.deploy("{command}", {time_slots})'
        Restart=always
        User=root

        [Install]
        WantedBy=multi-user.target
        """
        with open('/etc/systemd/system/deploymaster.service', 'w') as service_file:
            service_file.write(service_content)

        os.system('systemctl daemon-reload')
        os.system('systemctl enable deploymaster.service')
        os.system('systemctl start deploymaster.service')
