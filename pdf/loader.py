import pymupdf

filename = "C:\\Users\\acer\\Desktop\\Projects\\AI Research Paper Assistant\\data\\papers\\ForgeNet_X_IEEE_Paper.pdf"
doc = pymupdf.open(filename)
toc = doc.get_toc()
print(toc)