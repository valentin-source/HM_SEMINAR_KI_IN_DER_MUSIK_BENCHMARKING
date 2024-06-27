import tkinter as tk
from tkinter import filedialog, messagebox
import jiwer # paket zur Berechnung der WER
import re
import numpy as np # für berechnung der levenshtein Distanz

def calculate_wer(reference, hypothesis):
    return jiwer.wer(reference, hypothesis)
import numpy as np
# Funktion übernommen aus: https://thepythoncode.com/article/calculate-word-error-rate-in-python#how-wer-is-calculated
def calculate_lev(reference, hypothesis):
    ref_words = reference.split()
    hyp_words = hypothesis.split()
    d = np.zeros((len(ref_words) + 1, len(hyp_words) + 1))
    for i in range(len(ref_words) + 1):
        d[i, 0] = i
    for j in range(len(hyp_words) + 1):
        d[0, j] = j
    for i in range(1, len(ref_words) + 1):
        for j in range(1, len(hyp_words) + 1):
            if ref_words[i - 1] == hyp_words[j - 1]:
                d[i, j] = d[i - 1, j - 1]
            else:
                substitution = d[i - 1, j - 1] + 1
                insertion = d[i, j - 1] + 1
                deletion = d[i - 1, j] + 1
                d[i, j] = min(substitution, insertion, deletion)
    return d[len(ref_words), len(hyp_words)] / len(ref_words)

def load_file(text_widget):
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, content)
def replace_special_characters(text):
    return re.sub(r'[^A-Za-z0-9\s]', '-', text)
def remove_bracketed_text(text):
    cleaned_text = re.sub(r'\[.*?\]', '', text)
    return replace_special_characters(clean_text2(cleaned_text))
def clean_text2(text):
    cleaned_text = re.sub(r'"text" ?: ?"([^"]*)"', r'\1', text)
    return re.sub(r'\s+', ' ', cleaned_text).strip()
def compare_texts():
    reference = text_area1.get(1.0, tk.END).strip()
    hypothesis = text_area2.get(1.0, tk.END).strip()
    if not reference or not hypothesis:
        messagebox.showwarning("Input Error", "Both text fields must be filled.")
        return
    wer = calculate_wer(reference, hypothesis)
    lev = calculate_lev(reference, hypothesis)
    messagebox.showinfo("WER Result", f"Word Error Rate (WER): {wer:.2f}\nLevenshtein Distanz: {lev:.2f}")
def clean_text(text):
    cleaned_lines = [line.strip() for line in text.splitlines()]
    non_empty_lines = [line for line in cleaned_lines if line]
    cleaned_text = ' '.join(non_empty_lines) 
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text) 
    return remove_bracketed_text(cleaned_text)
def clean_text_fields():
    reference = text_area1.get(1.0, tk.END)
    hypothesis = text_area2.get(1.0, tk.END)
    cleaned_reference = clean_text(reference)
    cleaned_hypothesis = clean_text(hypothesis)
    text_area1.delete(1.0, tk.END)
    text_area1.insert(tk.END, cleaned_reference)
    text_area2.delete(1.0, tk.END)
    text_area2.insert(tk.END, cleaned_hypothesis)
    messagebox.showinfo("Info", "Text fields have been cleaned.")
root = tk.Tk()
root.title("Text Comparison Tool")
text_area1 = tk.Text(root, height=20, width=120)
text_area1.pack(padx=10, pady=10)
text_area2 = tk.Text(root, height=20, width=120)
text_area2.pack(padx=10, pady=10)
btn_load_file1 = tk.Button(root, text="Load File 1", command=lambda: load_file(text_area1))
btn_load_file1.pack(pady=5)
btn_load_file2 = tk.Button(root, text="Load File 2", command=lambda: load_file(text_area2))
btn_load_file2.pack(pady=5)
btn_clean_text = tk.Button(root, text="Clean Text Fields", command=clean_text_fields)
btn_clean_text.pack(pady=5)
btn_compare = tk.Button(root, text="Compare Texts", command=compare_texts)
btn_compare.pack(pady=10)
root.mainloop()
