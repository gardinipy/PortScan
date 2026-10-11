# 🚀 Python Port Scanner

Um scanner de portas TCP rápido, leve e eficiente desenvolvido em Python. Diferente de scanners sequenciais padrão, este script utiliza **multithreading** para verificar múltiplas portas simultaneamente, reduzindo drasticamente o tempo de varredura.

## ✨ Funcionalidades

- **Alta Velocidade:** Utiliza `ThreadPoolExecutor` para escanear até 50 portas ao mesmo tempo.
- **Interface de Linha de Comando (CLI):** Desenvolvido com `argparse` para uma experiência de usuário intuitiva.
- **Segurança de Memória:** Implementado com Context Managers (`with`) para garantir o fechamento adequado de conexões e evitar vazamento de recursos.
- **Zero Dependências:** Construído inteiramente com a biblioteca padrão do Python. Nenhuma instalação do `pip` é necessária.

## ⚙️ Pré-requisitos

- Python 3.6 ou superior.

## 🚀 Como usar

Baixe ou clone o script para a sua máquina e execute-o via terminal.

### Verificação Básica (Portas Padrão)
Se você não especificar as portas, o script verificará automaticamente uma lista das portas mais comuns (21, 22, 23, 25, 80, 443, 8080, 8443, 3306, 139, 135).
