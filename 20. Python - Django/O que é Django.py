# O que é Django?
# Django é um framework Python que facilita a criação de sites usando Python.

# O Django cuida das coisas difíceis para que você possa se concentrar na construção de suas aplicações web.

# O Django enfatiza a reutilização de componentes, também conhecido como DRY (Don't Repeat Yourself), e vem com recursos prontos para uso, como sistema de login, conexão de banco de dados e operações CRUD (Create Read Update Delete).

# Como funciona o Django?
# O Django segue o padrão de design MVT (Model View Template).

# Modelo - Os dados que você deseja apresentar, geralmente dados de um banco de dados.
# View - Um manipulador de solicitação que retorna o modelo e o conteúdo relevantes - com base na solicitação do usuário.
# Template - Um arquivo de texto (como um arquivo HTML) contendo o layout da página da web, com lógica de como exibir os dados.

# Model
# O modelo fornece dados do banco de dados.
# No Django, os dados são entregues como um Object Relational Mapping (ORM), que é uma técnica projetada para facilitar o trabalho com bancos de dados.

# A maneira mais comum de extrair dados de um banco de dados é o SQL. Um problema com o SQL é que você precisa ter um bom entendimento da estrutura do banco de dados para poder trabalhar com ele.
# O Django, com ORM, facilita a comunicação com o banco de dados, sem ter que escrever instruções SQL complexas.
# Os modelos geralmente estão localizados em um arquivo chamado models.py.

# View
# Uma view é uma função ou método que recebe solicitações http como argumentos, importa o(s) modelo(s) relevante(s), descobre quais dados enviar para o modelo e retorna o resultado final.
# As visualizações geralmente estão localizadas em um arquivo chamado views.py.

# Template
# Um template é um arquivo onde você descreve como o resultado deve ser representado.
# Os templates geralmente são arquivos .html, com código HTML descrevendo o layout de uma página da web, mas também podem estar em outros formatos de arquivo para apresentar outros resultados, mas vamos nos concentrar nos arquivos .html.

# Django usa HTML padrão para descrever o layout, mas usa tags Django para adicionar lógica.

# Os templates de um aplicativo estão localizados em uma pasta chamada templates.

# URLs
# O Django também fornece uma maneira de navegar pelas diferentes páginas de um site.

# Quando um usuário solicita uma URL, o Django decide para qual visualização ele a enviará.

# Isso é feito em um arquivo chamado urls.py.