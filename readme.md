# FOSpider
Všechny studijní texty fyzikální olympiády (FO) společně se zadáními a řešeními úloh od školního roku 1997/1998 do současnosti.

## Popis
Studijní texty jsou volně dostupné na stránkách FO: http://fyzikalniolympiada.cz/studijni-texty. Skript `fotexts.py` nedělá nic jiného než že je všechny stáhne naráz. 

Každý text je uložen tak, aby výsledný soubor ve svém názvu nesl autory a správný titul (např.: zatímco ze stránek si stáhnete soubor `odpor.pdf`, skript jej uloží přehledněji jako `Šedivý, P. – Volf, I.: Pohyby tělesa v odporujícím prostředí.pdf`).

Druhý skript `foproblems.py` stáhne všechna zadání a řešení FO od roku 1997. 

## Závislosti
Skripty jsou napsané v Pythonu a používají knihovnu [Scrapy](https://scrapy.org/). 

### Instalace Scrapy
Například jako 

```python
pip install scrapy
```

## Spuštění skriptů

Pro stažení studijních textů zadejte do terminálu

```python
scrapy runspider fotexts.py
```

pro zadání a řešení úloh FO pak

```python
scrapy runspider foproblems.py
```

## Data v JSONu
Chcete-li si vytvořit knihovničku včetně odkazů, spusťte skript

```python
scrapy runspider fospider.py -o FO-texty.json -s FEED_EXPORT_ENCODING=utf-8
```
