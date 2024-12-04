import tkinter as tk
from tkinter import messagebox

def calcular_determinante():
    try:
        A = [
            [float(a11.get()), float(a12.get()), float(a13.get())],
            [float(a21.get()), float(a22.get()), float(a23.get())],
            [float(a31.get()), float(a32.get()), float(a33.get())],
        ]
        det = 1.0
        n = len(A)
        for i in range(n):
            if A[i][i] == 0:
                for j in range(i + 1, n):
                    if A[j][i] != 0:
                        A[i], A[j] = A[j], A[i]
                        det *= -1  
                        break
            
            # Pivô
            pivô = A[i][i]
            if pivô == 0:
                det = 0
                break
            
            det *= pivô
            for j in range(i, n):
                A[i][j] /= pivô
            
            for k in range(i + 1, n):
                fator = A[k][i]
                for j in range(i, n):
                    A[k][j] -= fator * A[i][j]
        resultado_label.config(text=f"Determinante: {det:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

janela = tk.Tk()
janela.title("Calculadora de Determinante por Escalonamento")
janela.geometry("450x450")
janela.resizable(False, False)

titulo_label = tk.Label(janela, text="Determinante de Matriz 3x3", font=("Arial", 16))
titulo_label.pack(pady=10)


instrucao_label = tk.Label(janela, text="Insira os valores da matriz:", font=("Arial", 12))
instrucao_label.pack(pady=5)


frame_matriz = tk.Frame(janela)
frame_matriz.pack(pady=10)

a11 = tk.Entry(frame_matriz, width=5, font=("Arial", 14)); a11.grid(row=0, column=0, padx=5, pady=5)
a12 = tk.Entry(frame_matriz, width=5, font=("Arial", 14)); a12.grid(row=0, column=1, padx=5, pady=5)
a13 = tk.Entry(frame_matriz, width=5, font=("Arial", 14)); a13.grid(row=0, column=2, padx=5, pady=5)

a21 = tk.Entry(frame_matriz, width=5, font=("Arial", 14)); a21.grid(row=1, column=0, padx=5, pady=5)
a22 = tk.Entry(frame_matriz, width=5, font=("Arial", 14)); a22.grid(row=1, column=1, padx=5, pady=5)
a23 = tk.Entry(frame_matriz, width=5, font=("Arial", 14)); a23.grid(row=1, column=2, padx=5, pady=5)

a31 = tk.Entry(frame_matriz, width=5, font=("Arial", 14)); a31.grid(row=2, column=0, padx=5, pady=5)
a32 = tk.Entry(frame_matriz, width=5, font=("Arial", 14)); a32.grid(row=2, column=1, padx=5, pady=5)
a33 = tk.Entry(frame_matriz, width=5, font=("Arial", 14)); a33.grid(row=2, column=2, padx=5, pady=5)


calcular_btn = tk.Button(janela, text="Calcular Determinante", command=calcular_determinante,
                         font=("Arial", 14), bg="#4CAF50", fg="white")
calcular_btn.pack(pady=20, ipadx=10, ipady=5)


resultado_label = tk.Label(janela, text="Determinante: ", font=("Arial", 14), fg="#333")
resultado_label.pack(pady=10)

janela.mainloop()
