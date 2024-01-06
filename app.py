import gradio as gr
from rembg import remove

title = "Remove Background"
description = """
In this space, you can quickly remove background from images.

⚠️ Make sure your image is of good quality and has a clear background!

⚠️ Sometimes the background is not removed correctly, this is normal, because this is just a demo version!
"""

def segment(image):
     return remove(image)
     
demo = gr.Interface(fn=segment, inputs = gr.Image(label="Input Image", interactive=True), outputs = gr.Image(label="Result Image"), title=title, description=description)
demo.launch(show_api=False)