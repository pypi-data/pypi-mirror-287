"""
Tutor plugin to enable horizontal pod autoscaling in K8s environments.
"""
from glob import glob
import os

import importlib_resources
from tutor import hooks

from .__about__ import __version__


# Configuration
CMS_MEMORY_REQUEST_MB = 768
CMS_WORKER_MEMORY_REQUEST_MB = 1024
LMS_MEMORY_REQUEST_MB = 768
LMS_WORKER_MEMORY_REQUEST_MB = 1024

config = {
    # Add here your new settings
    "defaults": {
        "CMS_MEMORY_REQUEST": f"{CMS_MEMORY_REQUEST_MB}Mi",
        "LMS_MEMORY_REQUEST": f"{LMS_MEMORY_REQUEST_MB}Mi",

        # Kubernetes autoscaling settings
        "CMS_AUTOSCALING": True,
        "CMS_AVG_CPU": 75,
        "CMS_AVG_MEMORY": "",
        "CMS_CPU_LIMIT": 2,
        "CMS_CPU_REQUEST": 0.1,
        "CMS_MAX_REPLICAS": 2,
        "CMS_MEMORY_LIMIT": f"{round(CMS_MEMORY_REQUEST_MB * 1.35)}Mi",
        "CMS_MIN_REPLICAS": 1,

        "CMS_WORKER_AUTOSCALING": True,
        "CMS_WORKER_AVG_CPU": 80,
        "CMS_WORKER_AVG_MEMORY": "",  # Disable memory-based autoscaling
        "CMS_WORKER_CPU_LIMIT": 2.5,
        "CMS_WORKER_CPU_REQUEST": 0.1,
        "CMS_WORKER_MAX_REPLICAS": 4,
        "CMS_WORKER_MEMORY_LIMIT": f"{round(CMS_WORKER_MEMORY_REQUEST_MB * 1.35)}Mi",
        "CMS_WORKER_MEMORY_REQUEST": f"{CMS_WORKER_MEMORY_REQUEST_MB}Mi",
        "CMS_WORKER_MIN_REPLICAS": 1,

        "LMS_AUTOSCALING": True,
        "LMS_AVG_CPU": 75,
        "LMS_AVG_MEMORY": "",
        "LMS_CPU_LIMIT": 2,
        "LMS_CPU_REQUEST": 0.1,
        "LMS_MAX_REPLICAS": 2,
        "LMS_MEMORY_LIMIT": f"{round(LMS_MEMORY_REQUEST_MB * 1.35)}Mi",
        "LMS_MIN_REPLICAS": 1,

        "LMS_WORKER_AUTOSCALING": True,
        "LMS_WORKER_AVG_CPU": 80,
        "LMS_WORKER_AVG_MEMORY": "",  # Disable memory-based autoscaling
        "LMS_WORKER_CPU_LIMIT": 2,
        "LMS_WORKER_CPU_REQUEST": 0.1,
        "LMS_WORKER_MAX_REPLICAS": 4,
        "LMS_WORKER_MEMORY_LIMIT": f"{round(LMS_WORKER_MEMORY_REQUEST_MB * 1.35)}Mi",
        "LMS_WORKER_MEMORY_REQUEST": f"{LMS_WORKER_MEMORY_REQUEST_MB}Mi",
        "LMS_WORKER_MIN_REPLICAS": 1,
    },
}

# Load all configuration entries
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        (f"HPA_{key}", value)
        for key, value in config["defaults"].items()
    ]
)

hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        ("HPA_VERSION", __version__),
    ]
)

# Add the "templates" folder as a template root
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    str(importlib_resources.files("tutorhpa") / "templates")
)

hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("hpa/build", "plugins"),
        ("hpa/apps", "plugins"),
        ("hpa/k8s", "plugins"),
    ],
)


# Load patches from files
for path in glob(str(importlib_resources.files("tutorhpa") / "patches" / "*")):
    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))
