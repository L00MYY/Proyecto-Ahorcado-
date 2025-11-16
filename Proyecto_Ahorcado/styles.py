TITLE_CHAR = "="       
SEPARATOR_CHAR = "-"   
LOADING_CHAR = "#"     
EMPTY_CHAR = "."       


def center_text(text, width=80):
    padding = (width - len(text)) // 2
    return " " * padding + text