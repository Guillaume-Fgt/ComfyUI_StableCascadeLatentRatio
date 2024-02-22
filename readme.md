A custom node to create empty latents for Stable Cascade. Compare to stable_cascade_empty_latent_node, it adds:

- purple background color at creation
- width and height incrementation of 64 by default
- possibility to lock the aspect ratio. Changing the width or the height will update the other dimension accordingly
- switch width/height at execution (not displayed in the node, this is a TODO)

To install, simply git clone the repo in /custom_nodes.
You will find the node under latent/Stable Cascade Latent Ratio
