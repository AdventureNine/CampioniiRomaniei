import os

FRONTEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_asset_path(region, asset_type, filename):
    path = os.path.join(FRONTEND_DIR, 'regions', region, 'assets', asset_type, filename)
    return os.path.normpath(path)


def get_region_assets_base(region):
    path = os.path.join(FRONTEND_DIR, 'regions', region, 'assets')
    return os.path.normpath(path)

TRANSILVANIA_MAP = get_asset_path('transilvania', 'maps', 'transilvania.png')
TRANSILVANIA_MASCOT = get_asset_path('transilvania', 'mascots', 'geo_muntii.png')
TRANSILVANIA_PLAY_BUTTON = get_asset_path('transilvania', 'backgrounds', 'play.png')
