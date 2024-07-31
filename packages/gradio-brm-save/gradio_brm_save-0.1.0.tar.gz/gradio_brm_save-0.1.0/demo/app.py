
import gradio as gr
from gradio_brm_save import brm_save

with gr.Blocks() as demo:
    save = brm_save(visible=False)
    visible_btn = gr.Button('Visible')
    def update():
        return brm_save(fileName="test1.txt", fileContent="1234", visible=True)
    visible_btn.click(update, outputs=save)
    def changed(e):
        if e:
            print('Saved Successfully')
        else:
            print('Cancel')
        return brm_save(visible=False)
    save.submit(changed, inputs=save, outputs=save)


if __name__ == "__main__":
    demo.launch()
