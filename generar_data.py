#!/usr/bin/env python3
"""
Generador de Base de Datos - Tienda de Deportes Extremos "El Último Salto"
===========================================================================

Este script crea una base de datos SQLite con datos sintéticos realistas para
un taller de SQL educativo. Genera 4 tablas normalizadas y al menos 1000 transacciones
de venta con lógica de negocio especial (cupón ULTIMO_SUSPIRO para mayores de 60 años).

Dependencias: faker, sqlite3 (stdlib)
Uso: python3 generar_data.py
Salida: tienda.db (en el mismo directorio)
"""

import sqlite3
import random
from datetime import datetime, timedelta
from faker import Faker

# Configuración
DB_NAME = "tienda.db"
NUM_CLIENTES = 250
NUM_VENTAS = 1250  # Garantiza más de 1000
SEED = 42  # Para reproducibilidad


def crear_conexion(db_name):
    """Crea conexión a la base de datos SQLite."""
    try:
        conn = sqlite3.connect(db_name)
        print(f"✓ Conexión a {db_name} establecida")
        return conn
    except sqlite3.Error as e:
        print(f"✗ Error al conectar: {e}")
        return None


def crear_tablas(conn):
    """Crea las 4 tablas del esquema normalizado."""
    cursor = conn.cursor()

    # Tabla: clientes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL UNIQUE,
            fecha_nacimiento DATE NOT NULL,
            genero TEXT NOT NULL CHECK(genero IN ('M', 'F', 'Otro'))
        )
    """)

    # Tabla: productos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL CHECK(precio > 0),
            stock INTEGER NOT NULL DEFAULT 0
        )
    """)

    # Tabla: ventas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ventas (
            id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER NOT NULL,
            fecha_venta DATE NOT NULL,
            total_venta REAL NOT NULL CHECK(total_venta >= 0),
            cupon_usado TEXT,
            FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente)
        )
    """)

    # Tabla: detalle_ventas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS detalle_ventas (
            id_detalle INTEGER PRIMARY KEY AUTOINCREMENT,
            id_venta INTEGER NOT NULL,
            id_producto INTEGER NOT NULL,
            cantidad INTEGER NOT NULL CHECK(cantidad > 0),
            precio_unitario REAL NOT NULL CHECK(precio_unitario > 0),
            FOREIGN KEY(id_venta) REFERENCES ventas(id_venta),
            FOREIGN KEY(id_producto) REFERENCES productos(id_producto)
        )
    """)

    conn.commit()
    print("✓ Tablas creadas exitosamente")


def generar_clientes(conn, num_clientes):
    """Genera clientes realistas con distribucion de edades variada."""
    fake = Faker("es_ES")
    Faker.seed(SEED)
    random.seed(SEED)

    cursor = conn.cursor()
    clientes = []

    # Para garantizar buenos datos de tercera edad
    fecha_hoy = datetime.now().date()

    for i in range(num_clientes):
        nombre = fake.name()
        correo = fake.email()

        # Distribución de edades:
        # 30% mayores de 60 años (para "ULTIMO_SUSPIRO")
        # 70% menores de 60 años
        if random.random() < 0.30:
            # Mayor de 60 años: entre 61 y 90 años
            edad = random.randint(61, 90)
        else:
            # Menor de 60 años: entre 18 y 59 años
            edad = random.randint(18, 59)

        fecha_nacimiento = fecha_hoy - timedelta(days=edad * 365 + random.randint(0, 365))
        genero = random.choice(["M", "F", "Otro"])

        clientes.append((nombre, correo, fecha_nacimiento, genero))

    cursor.executemany(
        "INSERT INTO clientes (nombre, correo, fecha_nacimiento, genero) VALUES (?, ?, ?, ?)",
        clientes,
    )
    conn.commit()
    print(f"✓ {num_clientes} clientes insertados")


def generar_productos(conn):
    """Genera catálogo realista de productos para deportes extremos."""
    cursor = conn.cursor()

    productos = [
        # Paracaídas (Producto Principal)
        ("Paracaídas Militar Pro", "Paracaídas", 3500.00),
        ("Paracaídas Deportivo Elite", "Paracaídas", 2800.00),
        ("Paracaídas de Emergencia Compacto", "Paracaídas", 1500.00),
        ("Paracaídas Tandem para Instructor", "Paracaídas", 5200.00),
        ("Paracaídas de Precisión Racing", "Paracaídas", 4100.00),
        # Accesorios
        ("Casco Integral Carbon Fiber", "Accesorios", 850.00),
        ("Casco Abierto Ligero", "Accesorios", 450.00),
        ("Altímetro Digital Precisión", "Accesorios", 280.00),
        ("Altímetro Analógico Confiable", "Accesorios", 150.00),
        ("Traje de Vuelo Aerodinámico XL", "Accesorios", 1200.00),
        ("Traje de Vuelo Estándar M/L", "Accesorios", 900.00),
        ("Gafas Panorámicas Anti-reflejo", "Accesorios", 320.00),
        ("Gafas de Noche Infra-ventiladas", "Accesorios", 580.00),
        ("Guantes Térmicos Profesionales", "Accesorios", 240.00),
        ("Mochila de Reserva Compacta", "Accesorios", 1800.00),
    ]

    cursor.executemany(
        "INSERT INTO productos (nombre, categoria, precio) VALUES (?, ?, ?)",
        productos,
    )
    conn.commit()
    print(f"✓ {len(productos)} productos insertados")


