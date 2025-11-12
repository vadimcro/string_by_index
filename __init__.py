# Import the mappings from your node file
from .StringByIndex import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# This tells ComfyUI's loader that these are the mappings from this directory.
# If you add more node files, you'll merge their mappings here.
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']