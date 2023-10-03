# importação da biblioteca Flet
import flet as ft


# classe chamada Message que representa uma mensagem no chat.
class Message():
    def __init__(self, user_name: str, text: str, message_type: str):
        self.user_name = user_name
        self.text = text
        self.message_type = message_type

class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.vertical_alignment="start"
        self.controls=[
                ft.CircleAvatar(
                    content=ft.Text(self.get_initials(message.user_name)),
                    color=ft.colors.WHITE,
                    bgcolor=self.get_avatar_color(message.user_name),
                ),
                ft.Column(
                    [
                        ft.Text(message.user_name, weight="bold"),
                        ft.Text(message.text, selectable=True),
                    ],
                    tight=True,
                    spacing=5,
                ),
            ]
    '''
    Isso define uma função chamada get_initials que recebe dois parâmetros, self (que é uma referência à instância da classe, 
    embora não seja usada no corpo do método) e user_name (que é uma string representando o nome de usuário).
user_name[:1]: Isso usa a sintaxe de fatiamento de strings ([:1]) para obter os primeiros caracteres da string user_name. 
Neste caso, está pegando o primeiro caractere.

.capitalize(): Este método converte o primeiro caractere da string para maiúsculo, 
e os caracteres restantes para minúsculo. Isso é feito para garantir que as iniciais estejam sempre em maiúsculas, 
independentemente da forma como o nome de usuário é inserido.
    '''
    def get_initials(self, user_name: str):
       # return user_name[:1].capitalize()
        return user_name

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
            ft.colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]
    
# Define a função principal do programa, que recebe um objeto page da biblioteca Flet.
def main(page: ft.Page):
    # Configura a orientação da página como horizontal e atribui o título "Flet Chat".
    page.horizontal_alignment = "stretch"
    page.title = "Flet Chat"
    # Define duas funções de clique: uma para entrar no chat (join_chat_click) e outra para enviar mensagens (send_message_click).
    def join_chat_click(e):
        if not join_user_name.value:
            join_user_name.error_text = "Name cannot be blank!"
            join_user_name.update()
        else:
            page.session.set("user_name", join_user_name.value)
            page.dialog.open = False
            new_message.prefix = ft.Text(f"{join_user_name.value}: ")
            page.pubsub.send_all(Message(user_name=join_user_name.value, text=f"{join_user_name.value} has joined the chat.", message_type="login_message"))
            page.update()

    def send_message_click(e):
        if new_message.value != "":
            page.pubsub.send_all(Message(page.session.get("user_name"), new_message.value, message_type="chat_message"))
            new_message.value = ""
            new_message.focus()
            page.update()

# Define uma função para manipular mensagens recebidas, criando instâncias adequadas de ChatMessage ou ft.Text e adicionando à lista de mensagens no chat.
    def on_message(message: Message):
        if message.message_type == "chat_message":
            m = ChatMessage(message)
        elif message.message_type == "login_message":
            m = ft.Text(message.text, italic=True, color=ft.colors.BLACK45, size=12)
        chat.controls.append(m)
        page.update()
# Registra a função on_message como um assinante para receber mensagens sempre que são enviadas para o pub/sub.
    page.pubsub.subscribe(on_message)

    # Cria um campo de texto para que o usuário insira seu nome antes de entrar no chat.
    join_user_name = ft.TextField(
        label="Enter your name to join the chat",
        autofocus=True,
        on_submit=join_chat_click,
    )
    page.dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Welcome!"),
        content=ft.Column([join_user_name], width=300, height=70, tight=True),
        actions=[ft.ElevatedButton(text="Join chat", on_click=join_chat_click)],
        actions_alignment="end",
    )

    # Cria uma lista visual para exibir as mensagens do chat. Configura para expandir e rolar automaticamente.
    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    # Adiciona o chat e o campo de nova mensagem à página.
    new_message = ft.TextField(
        hint_text="Digite uma mensagem...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        on_submit=send_message_click,
    )

    # Adicione tudo à página
    page.add(
        ft.Container(
            content=chat,
            border=ft.border.all(1, ft.colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True,
        ),
        ft.Row(
            [
                new_message,
                ft.IconButton(
                    icon=ft.icons.SEND_ROUNDED,
                    tooltip="Send message",
                    on_click=send_message_click,
                ),
            ]
        ),
    )
# Inicializa o aplicativo Flet, definindo a porta para 8001, o alvo como a função principal 
ft.app(port=8001, target=main, view=ft.WEB_BROWSER)



