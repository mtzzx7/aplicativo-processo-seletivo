#!/usr/bin/env python3
"""
Script de teste para validar migração do banco de dados
Verifica se as novas tabelas foram criadas com sucesso
"""

import sqlite3
from pathlib import Path

DB_PATH = Path("selection.db")

def test_migration():
    """Testa se a migração foi feita corretamente"""
    
    if not DB_PATH.exists():
        print("❌ Banco de dados não encontrado. Será criado na primeira execução da app.")
        return False
    
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        # Verificar versão do schema
        c.execute("PRAGMA user_version")
        version = c.fetchone()[0]
        print(f"✅ Versão do schema: {version}")
        
        if version < 12:
            print(f"⚠️  Schema versão {version} é anterior à versão 12")
            print("   A migração será feita automaticamente na próxima execução")
            conn.close()
            return False
        
        # Tabela logic_scores deve existir
        c.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='logic_scores'
        """)
        if c.fetchone():
            print("✅ Tabela 'logic_scores' encontrada")
        else:
            print("❌ Tabela 'logic_scores' NÃO encontrada")
            conn.close()
            return False
        
        # Campo evaluation_type deve existir em evaluations
        c.execute("PRAGMA table_info(evaluations)")
        columns = [row[1] for row in c.fetchall()]
        if 'evaluation_type' in columns:
            print("✅ Campo 'evaluation_type' encontrado em 'evaluations'")
        else:
            print("❌ Campo 'evaluation_type' NÃO encontrado em 'evaluations'")
            conn.close()
            return False
        
        # Verificar candidatos
        c.execute("SELECT COUNT(*) FROM candidates")
        count = c.fetchone()[0]
        print(f"✅ Total de candidatos: {count}")
        
        # Verificar equipes
        c.execute("SELECT COUNT(*) FROM teams")
        count = c.fetchone()[0]
        print(f"✅ Total de equipes: {count}")
        
        conn.close()
        print("\n✅ Migração validada com sucesso!")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao validar banco de dados: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("Teste de Migração do Banco de Dados")
    print("=" * 50)
    success = test_migration()
    print("=" * 50)
    exit(0 if success else 1)
