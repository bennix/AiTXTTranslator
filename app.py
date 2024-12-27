import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import re

# Initialize model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    'DRT-o1-7B',
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained('DRT-o1-7B')

def extract_output(text):
    # 提取所有<output>标签中的内容
    pattern = r'<output>(.*?)</output>'
    matches = re.findall(pattern, text, re.DOTALL)
    if matches:
        return '\n'.join(match.strip() for match in matches)
    return text

def translate_text(file, progress=gr.Progress()):
    # Read the content of the uploaded file
    content = file.name
    with open(content, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split content into sentences
    sentences = re.split('[.!?]+', content)
    sentences = [s.strip() for s in sentences if s.strip()]  # Remove empty sentences
    
    # Group sentences into pairs
    pairs = []
    for i in range(0, len(sentences), 2):
        if i + 1 < len(sentences):
            pair = sentences[i] + ". " + sentences[i + 1] + "."
        else:
            pair = sentences[i] + "."
        pairs.append(pair)
    
    # Translate each pair and collect results
    translations = []
    progress(0, desc="开始翻译...")
    for idx, pair in enumerate(pairs):
        progress((idx + 1) / len(pairs), desc=f"正在翻译第 {idx + 1}/{len(pairs)} 组句子")
        
        prompt = f"Please translate the following text from English to Chinese:\n{pair}"
        messages = [
            {"role": "system", "content": "You are a philosopher skilled in deep thinking, accustomed to exploring complex problems with profound insight."},
            {"role": "user", "content": prompt}
        ]
        
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
        
        generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=1024
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]
        
        response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        translations.append(extract_output(response))
    
    progress(1.0, desc="翻译完成！")
    # Combine all translations
    final_translation = "\n\n".join(translations)
    return final_translation

# Create Gradio interface
iface = gr.Interface(
    fn=translate_text,
    inputs=gr.File(file_types=[".txt"]),
    outputs="text",
    title="英文到中文翻译器",
    description="上传包含英文文本的TXT文件来获取中文翻译。"
)

if __name__ == "__main__":
    iface.launch()