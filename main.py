from colorama import init, Fore, Style
import matplotlib.pyplot as plt

# Inicializa o colorama (necessário para funcionar em Windows)
init(autoreset=True)

# Lista de alunos em recuperação
recuperacao = [
    "ANA JULIA LIBORIO SOUZA",
    "BEATRIZ VICTORIA CARIAS DA SILVA",
    "CAIO VICTOR DA COSTA SANTOS",
    "GABRIEL ALVES MENDES DA SILVA",
    "GUILHERME DOS SANTOS DA SILVA",
    "ISABELLY APARECIDA DA SILVA",
    "KAUAN REGIS DOS SANTOS NASCIMENTO",
    "MIGUEL FERNANDES OLIVEIRA",
    "MURILO MATIAS DOS SANTOS",
    "ANA GABRIELE DA SILVA NEIVA DE LIMA",
    "BIANCA FERREIRA DOS SANTOS",
    "CLAUDIO DIAS DE OLIVEIRA JUNIOR",
    "DAVID LUIS OLIVEIRA DE BARROS",
    "DOUGLAS DE MORAES LOPES DA SILVA",
    "ELAINE ROCHA COSTA",
    "EMILLY ARAUJO SANTOS",
    "GABRIEL RICARDO GONCALVES DA SILVA",
    "KELVIN XAVIER DE SOUZA",
    "LUCAS DE SOUZA GONCALVES",
    "FLAVIA EDUARDA DE OLIVEIRA SANTOS",
]
import matplotlib.pyplot as plt
from colorama import Fore, Style
from unidecode import unidecode  # Biblioteca para lidar com acentos

# Funcoa para validar o nome do aluno
def validar_nome(nome):
    nome_formatado = unidecode(nome.strip().upper())  # Remove acentos e padroniza
    if not nome_formatado.replace(" ", "").isalpha():  # Verifica se contem apenas letras e espacos
        print(f"{Fore.RED}Nome invalido! Por favor, insira um nome valido.{Style.RESET_ALL}")
        return None
    return nome_formatado

# Funcao para solicitar as notas
def solicitar_notas():
    """Solicita as notas do aluno e retorna uma lista de valores validos."""
    notas = []
    for i in range(1, 6):  # 5 bimestres definidos
        while True:
            try:
                nota = float(input(f"{Fore.YELLOW}Digite a nota do {i}º bimestre (0 a 10): {Style.RESET_ALL}"))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print(f"{Fore.RED}A nota deve ser um numero entre 0 e 10.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Entrada invalida. Digite um numero.{Style.RESET_ALL}")
    return notas

# Funcao para calcular soma e media das notas
def calcular_media(notas):
    """Calcula e retorna a soma e a media das notas."""
    soma = sum(notas)
    media = soma / len(notas)
    return soma, media

# Funcao para exibir graficos das notas
def exibir_grafico(notas):
    """Exibe um grafico das notas de cada bimestre."""
    bimestres = [f'{i+1}º' for i in range(len(notas))]
    plt.bar(bimestres, notas, color='skyblue')
    plt.xlabel('Bimestres')
    plt.ylabel('Notas')
    plt.title('Desempenho Bimestral do Aluno')
    plt.ylim(0, 10)
    plt.show()

# Funcao para exibir o resultado
def exibir_resultado(nome, soma, media, notas):
    """Exibe o resultado do aluno com base nas notas."""
    print(f"\n{Fore.CYAN}Soma das notas: {soma:.2f}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Media: {media:.2f}{Style.RESET_ALL}")

    # Feedback visual com emojis e icones
    if media >= 6:
        print(f"{Fore.GREEN}✔️ Parabens, o aluno esta aprovado! 🎉{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}❌ Infelizmente, o aluno esta reprovado. 😔{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Dica: Revise os conteudos dos bimestres para melhorar!{Style.RESET_ALL}")

    # Exibindo grafico das notas
    exibir_grafico(notas)

# Funcao principal
def verificar_aprovacao():
    """Funcao principal do programa."""
    print(f"{Fore.BLUE}Bem-vindo ao sistema de avaliacao escolar!{Style.RESET_ALL}")
    nome = input(f"{Fore.YELLOW}Digite o nome completo do aluno: {Style.RESET_ALL}")
    nome_formatado = validar_nome(nome)

    if nome_formatado is None:
        return

    # Solicitar as notas e calcular a media
    notas = solicitar_notas()
    soma, media = calcular_media(notas)

    # Exibir resultado
    exibir_resultado(nome_formatado, soma, media, notas)

    # Perguntar se deseja revisar as notas
    revisar = input(f"{Fore.YELLOW}Deseja revisar as notas? (s/n): {Style.RESET_ALL}").strip().lower()
    if revisar == 's':
        notas = revisar_notas(notas)
        soma, media = calcular_media(notas)
        exibir_resultado(nome_formatado, soma, media, notas)

    print(f"{Fore.BLUE}Obrigado por usar o sistema de avaliacao escolar!{Style.RESET_ALL}")

if __name__ == "__main__":
    verificar_aprovacao()
