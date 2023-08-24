from db.db_utilis import criando_tabela, inserindo_registros, consultar_registro, atualizando_registro, exluindo_registro
import sqlite3

criando_tabela('database_alunos2.db', 'Alunos', {'ID': 'INTEGER PRIMARY KEY AUTOINCREMENT', 'Nome': 'TEXT NOT NULL', 'Curso': 'TEXT NOT NULL', 'AnoIngresso': 'INTEGER'})

inserindo_registros('database_alunos2.db', 'Alunos', [('Ana Silva', 'Computação', 2019), ('Pedro Mendes', 'Física', 2021), ('Carla Souza', 'Computação', 2020), ('João Alves', 'Matemática', 2018), ('Maria Oliveira', 'Química', 2022
)])

consultar_registro('database_alunos2.db', 'Alunos', 'AnoIngresso = 2019 OR AnoIngresso = 2020')

atualizando_registro('database_alunos2.db', 'Alunos', 'AnoIngresso', 2024, 'ID', 1)

exluindo_registro('database_alunos2.db', 'Alunos', 1)

consultar_registro('database_alunos2.db', 'Alunos', 'AnoIngresso >= 2019')

atualizando_registro('database_alunos2.db', 'Alunos', 'AnoIngresso', 2018, 'Curso', 'Computação')