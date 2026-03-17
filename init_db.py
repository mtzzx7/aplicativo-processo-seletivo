#!/usr/bin/env python3
"""
Script para inicializar o banco de dados e disparar migração
Sem interface gráfica
"""

import sys
from db import connect_db

# Importar a função de inicialização do banco
sys.path.insert(0, '.')
from app import init_db

print("Inicializando banco de dados...")
try:
    init_db()
    print("✅ Banco de dados inicializado/migrado com sucesso!")
    
    # Verificar versão final
    conn = connect_db()
    c = conn.cursor()
    c.execute("PRAGMA user_version")
    version = c.fetchone()[0]
    conn.close()
    print(f"✅ Versão final do schema: {version}")
    
except Exception as e:
    print(f"❌ Erro ao inicializar banco: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
