import qrcode
site_url = "https://YOUR-USERNAME.github.io/nnc-tarek-contact/"
qrcode.make(site_url).save("NNC_Tarek_Website_QR.png")
print("QR generated for:", site_url)
