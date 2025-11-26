import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("미니계산기")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # 계산식을 저장할 변수
        self.expression = ""
        
        # GUI 생성
        self.create_widgets()
    
    def create_widgets(self):
        # 디스플레이 프레임
        display_frame = tk.Frame(self.root, bg="#f0f0f0", height=100)
        display_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        display_frame.pack_propagate(False)
        
        # 디스플레이 라벨
        self.display = tk.Label(
            display_frame,
            text="0",
            font=("Arial", 40, "bold"),
            bg="#f0f0f0",
            fg="#333333",
            justify=tk.RIGHT,
            anchor=tk.E
        )
        self.display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 버튼 프레임
        button_frame = tk.Frame(self.root, bg="#ffffff")
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 버튼 레이아웃
        buttons = [
            ['C', '(', ')', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '←']
        ]
        
        # 버튼 생성
        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                self.create_button(button_frame, btn_text, row_idx, col_idx)
    
    def create_button(self, frame, text, row, col):
        # 버튼 스타일 설정
        if text in ['=']:
            bg_color = "#4CAF50"
            fg_color = "white"
            font_style = ("Arial", 18, "bold")
        elif text in ['C', '←']:
            bg_color = "#f44336"
            fg_color = "white"
            font_style = ("Arial", 18, "bold")
        elif text in ['÷', '×', '-', '+']:
            bg_color = "#FF9800"
            fg_color = "white"
            font_style = ("Arial", 18, "bold")
        else:
            bg_color = "#e0e0e0"
            fg_color = "#333333"
            font_style = ("Arial", 18)
        
        button = tk.Button(
            frame,
            text=text,
            font=font_style,
            bg=bg_color,
            fg=fg_color,
            border=0,
            activebackground="#CCCCCC",
            activeforeground="#333333",
            command=lambda: self.on_button_click(text)
        )
        
        button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        
        # 그리드 가중치 설정 (균등하게 분배)
        frame.grid_rowconfigure(row, weight=1)
        frame.grid_columnconfigure(col, weight=1)
    
    def on_button_click(self, char):
        if char == 'C':
            # 초기화
            self.expression = ""
            self.update_display("0")
        
        elif char == '←':
            # 한 글자 삭제
            self.expression = self.expression[:-1]
            self.update_display(self.expression if self.expression else "0")
        
        elif char == '=':
            # 계산 실행
            try:
                # ÷, × 기호를 파이썬 연산자로 변환
                calc_expression = self.expression.replace('÷', '/').replace('×', '*')
                result = eval(calc_expression)
                
                # 소수점 정리
                if isinstance(result, float):
                    if result == int(result):
                        result = int(result)
                
                self.expression = str(result)
                self.update_display(result)
            except:
                self.update_display("오류")
                self.expression = ""
        
        else:
            # 숫자 및 연산자 입력
            self.expression += char
            self.update_display(self.expression)
    
    def update_display(self, value):
        self.display.config(text=str(value))


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
