wget https://raw.githubusercontent.com/elsuterino/timelapse-pi/main/picture.py

sudo nano /etc/systemd/system/timelapse.service

```
[Unit]
Description=Python Timelapse Camera Script
After=network.target

[Service]
User=elsuterino   
ExecStart=/usr/bin/python3 /home/elsuterino/picture.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

sudo systemctl daemon-reload

sudo systemctl enable timelapse.service

sudo systemctl start timelapse.service
