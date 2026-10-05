import os

vps_data = {}
admin_data = {"admins": []}
CPU_THRESHOLD = 90
RAM_THRESHOLD = 90
resource_monitor_active = True
VPS_USER_ROLE_ID = int(os.getenv("VPS_USER_ROLE_ID", "0"))
DEFAULT_STORAGE_POOL = os.getenv("DEFAULT_STORAGE_POOL", "default")
