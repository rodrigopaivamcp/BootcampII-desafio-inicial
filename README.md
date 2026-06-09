# 💰 Gestor de Gastos Multitens

Este é o projeto final desenvolvido para o **Bootcamp II**. O sistema consiste em um gerenciador de finanças pessoais que permite o cadastro, visualização e exclusão de gastos, contando com conversão automática de moedas e persistência de dados em nuvem.

## 🚀 Link do Aplicativo Publicado
O sistema está em produção e pode ser acessado aqui:
👉 **[CLIQUE AQUI PARA ACESSAR O APP](https://bootcampii-desafio-inicial-j6gtfxfhatgwlzgekkpqpu.streamlit.app/)**

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Interface Web:** [Streamlit](https://streamlit.io/)
* **Banco de Dados:** PostgreSQL (Hospedado na nuvem via [Supabase](https://supabase.com/))
* **Integração de Banco:** `psycopg2-binary`
* **Criptografia de Credenciais:** Streamlit Secrets (`[env]`)

---

## 👥 Desenvolvedores (Grupo)
* **Rodrigo Paiva**
* **Thales Freitas**

---

## 📈 Boas Práticas e Governança de Código Implementadas
Durante o ciclo de desenvolvimento, nossa equipe aplicou conceitos reais de engenharia de software:
1. **Gerenciamento de Tarefas:** Divisão do escopo do projeto através de *Issues* no GitHub.
2. **Trabalho em Equipe com Git:** Criação de ramificações (*Feature Branches*) paralelas para que nenhum desenvolvedor interferisse no código do outro.
3. **Revisão de Código (Code Review):** Integração das funcionalidades na branch principal (`main`) realizada exclusivamente através de *Pull Requests* validados pela dupla.
4. **Segurança da Informação:** Nenhuma senha ou URL de banco de dados foi exposta no código público. Todas as credenciais foram mascaradas e injetadas via variáveis de ambiente seguras no ambiente de Deploy.
