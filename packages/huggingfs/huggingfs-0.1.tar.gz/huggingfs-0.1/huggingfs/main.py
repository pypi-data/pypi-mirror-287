"""
huggingfs.json := [{
  "path": "models",
  "options": [
    "nvidia/Minitron-4B-Base",
    "coqui/XTTS-v2",
    "KwaiVGI/LivePortrait",
    "BAAI/bge-m3",
    "vidore/colpali"
  ],
}]


huggingfs.json := [{
  "path": "app/models/Stable-diffusion",
  "options": [
    "nvidia/Minitron-4B-Base",
    "coqui/XTTS-v2",
    "KwaiVGI/LivePortrait",
    "BAAI/bge-m3",
    "vidore/colpali"
  ],
}, {
  "path": "app/models/Stable-diffusion",
  "allowed": ["input", "options"],
  "options": [
    "nvidia/Minitron-4B-Base",
    "coqui/XTTS-v2",
    "KwaiVGI/LivePortrait",
    "BAAI/bge-m3",
    "vidore/colpali"
  ],
  "path": "app/models/Lora",
  "options": []
}, {
  "path": "app/models/RealESRGAN",
  "options": []
}, {
  "path": "app/embeddings",
  "options": []
}, {
  "path": "app/models/ControlNet",
  "options": []
}]
"""
import gradio as gr
from huggingface_hub import snapshot_download
import os
import json
import argparse


css = """
.gradio-container { max-width: none !important; }
.title { padding: 10px; }
.gr-group { border-radius: 0 !important; }
th, tr, td { border-radius: 0 !important; }
.cell-wrap { border-radius: 0 !important; }
.table-wrap { border-radius: 0 !important; }
.invisible { display: none !important; }
"""
def download_model(local_dir):
    def fn(model_id, model_dropdown, progress=gr.Progress()):
        if len(model_id) > 0:
            id = model_id
        elif len(model_dropdown) > 0:
            id = model_dropdown
        model_dir = os.path.join(local_dir, "-".join(id.split("/")))
        try:
            snapshot_download(
                repo_id=id,
                local_dir=model_dir,
                tqdm_class=progress.tqdm
            )
            return downloaded(local_dir)()
        except Exception as e:
            return f"Error downloading model: {str(e)}"
    return fn
def downloaded(local_dir):
    def fn():
        items = os.listdir(local_dir)
        items = [[s] for s in items]
        return items
    return fn

def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    config = args.argument

    print(f"config={config}")


    base_dir = os.path.abspath(os.getcwd())
    items = []
    try:
        with open(config, 'r') as file:
            fs = json.load(file)
            items = fs["fs"]
    except Exception:
        print("can't find huggingfs.json")
    with gr.Blocks(css=css) as app:
        gr.HTML("<h1>HuggingFS</h1>")
        for item in items:
            choices = []
            try:
                choices = item['options']
            except Exception:
                print("options need to be an array")
            

            allowed = ["input", "options"]
            try:
                allowed = item['allowed']
            except Exception:
                print("no 'allowed' attribute")

            local_dir = os.path.join(base_dir, item['path'])
            os.makedirs(local_dir, exist_ok=True)
            #with gr.Group():
            with gr.Tab(item['path']):
                with gr.Group():
                    gr.HTML(f"<h2 class='title'>/{item['path']}</h2>")
                    with gr.Row():
                        if "input" in allowed:
                            model_input = gr.Textbox(label="Enter Hugging Face Model ID")
                        else:
                            model_input = gr.Textbox(label="Enter Hugging Face Model ID", elem_classes="invisible")
                        if len(choices) > 0:
                            model_dropdown = gr.Dropdown(label="Select from available options", choices=choices)
                        else:
                            model_dropdown = gr.Dropdown(label="Select from available options", choices=choices, elem_classes="invisible")
                        button = gr.Button("download")
                    with gr.Row():
                        dataFrame = gr.Dataframe(
                            downloaded(local_dir),
                            headers=["name"],
                            datatype=["str"],
                        )
                button.click(fn=download_model(local_dir), inputs=[model_input, model_dropdown], outputs=[dataFrame])
                button.click(fn=downloaded(local_dir), outputs=[dataFrame])

    app.launch()

if __name__ == "__main__":
    main()