def generar_ventas(conn, num_ventas):
    """Genera transacciones realistas con aplicación inteligente del cupón ULTIMO_SUSPIRO."""
    cursor = conn.cursor()
    fake = Faker("es_ES")
    Faker.seed(SEED)
    random.seed(SEED)

    # Obtener IDs de clientes y productos
    cursor.execute("SELECT id_cliente, fecha_nacimiento FROM clientes ORDER BY RANDOM()")
    clientes = cursor.fetchall()

    cursor.execute("SELECT id_producto, precio FROM productos")
    productos = cursor.fetchall()

    fecha_inicio = datetime(2024, 1, 1).date()
    fecha_fin = datetime(2025, 12, 31).date()
    fecha_hoy = datetime.now().date()

    for _ in range(num_ventas):
        id_cliente = random.choice(clientes)[0]
        fecha_venta = fecha_inicio + timedelta(days=random.randint(0, (fecha_fin - fecha_inicio).days))

        # Determinar si aplica cupón ULTIMO_SUSPIRO (cliente > 60 años)
        cursor.execute(
            "SELECT fecha_nacimiento FROM clientes WHERE id_cliente = ?",
            (id_cliente,),
        )
        fecha_nacimiento = cursor.fetchone()[0]
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()

        edad = (fecha_hoy - fecha_nacimiento).days // 365
        cupon_usado = None
        descuento = 1.0

        if edad > 60:
            # Aplicar cupón con probabilidad 70%
            if random.random() < 0.70:
                cupon_usado = "ULTIMO_SUSPIRO"
                descuento = 0.70  # 30% de descuento

        # Generar detalles de la venta (1-3 productos)
        num_productos = random.randint(1, 3)
        productos_venta = random.sample(productos, min(num_productos, len(productos)))

        total_venta = 0.0
        detalles = []

        for id_producto, precio_base in productos_venta:
            cantidad = random.randint(1, 2)
            precio_unitario = precio_base * descuento
            subtotal = cantidad * precio_unitario
            total_venta += subtotal

            detalles.append((id_producto, cantidad, precio_unitario))

        # Insertar venta
        cursor.execute(
            "INSERT INTO ventas (id_cliente, fecha_venta, total_venta, cupon_usado) VALUES (?, ?, ?, ?)",
            (id_cliente, fecha_venta, round(total_venta, 2), cupon_usado),
        )

        id_venta = cursor.lastrowid

        # Insertar detalles de venta
        for id_producto, cantidad, precio_unitario in detalles:
            cursor.execute(
                "INSERT INTO detalle_ventas (id_venta, id_producto, cantidad, precio_unitario) VALUES (?, ?, ?, ?)",
                (id_venta, id_producto, cantidad, round(precio_unitario, 2)),
            )

    conn.commit()
    print(f"✓ {num_ventas} ventas generadas")


def validar_datos(conn):
    """Valida la integridad y coherencia de los datos generados."""
    cursor = conn.cursor()

    # Conteos
    cursor.execute("SELECT COUNT(*) FROM clientes")
    num_clientes = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM productos")
    num_productos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM ventas")
    num_ventas = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM detalle_ventas")
    num_detalles = cursor.fetchone()[0]

    # Cupones aplicados
    cursor.execute("SELECT COUNT(*) FROM ventas WHERE cupon_usado = 'ULTIMO_SUSPIRO'")
    num_cupones = cursor.fetchone()[0]

    # Clientes con descuento vs edad
    cursor.execute("""
        SELECT COUNT(DISTINCT v.id_cliente)
        FROM ventas v
        JOIN clientes c ON v.id_cliente = c.id_cliente
        WHERE v.cupon_usado = 'ULTIMO_SUSPIRO'
        AND (julianday('now') - julianday(c.fecha_nacimiento)) / 365.25 > 60
    """)
    cupones_validos = cursor.fetchone()[0]

    # Estadísticas de ventas
    cursor.execute("SELECT SUM(total_venta) FROM ventas")
    total_ingresos = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(total_venta) FROM ventas WHERE cupon_usado = 'ULTIMO_SUSPIRO'")
    total_descuentos = cursor.fetchone()[0] or 0

    print("\n" + "=" * 60)
    print("VALIDACIÓN Y ESTADÍSTICAS DE DATOS")
    print("=" * 60)
    print(f"✓ Clientes generados: {num_clientes}")
    print(f"✓ Productos en catálogo: {num_productos}")
    print(f"✓ Ventas registradas: {num_ventas}")
    print(f"✓ Líneas de detalle: {num_detalles}")
    print(f"\n✓ Cupones ULTIMO_SUSPIRO aplicados: {num_cupones}")
    print(f"✓ Cupones validados (cliente > 60 años): {cupones_validos}")
    print(f"\n✓ Ingresos totales: ${total_ingresos:,.2f}")
    print(f"✓ Ventas con descuento: ${total_descuentos:,.2f}")
    print(f"✓ Tasa de descuento: {(total_descuentos / total_ingresos * 100):.1f}%")
    print("=" * 60 + "\n")


def main():
    """Orquesta el flujo completo de generación de datos."""
    print("\n🚀 Iniciando generación de base de datos...")
    print("   Tienda de Deportes Extremos: El Último Salto\n")

    # Crear conexión
    conn = crear_conexion(DB_NAME)
    if not conn:
        return

    try:
        # Crear estructura
        crear_tablas(conn)

        # Generar datos
        print("\n📊 Generando datos...")
        generar_clientes(conn, NUM_CLIENTES)
        generar_productos(conn)
        generar_ventas(conn, NUM_VENTAS)

        # Validar
        print("\n✅ Validando integridad...")
        validar_datos(conn)

    except Exception as e:
        print(f"\n✗ Error durante la generación: {e}")
    finally:
        conn.close()
        print(f"✓ Base de datos guardada como: {DB_NAME}\n")


if __name__ == "__main__":
    main()
