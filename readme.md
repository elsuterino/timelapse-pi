wget https://raw.githubusercontent.com/elsuterino/timelapse-pi/main/picture.py

mkdir -p ~/.config/systemd/user/

nano ~/.config/systemd/user/timelapse.service

```
[Unit]
Description=Python Timelapse Camera Script
After=network.target

[Service]
WorkingDirectory=/home/elsuterino
ExecStart=/usr/bin/python3 /home/elsuterino/picture.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

systemctl --user daemon-reload
systemctl --user enable timelapse.service
systemctl --user start timelapse.service
