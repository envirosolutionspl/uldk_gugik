import os
import sys
import importlib

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PLUGIN_DIR = os.path.dirname(TEST_DIR)
PARENT_DIR = os.path.dirname(PLUGIN_DIR)
PLUGIN_NAME = os.path.basename(PLUGIN_DIR)
DATA_DIR = os.path.join(TEST_DIR, 'data')

if PARENT_DIR not in sys.path:
    sys.path.insert(0, PARENT_DIR)
if TEST_DIR not in sys.path:
    sys.path.insert(0, TEST_DIR)

for name in ['constants', 'https_adapter', 'request', 'request_search',
              'request_region', 'uldk', 'uldk_teryt', 'uldk_gugik_dialog',
              'uldk_xy', 'uldk_api', 'uldk_parcel']:
    try:
        sys.modules[name] = importlib.import_module(f"{PLUGIN_NAME}.{name}")
    except Exception:
        pass
