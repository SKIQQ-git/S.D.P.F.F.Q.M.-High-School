# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
transform padrão_direito:
    xalign 0.0
    yalign 0.5

transform padrão_esquerdo:
    xalign 1.0
    yalign 0.5

define r = Character("Rato Cosmico")
define n = Character("Nosferatu")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg patio escolar

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show nixy at padrão_direito

    # These display lines of dialogue.

    r "Eu estou tão feliz pro meu primeiro dia de aula..."

    r "Tomara que dessa vez seja diferente, a escola passada era uma bosta."

    show nosferatu at padrão_esquerdo

    n "Ei, você viu a briga que ta tendo lá no portão da escola? Dois idiotas estão se matando pra saber que é mais inteligente."
    
    menu:

        "Vamo lá?"

        "Sim":
            r "Ok, vamo lá."

        "Não":
            r "Não, não quero ir."

    # This ends the game.

    return
