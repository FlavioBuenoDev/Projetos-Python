# Flet - Flutter

"""
Passo a Passo

1° Botao para iniciar chat
Popup para entrar no chat
Quando entrar no chat: (aparece para todo mundo)
    a mensagem que você entrou no chat
    o campo e o botão de enviar mensagem 

a cada mensagem que envia (aparece para todo mundo)
    Nome: Texto da mensagem

  Passo para trabalhar com flet

  1- importat flet
  2- criar funçao para gerenciar o site
  3 - precisa indicar qual é a target(pagina) que ele vai usar como principal
"""
import flet as ft

def main(pagina):
    # add/update controls on Page
    texto = ft.Text("ChatNew")

    # adicionar coluna no campo chat
    chat = ft.Column()

    nome_usuario = ft.TextField(label="Escreva seu nome")
        
    # Envia a mensagem pelo tunel
    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]

            # adiciona a mensagem no chat
            chat.controls.append(ft.Text(f"{usuario_mensagem}:{texto_mensagem}"))
        else:
            # Enviar mensagem a todos a entrada do usuário
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", 
                                         size=12,
                                         italic=True,
                                         color=ft.colors.ORANGE_400
                                         ))
            
        pagina.update()

        #PubSub - Tunel de comunicação entre usuários
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    # Envia a mensagem 
    def enviar_mensagem(evento):        
        pagina.pubsub.send_all({"texto":" "+campo_mensagem.value, "usuario":" "+nome_usuario.value, "tipo": "mensagem"})
        #limpar o campo
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
   
    def entrar_popup(evento):
        # Envia a todos a entrada de um usuário
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})

        # adicionar o chat
        pagina.add(chat)
        # fechar o popup
        popup.open = False
        # remover botão iniciar chat
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        # criar o campoi msg do usuário
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
            ))
        # criar o botão de enviar mensagem
        pagina.add(botao_enviar_mensagem)
        # atualiza a pagina
        pagina.update()
    

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo"),
        content=nome_usuario ,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],

    )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=entrar_chat)

    # Adiciona a tela
    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER, port=8000)


