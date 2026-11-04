from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import os, zipfile

# --- CAMBIO AQUÍ: Ruta exacta a tus documentos ---
        # --- CAMBIO AQUÍ: Ruta exacta a tus documentos ---
base = r"C:\Users\Emiliano Marcial\Documents\word"
# ------------------------------------------------
os.makedirs(base, exist_ok=True)

def setup_doc(title, subtitle):
    doc = Document()
    sec = doc.sections[0]
    sec.top_margin = Inches(0.7)
    sec.bottom_margin = Inches(0.7)
    sec.left_margin = Inches(0.8)
    sec.right_margin = Inches(0.8)

    normal = doc.styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(10)
    normal.paragraph_format.space_after = Pt(6)

    h1 = doc.styles["Heading 1"]
    h1.font.name = "Arial"
    h1.font.color.rgb = RGBColor(21, 101, 192)
    h1.font.size = Pt(16)

    h2 = doc.styles["Heading 2"]
    h2.font.name = "Arial"
    h2.font.color.rgb = RGBColor(13, 71, 161)
    h2.font.size = Pt(12)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("INVENTARIO DE ALMACENAMIENTO")
    r.bold = True
    r.font.size = Pt(22)
    r.font.color.rgb = RGBColor(21, 101, 192)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(title)
    r.bold = True
    r.font.size = Pt(16)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run(subtitle + "\nVersión 1.0 · 2026").italic = True

    doc.add_paragraph("")
    return doc

def add_bullets(doc, items):
    for item in items:
        doc.add_paragraph(item, style="List Bullet")

def add_table(doc, headers, rows):
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = h
        for run in cell.paragraphs[0].runs:
            run.bold = True
            run.font.color.rgb = RGBColor(255,255,255)
        tcPr = cell._tc.get_or_add_tcPr()
        shd = OxmlElement('w:shd')
        shd.set(qn('w:fill'), '1565C0')
        tcPr.append(shd)
    for row in rows:
        cells = table.add_row().cells
        for i, value in enumerate(row):
            cells[i].text = value
    return table

# Manual del sistema
doc = setup_doc("MANUAL DEL SISTEMA", "Documento de apoyo del sistema")
doc.add_heading("1. Introducción", level=1)
doc.add_paragraph(
    "El sistema Inventario de Almacenamiento es una aplicación web orientada al control "
    "de productos, categorías, proveedores, movimientos y operaciones de compra. Su propósito "
    "es centralizar la información del inventario y facilitar las actividades de administración y consulta."
)
doc.add_heading("2. Objetivo", level=1)
doc.add_paragraph(
    "Proporcionar una herramienta para mantener organizada la información de los productos, "
    "consultar existencias, registrar operaciones y dar seguimiento a las ventas realizadas por los clientes."
)
doc.add_heading("3. Tipos de usuario", level=1)
doc.add_paragraph(
    "Administrador: administra la información general del sistema, incluyendo productos, categorías, "
    "usuarios, proveedores, movimientos y ventas, de acuerdo con las opciones habilitadas."
)
doc.add_paragraph(
    "Cliente: consulta el catálogo, agrega productos al carrito, revisa sus compras y realiza pagos "
    "mediante PayPal Sandbox durante las pruebas."
)
doc.add_heading("4. Módulos principales", level=1)
add_table(doc, ["Módulo", "Descripción"], [
    ["Productos", "Consulta y administración de productos y existencias."],
    ["Categorías", "Organización de productos por tipo o clasificación."],
    ["Proveedores", "Registro y consulta de proveedores."],
    ["Usuarios", "Administración de cuentas y estados de usuario."],
    ["Movimientos", "Registro de entradas, salidas y ajustes de inventario."],
    ["Ventas", "Consulta de ventas y sus detalles."],
    ["Compras", "Carrito, creación de compras e historial del cliente."],
    ["Pagos", "Registro y confirmación de pagos mediante PayPal Sandbox."]
])
doc.add_heading("5. Recomendaciones de uso", level=1)
add_bullets(doc, [
    "Mantener actualizados los datos de productos y proveedores.",
    "Verificar las cantidades antes de registrar movimientos.",
    "No compartir contraseñas.",
    "Confirmar que una venta esté pagada antes de considerarla finalizada.",
    "Utilizar las cuentas Sandbox únicamente para pruebas."
])
doc.add_heading("6. Consideraciones", level=1)
doc.add_paragraph(
    "La integración configurada con PayPal Sandbox es un entorno de pruebas. Los pagos realizados "
    "en Sandbox son simulados y no representan cobros reales. Para operar comercialmente se requiere "
    "configurar credenciales Live y realizar las verificaciones de seguridad correspondientes."
)
manual_path = os.path.join(base, "manual_inventario.docx")
doc.save(manual_path)

