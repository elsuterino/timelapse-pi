wget https://raw.githubusercontent.com/elsuterino/timelapse-pi/main/picture.py

sudo nano /etc/systemd/system/timelapse.service

```
[Unit]
Description=Python Timelapse Camera Script
After=network.target

[Service]
# Replace 'pi' with your username if different
User=pi
# The directory where your script lives
WorkingDirectory=/home/elsuterino/scripts
# The command to run your script
ExecStart=/usr/bin/python3 /home/elsuterino/scripts/take_photo.php
# Auto-restart if the script crashes
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

sudo systemctl daemon-reload

sudo systemctl enable timelapse.service

sudo systemctl start timelapse.service
