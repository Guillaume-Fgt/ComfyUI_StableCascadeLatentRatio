import torch
import nodes

RATIOS:tuple[str]=(
    "None",
    "1:1|Social apps",
    "4:3|Traditional television & computer monitor standard; classic 35 mm film standard",
    "14:9|Used as a middle ground between 4:3 and 16:9",
    "16:10|Mostly used for computer displays and tablet computers",
    "16:9|HD video standard; American & British digital broadcast TV standard",
    "1.85:1|35 mm American and British widescreen standard for theatrical film",
    "2.39:1|Current anamorphic widescreen theatrical viewings, commercials, and some music videos",
    "6:13|Commonly used in modern smartphones",
    "9:16|Commonly used in mid-late 2010s smartphones",
    "2:3|Commonly used in late 2000s smartphones",
    "5:4|Common in large and medium format photography",
    "3:1|Used for panorama photography"
)

class StableCascadeLatentRatio:
    def __init__(self, device="cpu"):
        self.device = device

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "width": ("INT", {"default": 1024, "min": 256, "max": nodes.MAX_RESOLUTION, "step": 64}),
            "height": ("INT", {"default": 1024, "min": 256, "max": nodes.MAX_RESOLUTION, "step": 64}),
            "compression": ("INT", {"default": 42, "min": 4, "max": 128, "step": 1}),
            "batch_size": ("INT", {"default": 1, "min": 1, "max": 4096}),
            "lock_aspect_ratio_to":(RATIOS,),
            "switch_width_height":("BOOLEAN", {"default": False}),
        }}
    RETURN_TYPES = ("LATENT", "LATENT")
    RETURN_NAMES = ("stage_c", "stage_b")
    FUNCTION = "generate"

    CATEGORY = "latent"

    def generate(self, width, height, compression, lock_aspect_ratio_to, switch_width_height, batch_size=1):
        if not switch_width_height:
            c_latent = torch.zeros([batch_size, 16, height // compression, width // compression])
            b_latent = torch.zeros([batch_size, 4, height // 4, width // 4])
        else:
            c_latent = torch.zeros([batch_size, 16, width // compression, height // compression])
            b_latent = torch.zeros([batch_size, 4, width // 4, height // 4])
        return ({
            "samples": c_latent,
        }, {
            "samples": b_latent,
        })





