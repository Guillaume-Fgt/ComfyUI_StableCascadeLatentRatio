import { app } from "../../scripts/app.js";


app.registerExtension({
    name: "Comfy.StableCascadeLatentRatio",

    nodeCreated(node, app) {
        if (node.comfyClass == "StableCascadeLatentRatio") {
            node.bgcolor = "#535";
            node.color = "#323";

            let width = node.widgets.find(obj => obj.name === "width");
            let height = node.widgets.find(obj => obj.name === "height");
            let ratio = node.widgets.find(obj => obj.name === "lock_aspect_ratio_to");


            ratio.callback = function () {
                if (ratio.value == "None") {
                    return
                }
                let splitted_str = ratio.value.split(/[:|]+/);
                let ratio_val = splitted_str[0] / splitted_str[1];
                height.value = Math.floor((width.value / ratio_val) / 64) * 64;
            };

            width.callback = function () {
                if (ratio.value == "None") {
                    return
                }
                let splitted_str = ratio.value.split(/[:|]+/);
                let ratio_val = splitted_str[0] / splitted_str[1];
                height.value = Math.floor((width.value / ratio_val) / 64) * 64;
            };

            height.callback = function () {
                if (ratio.value == "None") {
                    return
                }
                let splitted_str = ratio.value.split(/[:|]+/);
                let ratio_val = splitted_str[0] / splitted_str[1];
                width.value = Math.floor((height.value * ratio_val) / 64) * 64;
            };
        }
    }
})