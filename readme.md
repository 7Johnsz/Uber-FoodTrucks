<img src="/.github/uber.png" width=100px>

# Uber: Food Trucks | Backend Sênior 🏆

Este projeto trata-se de um desafio técnico backend da **Uber**. Solucionado como **perfil sênior** usando **Python**.

`Desafio Proposto:` Crie um serviço que informe ao usuário quais tipos de food trucks podem ser encontrados perto de um local específico em um mapa. 🖥

> Link: <a href="https://github.com/uber-archive/coding-challenge-tools/blob/master/coding_challenge.md">Desafio Back-end Uber</a>

## Frameworks 👩🏿‍💻

- <a href="https://fastapi.tiangolo.com/">FastAPI</a>
- <a href="https://www.uvicorn.org/">Uvicorn</a>
- <a href="https://docs.pytest.org/en/stable/">PyTest</a>
- <a href="https://pypi.org/project/slowapi/">SlowAPI</a>
- Entre outros...

## Design de Arquitetura

<img src="/.github/arquitetura.svg" width=1000px>

## Funcionalidades 🔧

- **@AuthService**: Verificação de `HEADER AUTHORIZATION` com Bearer Token.
- **@FoodTrucksService**: Função para verificar status do serviço externo de FoodTrucks, atrelado a todos endpoints.
- **Rate Limiting**: Limitação de taxa para endpoints, configurado para `60/minutes`.
- **Testes Unitários**: Detecção de possíveis injeções inesperadas nos endpoints.

## Endpoints

- GET `/foodTrucks/`: Retorna todos os foodTrucks de San Francisco.

  Output:

  ```
      {
          "objectid": "1738240",
          "applicant": "Zuri Food Facilities",
          "facilitytype": "Truck",
          "cnn": "141000",
          "locationdescription": "02ND ST: STILLMAN ST to BRYANT ST (454 - 499)",
          "address": "490 02ND ST",
          "blocklot": "3763007",
          "block": "3763",
          "lot": "007",
          "permit": "23MFF-00035",
          "status": "APPROVED",
          "fooditems": "Peruvian Food Served Hot",
          "x": "6014337.512",
          "y": "2113125.58",
          "latitude": "37.783046099749996",
          "longitude": "-122.39406659922962",
          ...
      },
  ```

---

- POST `/foodTrucks/food`: Retorna food trucks com base em um tipo de comida especificado.

  ```
  {"food_type": "tacos"}
  ```

  Output:

  ```
  {
      "status": "success",
      "data": [
          {
              "objectid": "1735062",
              "applicant": "Bay Area Mobile Catering, Inc. dba. Taqueria Angelica's",
              "facilitytype": "Truck",
              "cnn": "1428000",
              "locationdescription": "25TH ST: ALABAMA ST to HARRISON ST (3042 - 3099)",
              "address": "3065 25TH ST",
              "blocklot": "4271038",
              "block": "4271",
              "lot": "038",
              "permit": "23MFF-00032",
              "status": "APPROVED",
              "fooditems": "Tacos: burritos: soda & juice",
              "x": "6009084.78",
              "y": "2101536.437",
              "latitude": "37.7509316476402",
              "longitude": "-122.4114199662057",
              ...
      },

  ```

---

- POST `/foodTrucks/nearest`: Retorna food trucks mais próximo do usuário com base na latitude e longitude.

  ```
  {
      "latitude": "37.49155786415492",
      "longitude": "-122.39167149978557"
  }
  ```

  Output:

  ```
  {
      "status": "success",
      "data": {
          "truck": {
              "applicant": "Quan Catering",
              "address": "BAY SHORE BLVD: VISITACION AVE to SUNNYDALE AVE (2501 - 2599) -- EAST --",
              "latitude": 37.70937546400143,
              "longitude": -122.40415437850858,
              "fooditems": "Cold Truck: Soft drinks: cup cakes: potato chips: cookies: gum: sandwiches (hot & cold): peanuts: muffins: coff (hot & cold): water: juice: yoplait: milk: orange juice: sunflower seeds: can foods: burritos: buscuits: chimichangas: rice krispies"
          }
      },
      "timestamp": "2024-08-18T18:25:56.340600"
  }

  ```

## Instalação 📂

Siga estes passos para instalar e configurar o projeto:

1. Clone o repositório:
   ```bash
   git clone https://github.com/usuario/repo.git
   ```
2. Inicie a API usando uvicorn, reload neste caso está ativado pois está fora de produção.
   ```console
   uvicorn app.main:app --reload
   ```

## License 📘

This project is under license. See the [LICENSE](LICENSE) file for more details.
