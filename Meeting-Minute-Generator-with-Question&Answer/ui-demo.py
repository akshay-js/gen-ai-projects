import gradio as gr
from transformers import pipeline
import torchaudio
import time

# Load Whisper ASR model
transcriber = pipeline(model="openai/whisper-base")

# Load summarization model
summarization_model = pipeline("summarization")

# Load question-answering model
model_name = "deepset/roberta-base-squad2"
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

def translate_audio(audio):
    # Step 1: Transcribe audio to text
    transcription = transcriber(audio)
    print('transcription', transcription)

    # Step 2: Translate text to Hindi
    summary = summarization_model(transcription['text'])
    print('summary', summary)

    return transcription['text'], summary[0]['summary_text']

def answer_question(context, question):
    QA_input = {
        'question': question,
        'context': context
    }
    print('----QA_input----', QA_input)
    return nlp(QA_input)['answer']

# Create Gradio interface
with gr.Blocks() as iface:
    gr.Markdown("# Audio Translator, Summarizer, and QA System")

    with gr.Row():
        audio_input = gr.Audio(type="filepath", label="Upload Audio")
        transcription_output = gr.Textbox(
            label="Transcribed Text", 
            info="Initial text")
        translation_output = gr.Textbox(
            label="Summary", 
            info="Meeting minute")

    translate_button = gr.Button("Translate Audio")

    translate_button.click(
        translate_audio,
        inputs=[audio_input],
        outputs=[transcription_output, translation_output]
    )

    def respond(message, chat_history, context):
      bot_message = answer_question(context, message)
      print('----bot_message---', bot_message)
      chat_history.append((message, bot_message))
      time.sleep(2)
      return "", chat_history

    with gr.Blocks() as demo:
      chatbot = gr.Chatbot()
      msg = gr.Textbox()
      clear = gr.ClearButton([msg, chatbot])

      msg.submit(respond, [msg, chatbot, transcription_output], [msg, chatbot])

# Launch the app
iface.launch(share=True)  # 'share=True' to get a public link 