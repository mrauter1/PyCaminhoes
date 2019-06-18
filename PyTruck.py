import plotly.plotly as py
import plotly.graph_objs as go

import os
import htmlMedidor as hm

css = """
.container {
  display: flex;
}

h1 {
    color: #333;
    clear: both;
    font-family: Roboto;
    font-weight: 400;
    text-align: center;
}

table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 70%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}

.g1 {
  flex: 0 0 50%;
}

.g2 {
  flex: 1;
}
"""

def tabelaEntregas(entregas):
    htmlTable = '<table><tr><th>Cliente</th><th>Peso</th></tr>'
    for entrega in entregas:
        htmlTable= (htmlTable+'<tr>'
                    + '<td>'+entrega['cliente']+'</td>'
                    + '<td>'+entrega['peso']+'</td>'
                    '</tr>')

    htmlTable = htmlTable+'</table>'
    return htmlTable

entregas = [{'cliente': 'Cliente 1', 'peso': '200'}, {'cliente': 'Cliente 2', 'peso': '450'}]

htmlEntregas = tabelaEntregas(entregas)

html = '<html>\n<head>\n<style>'+css+'\n</style>\n</head>\n' \
       '<body>\n<section class="container">'
html = html+('<div align="center" class="grafico g1"><h1>Caminhão Serjão</h1>'
             '<br> Peso: 4500 KG de 5000 KG<br> Entregas: 8 de 10'
             +hm.fazHtmlMedidor(83)
             +htmlEntregas+
             '</div>')
html = html+('<div align="center" class="grafico g2"><h1>Caminhão Paulo</h1>'
             '<br> Peso: 7800 KG de 8000 KG<br> Entregas: 12 de 15'
             +hm.fazHtmlBarraHorizontal(43)
             +htmlEntregas+
             '</div>')
html = html+"\n</section></body>\n</html>"

filepath = r"F:\Sistemas.new\PyCaminhões\test.html"

text_file = open(filepath, "w")
text_file.write(html)
text_file.close()

print(html)

print(filepath)

os.system("start "+filepath)

#ploff.plot(fig, filename="F:\Sistemas.new\PyCaminhões\gauge-meter-chart.html")
