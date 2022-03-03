# primeira-api-com-fastpi

### As instruções para rodar o projeto a seguir somente funcionam em windows, podendo mudar em outro SO.

## Ambientação:
Criando ambiente virtual:
* Abra o prompt de comando.
  * E execute os seguintes comandos:
  ``` python -m venv .primeira-api-com-fastapi ```
  ``` cd .\.primeira-api-com-fastapi\ ```
  ``` cd .\Scripts\ ```
  ``` activate.bat ```
  ``` cd .. ```
  ``` cd .. ```
  ``` pip install -r requiriments.txt ```

## Rodando a API:
``` uvicorn main:app --reload ```

## Observações:
* Toda nova biblioteca nova utilizada deve ter o nome de seu módulo colocado no arquivo requiriments.txt para que a ambientação seja simples em _deploy's_ futuros.
* É recomendado criar o ambiente virtual e escolhê-lo como interpretador dentro da IDE utilizada.

## Documentação:
Após rodar é possível verificar todos _endpoints_ no seguinte endereço ``` http://localhost:8000/docs ```, onde é apresentado via Swagger UI. 

## Considerações finais:
Este projeto foi construído em base em um vídeo do youtube (https://www.youtube.com/watch?v=bX5NrUWHqyo) de como criar uma API com FastAPI, pois estava estudando a possíbilidade de utilizá-la no trabalho.
Esta será incrementada conforme meus estudos sobre a Framework avançarem.
