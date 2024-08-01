from pyfiglet import Figlet

def CreateBanner(text, font='standard'):
    """
    Create a text banner.

    :param text: Text to create a banner for.
    :param font: Font for the banner (default is 'standard').
    :return: Banner text.
    """
    figlet = Figlet(font=font)
    return figlet.renderText(text)
