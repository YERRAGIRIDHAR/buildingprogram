import justpy as jp

def web1():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text = "A1 AUTOMOBILE Service Point", classes = "text-h6 q-pr-md text-weight-bolder text-center")
    p1 = jp.QDiv(a=wp, text = "Exterior Modification, Painting, Sheeting, Gentral Serivce", classes = "text-h6 q-pr-md text-weight-medium text-center")
    return wp

jp.justpy(web1)