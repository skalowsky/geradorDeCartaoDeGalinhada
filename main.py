from PIL import Image, ImageDraw, ImageFont

A4 = (595, 842)
NUM_CARTAO_FOLHA = 5

CARTAO = (A4[0], A4[1] // NUM_CARTAO_FOLHA)

DIST_ENTRE_LIN = 5

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)



def criarFolhaA4() -> Image:
  return Image.new('RGB', A4, BRANCO)



def redimencionarLogo(logo: Image, porcentagem: float) -> Image:
  hpercent = (porcentagem / float(logo.size[1]))
  wsize = int((float(logo.size[0]) * float(hpercent)))
  return logo.resize((wsize, porcentagem), Image.ANTIALIAS)



def criarLinhas(cartao: Image) -> Image:
  cartaoComLinha = ImageDraw.Draw(cartao)
  #Criar linha de cima
  cartaoComLinha.line((DIST_ENTRE_LIN ,DIST_ENTRE_LIN, cartao.size[0] - DIST_ENTRE_LIN, DIST_ENTRE_LIN), PRETO)

  #Criar linha de baixo
  #cartaoComLinha.line((DIST_ENTRE_LIN , cartao.size[1] - DIST_ENTRE_LIN, cartao.size[0] - DIST_ENTRE_LIN, cartao.size[1] - DIST_ENTRE_LIN), fill = 128)
  
  #Criar linha pontilhada do meio
  for y in range(0, cartao.size[1], 4): #bug da linha pontilhada bem em cima
    cartaoComLinha.line([(cartao.size[0] / 2, y), (cartao.size[0] / 2, y + 2)], PRETO)

  del cartaoComLinha



def criarDescricoesEsquerda(cartao: Image, numero: int, data: str, valor: str, nome: str, endereco: str, cidade: str) -> Image:
  fonteNumero = ImageFont.truetype("fonte/Arimo-Regular.ttf", 20)
  fonteTitulo = ImageFont.truetype("fonte/Arimo-Bold.ttf", 16)
  fonteDescricao = ImageFont.truetype("fonte/Arimo-Regular.ttf", 11)
 
  escrita = ImageDraw.Draw(cartao)

  #Escreve o numero
  escrita.text((CARTAO[0] * 0.22, CARTAO[1] * 0.1),"Nº " + str(numero).zfill(3), PRETO, font = fonteNumero)

  #Escreve 'Cartão de Galinhada' e sublinha
  escrita.text((CARTAO[0] * 0.12, CARTAO[1] * 0.25),"CARTÃO DE GALINHADA" , PRETO, font = fonteTitulo)
  escrita.line((CARTAO[0] * 0.12, CARTAO[1] * 0.35, CARTAO[0] * 0.46, CARTAO[1] * 0.35), PRETO , width = 2)

  #Escreve a data do evento
  escrita.text((CARTAO[0] * 0.10, CARTAO[1] * 0.43),"Data: " + data + " (Sábado ao meio dia)", PRETO, font = fonteDescricao)

  #Escreve o valor de cada cartão
  escrita.text((CARTAO[0] * 0.15, CARTAO[1] * 0.55),"Valor: R$ " + valor, PRETO, font = fonteDescricao)

  #Escreve o nome da sede
  escrita.text((CARTAO[0] * 0.05, CARTAO[1] * 0.67),"Local: " + nome, PRETO, font = fonteDescricao)

  #Escreve o rua e o numero
  escrita.text((CARTAO[0] * 0.12, CARTAO[1] * 0.79), endereco, PRETO, font = fonteDescricao)

  #Escreve o nome da cidade e o estado
  escrita.text((CARTAO[0] * 0.18, CARTAO[1] * 0.91), cidade, PRETO, font = fonteDescricao)

  return cartao



def criarDescricoesDireita(cartao: Image, numero: int, premio: str, descricaoNoFeminino: bool) -> Image:
  fonteNumero = ImageFont.truetype("fonte/Arimo-Regular.ttf", 20)
  fonteDescricao = ImageFont.truetype("fonte/Arimo-Bold.ttf", 10)
  fontePreencher = ImageFont.truetype("fonte/Arimo-Regular.ttf", 14)

  escrita = ImageDraw.Draw(cartao)

  #Escreve descrição padrão
  escrita.text((CARTAO[0] * 0.55, CARTAO[1] * 0.1), "PREENCHA E CONCORRA A DOIS SORTEIOS", PRETO, font = fonteDescricao)
  escrita.text((CARTAO[0] * 0.65, CARTAO[1] * 0.2), "NO DIA DA GALINHADA", PRETO, font = fonteDescricao)

  #Escreve o premio
  escrita.text((CARTAO[0] * 0.52, CARTAO[1] * 0.35), premio, PRETO, font = fonteDescricao)
  if descricaoNoFeminino:
    escrita.text((CARTAO[0] * 0.65, CARTAO[1] * 0.45), "(UMA POR CARTÃO)", PRETO, font = fonteDescricao)
  else:
    escrita.text((CARTAO[0] * 0.65, CARTAO[1] * 0.45), "(UM POR CARTÃO)", PRETO, font = fonteDescricao)

  #Escreve o nome
  escrita.text((CARTAO[0] * 0.52, CARTAO[1] * 0.6), "Nome: ", PRETO, font = fontePreencher)
  escrita.line((CARTAO[0] * 0.59, CARTAO[1] * 0.68, CARTAO[0] * 0.95, CARTAO[1] * 0.68), PRETO , width = 1) 

  #Escreve o telefone
  escrita.text((CARTAO[0] * 0.52, CARTAO[1] * 0.72), "Telefone: ", PRETO, font = fontePreencher)
  escrita.line((CARTAO[0] * 0.625, CARTAO[1] * 0.8, CARTAO[0] * 0.95, CARTAO[1] * 0.8), PRETO , width = 1) 

  #Escreve o numero
  escrita.text((CARTAO[0] * 0.7, CARTAO[1] * 0.85),"Nº " + str(numero).zfill(3), PRETO, font = fonteNumero)

  return cartao



def criarCartao(dimensao, logo: Image, numero: int) -> Image:

  cartao = Image.new('RGB', dimensao, BRANCO)
  logo = redimencionarLogo(logo, 60)
  criarLinhas(cartao)

  criarDescricoesEsquerda(
    cartao, 
    numero,
    "01/01/2020",
    "10,00 (dez reais)",
    "Associação dos Moradores do Bairro Aviação",
    "Rua Treze de Maio, 160 - B. Aviação",
    "Venâncio Aires - RS"
  )

  criarDescricoesDireita(
    cartao,
    numero,
    "SERÃO SORTEADOS DOIS PERNIS SUÍNOS COM PELE",
    False
  )

  cartao.paste(logo, (5, 8))
  return cartao



def criaPagina(numeroDaPagina: int) -> Image:
  logo = Image.open('logo.png')

  #Tamanho A4 com o fundo branco
  pagina: Image = criarFolhaA4()
  
  for numero in range(5):
    if numeroDaPagina == 1:
      numeroDoCartao = (numero + 1)
    else:
      numeroDoCartao = (numero + 1) + ( (numeroDaPagina - 1) * 5)

    pagina.paste(criarCartao(CARTAO, logo, numeroDoCartao), (0, numero *  CARTAO[1]))

  return pagina




def start():
  pagina: Image = criaPagina(1)

  paginas = []

  for numeroDaPagina in range(2, 51, 1):    
    paginas.append(criaPagina(numeroDaPagina))

  pagina.save('cartao.pdf', 'pdf', save_all = True, append_images = paginas)




if __name__ == "__main__":

  start()
