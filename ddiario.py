from ast import While
import csv
from urllib import request, response
import requests
import schedule
import time

# LINKS atualizado 30/04/2022

#https://www.gov.br/trabalho-e-previdencia/pt-br/composicao/orgaos-especificos/secretaria-de-trabalho/inspecao/areas-de-atuacao/cadastro_de_empregadores.csv
#https://servicos.ibama.gov.br/ctf/publico/areasembargadas/arquivos/areas_embargadas.csv
#https://www.gov.br/icmbio/pt-br/servicos/geoprocessamento/mapa-tematico-e-dados-geoestatisticos-das-unidades-de-conservacao-federais/Embargos_ICMBio_Atualizado_20042022.zip
#http://mapas.mma.gov.br/ms_tmp/ucstodas.shp
#https://certificacao.incra.gov.br/csv_shp/zip/%C3%81reas%20de%20Quilombolas.zip
#http://portal.iphan.gov.br/geoserver/SICG/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=SICG:sitios&maxFeatures=50000&outputFormat=SHAPE-ZIP




url = 'https://www.gov.br/trabalho-e-previdencia/pt-br/composicao/orgaos-especificos/secretaria-de-trabalho/inspecao/areas-de-atuacao/cadastro_de_empregadores.csv'
url2 = 'https://servicos.ibama.gov.br/ctf/publico/areasembargadas/arquivos/areas_embargadas.csv'
url3 = 'https://www.gov.br/icmbio/pt-br/servicos/geoprocessamento/mapa-tematico-e-dados-geoestatisticos-das-unidades-de-conservacao-federais/Embargos_ICMBio_Atualizado_20042022.zip'
url4= 'http://mapas.mma.gov.br/ms_tmp/ucstodas.shp'
url5= 'https://certificacao.incra.gov.br/csv_shp/zip/%C3%81reas%20de%20Quilombolas.zip'
url6= 'http://portal.iphan.gov.br/geoserver/SICG/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=SICG:sitios&maxFeatures=50000&outputFormat=SHAPE-ZIP'



def download():

 response_t_escravo_csv = requests.get(url)
 response_a_embargadas_csv = requests.get(url2, verify = False)
 response_embargosICMBIO_zip = requests.get(url3)
 response_uctodas_shp = requests.get(url4)
 response_quilombolas_zip = requests.get(url5, verify = False)
 response_terrasindigenas_zip = requests.get(url6)

 print('Download iniciado')

 with open('Trabalho_escravo.csv','wb') as f:
  f.write(response_t_escravo_csv.content)

 with open ('Areas_embargadas.csv','wb') as f:
  f.write(response_a_embargadas_csv.content) 

 with open ('Embargos_ICMBio_Atualizado_20042022.zip','wb') as f:
  f.write(response_embargosICMBIO_zip.content) 

 with open ('ucstodas.shp.csv','wb') as f:
  f.write(response_uctodas_shp.content) 

 with open ('Quilombolas.zip','wb') as f:
  f.write(response_quilombolas_zip.content) 

 with open ('Terras_idigenas.zip','wb') as f:
  f.write(response_terrasindigenas_zip.content) 
  

schedule.every().day.at("16:30").do(download)

while 1:
  schedule.run_pending()
  time.sleep(1)
  