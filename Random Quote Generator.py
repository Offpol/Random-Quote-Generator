import tkinter as tk
from tkinter import ttk, messagebox
import random
import json
import os

# --- Настройки ---
FILENAME = "quotes.json"
DEFAULT_QUOTES = [
    {"text": "Единственный способ делать великие дела — любить то, что ты делаешь.", "author": "Стив Джобс", "theme": "Мотивация"},
    {"text": "Величайшая слава не в том, чтобы никогда не ошибаться, а в том, чтобы уметь подняться каждый раз, когда падаешь.", "author": "Конфуций", "theme": "Жизнь"},
    {"text": "Знание — сила.", "author": "Фрэнсис Бэкон", "theme": "Образование"}
]

class QuoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор случайных цитат")
        self.root.geometry("600x500")
        
        self.quotes = DEFAULT_QUOTES.copy()
        self.history = []
        
        self.load_data()
        self.create_widgets()

    def create_widgets(self):
        # --- Фрейм для генерации ---
        frame_gen = tk.LabelFrame(self.root, text="Сгенерировать цитату")
        frame_gen.pack(pady=10, fill="x")

        self.quote_label = tk.Label(frame_gen, text="", wraplength=400, font=("Arial", 12))
        self.quote_label.pack(pady=5)

        self.author_label = tk.Label(frame_gen, text="", font=("Arial", 10, "italic"))
        self.author_label.pack(pady=5)

        btn_gen = tk.Button(frame_gen, text="Сгенерировать цитату", command=self.generate_quote)
        btn_gen.pack(pady=10)

        # --- Фрейм для добавления ---
        frame_add = tk.LabelFrame(self.root, text="Добавить свою цитату")
        frame_add.pack(pady=10, fill="x", padx=10)

        tk.Label(frame_add, text="Текст:").grid(row=0, column=0, sticky="w")
        self.entry_text = tk.Entry(frame_add, width=40)
        self.entry_text.grid(row=0, column=1, pady=5)

        tk.Label(frame_add, text="Автор:").grid(row=1, column=0, sticky="w")
        self.entry_author = tk.Entry(frame_add, width=40)
        self.entry_author.grid(row=1, column=1, pady=5)

        tk.Label(frame_add, text="Тема:").grid(row=2, column=0, sticky="w")
        self.entry_theme = ttk.Combobox(frame_add, values=["Мотивация", "Жизнь", "Образование", "Юмор"], width=37)
        self.entry_theme.grid(row=2, column=1, pady=5)
        self.entry_theme.set("Мотивация")

        btn_add = tk.Button(frame_add, text="Добавить", command=self.add_quote)
