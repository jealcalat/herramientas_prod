Se pueden generar códigos QR con la librería `qrcode` de Python. Para instalarla, abrir anacoda powershell o cmd y escribir:

```bash
pip install qrcode
```
En windows
```bash
py -m pip install qrcode
```

Luego, en el script de Python, importar la librería y generar el código QR:

```python
import qrcode

# Replace with your Google Drive or GitHub shareable link
shareable_link = "https://drive.google.com/file/d/12KGU3DTogAdwAv82MtCUafCUm2xlnn1Y/view?usp=drive_link"

# Create instance of QRCode
qr = qrcode.QRCode(
    version=None, # incremento en 1 para aumentar el tamaño del código +4 empezando por 21
    # va a depender de la cantidad de caracteres del link. Si se fija en None,
    # el tamaño se ajusta automáticamente. Con el corrección de errores L
    # y version 4 podría ser suficiente.
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    # la corrección de errores es L, que es la más baja; la corrección de errores
    # permite que el código se pueda leer aunque esté dañado, sucio
    # o parcialmente borrado. L permite recuperar hasta el 7% de los datos,
    # M hasta el 15%, Q hasta el 25% y H hasta el 30%.
    box_size=20, # tamaño de los cuadraditos en pixeles
    border=4, # tamaño del borde en cuadraditos
)

# Add data to QRCode
qr.add_data(shareable_link)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("drive_qr.png")
```
