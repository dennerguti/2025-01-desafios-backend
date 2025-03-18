<div align="center">  
  <img src="https://github.com/user-attachments/assets/2acc5cab-7ec9-4cc6-a3fc-1fe80eceee73" alt="logo" style="width:100px"></img>
</div>

## Desafios Estagiarios Backend

### Descrição
Desafios técnicos para os estagiarios do processo seletivo 2025.01 da [SIAPESQ](https://siapesq.com).

Realize o desafio que foi informado na sua entrevista

### Entrega limite 14/04
  Envie o link do repositorio para nos
  
### Desafios
* #### Desafio A - Time de Tooling e processamento de dados

  #### Descrição
    ##### Parte 1
  
    Desenvolva uma ferramenta CLI que utilize o [GBIF](https://techdocs.gbif.org/en/data-use/pygbif) para extrair registros de ocorrências da uma especie marinha informada com base no bounding box e no periodo de tempo informado.
  
    O csv de saida deve seguir o seguinte formato:

    ```csv
    decimalLongitude,decimalLatitude,year,day,month
    -83.08,24.13,2000,1,1
    -77.66,28.41,2000,2,1
    -77.25,29.25,2000,4,1
    -79.5,26.31,2000,5,1
    ```
  
    Exemplo:
  
      python gbifer.py --specie "Thunnus Obesus' --bbox 90 -90 180 -180 --limit 200 --begin_date '2000-01-01' --end_date '2000-02-01' --out_csv exemple.csv

    #### Parte 2
    Desenvolva uma ferramenta que o utilize o [Toolbox do Copernicus Marine Service](https://pypi.org/project/copernicusmarine) para extrair dados de temperatura(thetao) e salinidade(so) com base em um csv informado.
    O CSV informado deve estar no mesmo formato que o csv de saida da parte 1
    Exemplo :

      python dmarine.py --csv exemple.csv --out_csv dmarine_out.csv

    Exemplo do csv de saida:
    ```csv
    decimalLongitude,decimalLatitude,year,day,month,thetao,so
    -22.688034,32.415675,2022.0,7.0,5.0,19.724814601242542,36.90603347495198
    4.755267,-25.042099,2022.0,12.0,10.0,18.26358836889267,35.7783745508641
    -43.451333,-25.543,2021.0,25.0,12.0,25.30530716478825,37.40958888083696
    -81.982437,-1.827095,2020.0,10.0,10.0,22.89190343767405,33.75652329996228
    -26.215975,37.567852,2017.0,22.0,8.0,24.344340339303017,36.37653733603656
    ```

    #### Detalhes Adicionais:
    * **Não** exponha nenhuma de suas variavies de ambiente(login copernicus,login gbif,etc)
    * Adicione quantos argumentos nos CLI tu achares necessário e adicione explicaçoes para cada um deles
      
        Exemplo '--limit' serve para limitar o resultado que vem da API do GBIF

  

  
* #### Desafio B - Time Web

    ##### Descrição
    Desenvolva uma REST API utilizando [Node](https://nodejs.org) ,[Express framework](https://expressjs.com) e [SequelizeORM](https://sequelize.org)
    na qual implemente o CRUD de todas as entidades no diagrama abaixo:
  
    ![diagrama](https://github.com/user-attachments/assets/8098a6ec-ce8a-4a91-953f-3866a9b0782a)

    #### Detalhes Adicionais:
    * Exija autentificação por JWT em todas as rotas exceto a de login e de criação de usuario
    * Rotas de Listagem deve ser páginadas por parametros na query do request (limit e offset)
    * **Não será necessário nenhum serviço de arquivos externo(S3,AzureStorage,etc)** faça upload local e guarde o path
    * Utilize qualquer banco relacional
    

### Dúvidas
  Em caso de dúvidas entre em contato pelo grupo do whats ou no privado (Bruno ou Theodor)

  
