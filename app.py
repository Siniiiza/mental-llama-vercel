import os
import openai
import gradio as gr

openai.api_key = os.environ.get("OPENAI_API_KEY")

system_prompt = """
Ты — MentaLLama: психологический AI-помощник проекта InsideTennis [Mental Notes].

Говори мягко, поддерживающе, в стиле психотерапевта и ментального тренера по теннису.
Не давай сухих ответов. Используй метафоры, сравнения, говори от души.
Вдохновляй родителей понять чувства ребёнка и направить его без давления.
"""

def ask_llama(user_input):
    if not user_input.strip():
        return "Пожалуйста, напишите, что вас беспокоит..."
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
          )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Ошибка: {str(e)}"

ui = gr.Interface(
    fn=ask_llama,
    inputs=gr.Textbox(lines=4, placeholder="Спросите о поведении, страхах, эмоциях..."),
    outputs="text",
    title="🦙 MentaLLama — психолог для теннисных родителей",
    description="Помогает понять чувства ребёнка через стиль Mental Notes.",
    theme="soft",
)

ui.launch()
