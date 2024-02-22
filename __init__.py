from .stablecascadelatentratio import StableCascadeLatentRatio


NODE_CLASS_MAPPINGS = {
    "StableCascadeLatentRatio": StableCascadeLatentRatio,
}

NODE_DISPLAY_NAME_MAPPINGS = { "StableCascadeLatentRatio": "Stable Cascade Latent Ratio" }
WEB_DIRECTORY = "./js"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS','WEB_DIRECTORY'] 