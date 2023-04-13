import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]
messages = [
    {"role": "system", "content": "You are an AI specialized about block chain and cryptos. Do not answer anything other than related queries."},
]
def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=4, label="Ask me anything about Block Chain and Cryptos,will try answering them")
outputs = gr.outputs.Textbox(label="CryptoBot's Gyan")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="CryptoChatBot",
             description="Ask me anything about Block Chain & Cryptos",
             theme="compact").launch(share=True)
