import tkinter as tk
from tkinter import messagebox

def formatar_matriz(A):
   
    return "\n".join(["\t".join([f"{elem:.2f}" for elem in linha]) for linha in A])

def calcular_determinante():
    try:
       
        A = [
            [float(a11.get()), float(a12.get()), float(a13.get())],
            [float(a21.get()), float(a22.get()), float(a23.get())],
            [float(a31.get()), float(a32.get()), float(a33.get())],
        ]

        det = 1.0
        passos_text.delete(1.0, tk.END)  #
        passos_text.insert(tk.END, "Matriz inicial:\n")
        passos_text.insert(tk.END, formatar_matriz(A) + "\n\n")
        
        n = len(A)
        for i in range(n):
            if A[i][i] == 0:
                for j in range(i + 1, n):
                    if A[j][i] != 0:
                        A[i], A[j] = A[j], A[i]
                        det *= -1  
                        passos_text.insert(tk.END, f"Troca de linhas {i+1} e {j+1}:\n")
                        passos_text.insert(tk.END, formatar_matriz(A) + "\n\n")
                        break
            
            # Pivô
            pivô = A[i][i]
            if pivô == 0:
                det = 0
                passos_text.insert(tk.END, "Pivô zero encontrado. Determinante: 0\n")
                break
            
            det *= pivô
            for j in range(i, n):
                A[i][j] /= pivô
            
            passos_text.insert(tk.END, f"Normalização da linha {i+1} pelo pivô {pivô:.2f}:\n")
            passos_text.insert(tk.END, formatar_matriz(A) + "\n\n")
            
            for k in range(i + 1, n):
                fator = A[k][i]
                for j in range(i, n):
                    A[k][j] -= fator * A[i][j]
                
                passos_text.insert(tk.END, f"Zerando elemento ({k+1}, {i+1}) com fator {fator:.2f}:\n")
                passos_text.insert(tk.END, formatar_matriz(A) + "\n\n")
        resultado_label.config(text=f"Determinante: {det:.2f}")

        passos_text.insert(tk.END, f"Determinante final: {det:.2f}\n")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

janela = tk.Tk()
janela.title("Calculadora de Determinante por Escalonamento")
janela.geometry("600x600")
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


passos_text = tk.Text(janela, height=15, width=60, font=("Courier", 10))
passos_text.pack(pady=10)


janela.mainloop()
