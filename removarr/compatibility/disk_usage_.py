import shutil

# Always running on Python >= 3, so shutil.disk_usage is available
SUPPORT_SHUTIL = True

def disk_usage_(path):
    du = shutil.disk_usage(path)
    return {
        'total': du.total,
        'used': du.used,
        'free': du.free,
    }
