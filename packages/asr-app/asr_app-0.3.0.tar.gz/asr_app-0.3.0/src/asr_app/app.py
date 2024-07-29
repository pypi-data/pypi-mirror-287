from pathlib import Path
from typing import Union

import gradio as gr
import pandas as pd
import whisper
from whisper import Whisper

import asr_app.texts as t
from asr_app.io import browse_audio_files_str, browse_dir
from asr_app.progress import ProgressListener, progress_listener_handle
from asr_app.settings import settings

model: Union[Whisper | None] = None


def load_model(model_name: str, model_name_loaded: str, progress=gr.Progress()) -> tuple[str, str]:
    global model

    if model_name != model_name_loaded:
        progress((0, None), t.loading_model, unit="Ładowanie modelu")
        model = whisper.load_model(model_name)
        progress(None)

    return model_name, f"#### {t.loaded_model} {model_name}"


def on_transcribe(files_paths: str, save_dir: str, progress=gr.Progress()):
    files_paths = [Path(path) for path in files_paths.split('\n')]

    class FileProgressListener(ProgressListener):
        def __init__(self, file_path: Path):
            self.progress_description = f"{t.processing_file} {file_path}"
            self.finished_message = f"{t.processing_file_ended} {file_path}"

        def on_progress(self, current: Union[int, float], total: Union[int, float]):
            progress(progress=(current, total), desc=self.progress_description)

        def on_finished(self):
            gr.Info(message=self.finished_message)

    results = []
    for path in files_paths:

        if not path.exists():
            results.append((str(path), t.file_not_exist))
            continue

        listener = FileProgressListener(file_path=path)
        with progress_listener_handle(listener):
            try:
                result = model.transcribe(str(path), verbose=False, language="pl")
            except Exception as e:
                results.append((str(path), t.processing_file_error))
                continue
        try:
            save_path = get_save_path(save_dir, path)
            save_path.write_text(result["text"], encoding='utf-8')
        except Exception as e:
            results.append((str(path), t.saving_file_error))
            continue

        results.append((str(path), str(save_path)))

    df = pd.DataFrame(results, columns=t.results_table_header)
    return df


def get_save_path(save_dir: str, file_path: Path) -> Path:
    if save_dir and Path(save_dir).is_dir():
        save_dir = Path(save_dir)
    else:
        save_dir = file_path.parent

    return (save_dir / file_path.name).with_suffix(".txt")


def change_describe_button(text: str) -> gr.Button:
    if text.strip() == '':
        return gr.Button(value=t.transcribe_btn, variant="primary", min_width=1, interactive=False)
    else:
        return gr.Button(value=t.transcribe_btn, variant="primary", min_width=1, interactive=True)


with gr.Blocks(title=t.title) as demo:
    model_name_loaded_state = gr.State('')

    with gr.Row():
        with gr.Column(scale=2):
            menu_header = gr.Markdown(t.menu_header)

            with gr.Accordion(label=t.files_label, open=True):
                input_paths = gr.Markdown()
                browse_button = gr.Button(
                    value=t.browse_files_btn,
                    variant="secondary",
                )
                browse_button.click(
                    browse_audio_files_str,
                    outputs=input_paths,
                    show_progress="hidden",
                )

            with gr.Accordion(label=t.dir_label, open=True):
                output_dir = gr.Markdown()
                browse_button_dir = gr.Button(
                    value=t.browse_dir_btn,
                    variant="secondary",
                )
                browse_button_dir.click(
                    browse_dir,
                    outputs=output_dir,
                    show_progress="hidden",
                )

            model_dropdown = gr.Dropdown(
                label=t.model_dropdown_label,
                choices=settings.whisper_models_names,
                value=settings.whisper_default_model,
            )
            model_info = gr.Markdown()
            transcribe_button = gr.Button(
                value=t.transcribe_btn,
                variant="primary",
                min_width=1,
                interactive=False
            )

            input_paths.change(change_describe_button,
                               inputs=input_paths,
                               outputs=transcribe_button)

        with gr.Column(scale=5):
            header = gr.Markdown(t.results_header)
            output_values = gr.DataFrame(
                headers=t.results_table_header,
                col_count=(2, "fixed"),
                type="pandas",
                interactive=False,
            )
            file_content = gr.Markdown()


    def on_select(value: pd.DataFrame, evt: gr.SelectData):
        path = Path(value.iat[evt.index[0], 1])

        if path.is_file():
            text = path.read_text(encoding='utf-8')
        else:
            text = t.file_not_exist

        return text

    output_values.select(on_select, output_values, file_content)

    transcribe_button.click(
        load_model,
        inputs=[model_dropdown, model_name_loaded_state],
        outputs=[model_name_loaded_state, model_info],
    ).then(
        on_transcribe,
        inputs=[input_paths, output_dir],
        outputs=output_values,
    )


def main():
    demo.queue().launch()


if __name__ == '__main__':
    main()