# Catálogo de productos
doc = setup_doc("CATÁLOGO DE PRODUCTOS", "Documento de referencia")
doc.add_heading("1. Presentación", level=1)
doc.add_paragraph(
    "Este documento describe la información que utiliza el catálogo del sistema Inventario de "
    "Almacenamiento. El catálogo permite consultar los artículos registrados y conocer sus datos principales."
)
doc.add_heading("2. Información de cada producto", level=1)
add_table(doc, ["Campo", "Descripción"], [
    ["Código", "Identificador o clave asignada al producto."],
    ["Nombre", "Nombre descriptivo del artículo."],
    ["Categoría", "Clasificación a la que pertenece el producto."],
    ["Precio", "Importe de venta registrado para el producto."],
    ["Stock", "Cantidad disponible registrada en el inventario."],
    ["Estado", "Situación del producto dentro del sistema, si aplica."]
])
doc.add_heading("3. Consulta del catálogo", level=1)
doc.add_paragraph(
    "Para consultar los productos disponibles, el cliente debe iniciar sesión y entrar al apartado "
    "Productos. Desde esa sección puede revisar los artículos publicados y agregarlos al carrito cuando estén disponibles."
)
doc.add_heading("4. Actualización de la información", level=1)
doc.add_paragraph(
    "Los datos del catálogo deben mantenerse actualizados desde el módulo de administración. "
    "Cuando se registra una compra pagada, el sistema descuenta las cantidades correspondientes del stock "
    "y registra el movimiento de salida."
)
doc.add_heading("5. Nota importante", level=1)
doc.add_paragraph(
    "Este documento es una guía general de los campos del catálogo; no es una exportación automática "
    "de los registros actuales de MySQL. Para consultar existencias y precios vigentes, utiliza el catálogo "
    "dentro de la aplicación."
)
catalog_path = os.path.join(base, "catalogo_productos.docx")
doc.save(catalog_path)

# Guía del usuario
doc = setup_doc("GUÍA DEL USUARIO", "Instrucciones básicas de uso")
doc.add_heading("1. Acceso al sistema", level=1)
doc.add_paragraph(
    "Abre la dirección local del proyecto en el navegador. Si ya tienes una cuenta, entra desde la opción "
    "de inicio de sesión. Si todavía no tienes una cuenta, utiliza el formulario de registro."
)
doc.add_heading("2. Funciones del cliente", level=1)
doc.add_paragraph("Consultar productos: entra al apartado Productos para revisar los artículos disponibles.")
doc.add_paragraph("Agregar al carrito: selecciona los productos y las cantidades que deseas comprar.")
doc.add_paragraph("Revisar compras: consulta el resumen del carrito y el historial de operaciones.")
doc.add_paragraph("Consultar documentación: abre los manuales disponibles desde el apartado Documentación.")
doc.add_heading("3. Realizar una compra", level=1)
add_bullets(doc, [
    "Inicia sesión como cliente.",
    "Consulta el catálogo de productos.",
    "Agrega los artículos deseados al carrito.",
    "Revisa las cantidades y el total.",
    "Continúa para generar la compra.",
    "En el recibo, selecciona el botón de PayPal para continuar con el pago."
])
doc.add_heading("4. Pago mediante PayPal Sandbox", level=1)
doc.add_paragraph(
    "Durante las pruebas, utiliza una cuenta Personal Sandbox creada desde PayPal Developer. "
    "La cuenta Business Sandbox funciona como receptor de los pagos simulados. No se debe utilizar "
    "una tarjeta real ni compartir credenciales privadas. El pago se considera confirmado cuando el "
    "sistema recibe y verifica la respuesta de PayPal."
)
doc.add_heading("5. Después del pago", level=1)
doc.add_paragraph(
    "Cuando el pago se confirma, la venta cambia a estado pagada, el registro de pago cambia a completado, "
    "se actualizan las existencias y se registra el movimiento de salida correspondiente. El cliente puede consultar su recibo."
)
doc.add_heading("6. Recomendaciones", level=1)
add_bullets(doc, [
    "Revisa las cantidades antes de confirmar una compra.",
    "No cierres la ventana mientras se procesa el pago.",
    "Si ocurre un error, verifica el estado de la compra antes de intentar pagar otra vez.",
    "Conserva el recibo como comprobante de la operación."
])
doc.add_heading("7. Ayuda", level=1)
doc.add_paragraph(
    "Si una opción no aparece o no permite realizar una operación, contacta al administrador del sistema "
    "para revisar los permisos, el estado de la cuenta o la disponibilidad de los productos."
)
guide_path = os.path.join(base, "guia_usuario.docx")
doc.save(guide_path)

zip_path = "/mnt/data/documentos_inventario_word.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for p in [manual_path, catalog_path, guide_path]:
        z.write(p, arcname=os.path.basename(p))

print("Archivos Word creados:")
print(manual_path)
print(catalog_path)
print(guide_path)
print(zip_path)