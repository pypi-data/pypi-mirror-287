def ListFonts():
    """
    List available fonts for banners.
    
    :return: List of font names.
    """
    from pyfiglet import Figlet
    return Figlet().getFonts()
