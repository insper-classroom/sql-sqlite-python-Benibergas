import sqlite3

# {'Nome': TEXT NOT NULL, etc}
def criando_tabela (nome_db, nome_tabela, colunas_tabela):
    conn = sqlite3.connect(f'{nome_db}')
    cursor = conn.cursor()
    tabela_query = ''

    for coluna in colunas_tabela:
        if coluna == list(colunas_tabela)[-1]:
            tabela_query += f'{coluna} {colunas_tabela[coluna][-1]} '
        else:
            tabela_query += f'{coluna} {colunas_tabela[coluna]}, '

    cursor.execute (f'''
    CREATE TABLE IF NOT EXISTS {nome_tabela} (
        {tabela_query}
    );
    ''')
    
    conn.commit()


def inserindo_registros (nome_db, nome_tabela, registros):
    conn = sqlite3.connect(f'{nome_db}')
    cursor = conn.cursor()
    teste = registros

    cursor.executemany(f"""
        INSERT INTO {nome_tabela} (Nome, Curso, AnoIngresso)
        VALUES (?, ?, ?);
        """, teste)
    
    conn.commit()


def consultar_registro (nome_db, nome_tabela, filter):
    conn = sqlite3.connect(f'{nome_db}')
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM {nome_tabela} WHERE {filter}')
    print(cursor.fetchall())



def atualizando_registro (nome_db, nome_tabela, nome_coluna, novo_valor, condicao, valor_condicao):
    conn = sqlite3.connect(f'{nome_db}')
    cursor = conn.cursor()

    cursor.execute(f'UPDATE {nome_tabela} SET {nome_coluna} = ? WHERE {condicao} = ?', (novo_valor, valor_condicao))
    conn.commit()


def exluindo_registro (nome_db, nome_tabela, id):
    conn = sqlite3.connect(f'{nome_db}')
    cursor = conn.cursor()

    cursor.execute(f'DELETE FROM {nome_tabela} WHERE ID = {id}')
    conn.commit()
