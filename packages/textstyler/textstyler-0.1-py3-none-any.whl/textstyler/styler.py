from termcolor import colored

def StyleText(text, color=None, on_color=None, attrs=None):
    """
    Style text with color, background, and attributes.

    :param text: Text to style.
    :param color: Text color (e.g., 'red', 'green', 'blue').
    :param on_color: Background color (e.g., 'on_red', 'on_green').
    :param attrs: List of text attributes (e.g., ['bold', 'underline']).
    :return: Styled text.
    """
    return colored(text, color=color, on_color=on_color, attrs=attrs)
