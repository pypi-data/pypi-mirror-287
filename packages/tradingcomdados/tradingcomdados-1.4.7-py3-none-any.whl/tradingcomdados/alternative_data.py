import pandas as pd
import requests 
import zipfile  
import numpy as np
import urllib.request
from pathlib import Path
from datetime import datetime,timedelta
import urllib3
import os
import wget
import re
import PyPDF2 as pyf
from PyPDF2 import PdfReader
import time
import shutil

#path = 'https://raw.githubusercontent.com/victorncg/financas_quantitativas/main/Data%20Extraction/Stock%20Exchange/Index%20Composition/'
#file = 'backend_index.py'

# DEACTIVETED FOR FIXING BUGS - JULY 11
#with urllib.request.urlopen(path + file) as response:
#    py_content = response.read().decode('utf-8')

#exec(py_content)


def _return_index(index:str):

    conversion = {'ibov':'eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjEyMCwiaW5kZXgiOiJJQk9WIiwic2VnbWVudCI6IjEifQ==',
                 'ibra':'QlJB',
                 'ifix': 'eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjEyMCwiaW5kZXgiOiJJRklYIiwic2VnbWVudCI6IjEifQ==',
                  'idiv': 'RElW'}

    # Desabilitar avisos de verificação SSL
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    # Configurar sessão para não verificar SSL
    session = requests.Session()
    session.verify = False
    
    # URLs
    url1 = 'https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay/'
    url2 = conversion[index] 
    
    # Fazer a requisição
    response = session.get(url1 + url2)
    
    # Verificar o status da resposta
    if response.status_code == 200:
        dados = pd.DataFrame(response.json()["results"])
    else:
        print(f"A biblioteca está funcionando mas houve erro na requisição a partir da B3, código: {response.status_code}")

    return dados


def _parse_ibov():

    try:

        url = "https://raw.githubusercontent.com/victorncg/financas_quantitativas/main/IBOV.csv"
        df = pd.read_csv(
            url, encoding="latin-1", sep="delimiter", header=None, engine="python"
        )
        df = pd.DataFrame(df[0].str.split(";").tolist())

        return df

    except:

        print("An error occurred while parsing data from IBOV.")



def _standardize_ibov():

    try:
        df = _parse_ibov()
        df.columns = list(df.iloc[1])
        df = df[2:][["Código", "Ação", "Tipo", "Qtde. Teórica", "Part. (%)"]]
        df.reset_index(drop=True, inplace=True)

        return df
    except:

        print("An error occurred while manipulating data from IBOV.")



def _standardize_sp500():
    """
    This function fetches the updated composition of the S&P 500 index. 
    
    Parameters
    ----------
    
    """

    table = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    df = table[0]

    return df



def _adapt_index(
    index: object, assets: object = "all", mode: object = "df"
):
    """
    This function processes the data from the latest composition of either IBOV or S&P 500. 
    
    Parameters
    ----------
    index : choose the index to be returned, if IBOV or S&P 500
    ativos : you can pass a list with the desired tickets. Default = 'all'.
    mode: you can return either the whole dataframe from B3, or just the list containing the tickers which compose IBOV. Default = 'df'.
    
    """

    if index == "sp500":

        df = _standardize_sp500()

        if assets != "all":
            df = df[df["Symbol"].isin(assets)]

        if mode == "list":
            df = list(df.Symbol)

    else:

        df = _return_index(index)

        if assets != "all":
            df = df[df["cod"].isin(assets)]

        if mode == "list":
            df = list(df.cod)
    
    return df



def index_composition(
    index: object, assets: object = "all", mode: object = "df"
):
    """
    This function captures the latest composition of either IBOV or S&P 500. It is updated every 4 months.
    
    Parameters
    ----------
    index : choose the index to be returned, if IBOV or S&P 500
    ativos : you can pass a list with the desired tickets. Default = 'all'.
    mode: you can return either the whole dataframe from B3, or just the list containing the tickers which compose IBOV. Default = 'df'.
    
    """

    df = _adapt_index(index, assets, mode)

    return df
    
# Functions to extract data from Boletim Diário B3:
def get_previous_weekday():
    today = datetime.now()
    """
    Description:
    It Calculates the previous weekday date relative to the current date. 
    If the previous day is a weekend day, it returns the date of the previous Friday
    ---------------------------------------------------------------------------------------
    Returns:
    - str: A string representing the date of the previous weekday in the format 'YYYY-MM-DD'.  
    """
    
    previous_day = today - timedelta(days=1)
    
    if previous_day.weekday() >= 5 or previous_day.weekday() == 0:  
        days_to_friday = (previous_day.weekday() - 4) % 7  
        previous_day -= timedelta(days=days_to_friday)
    previous_day_str = previous_day.strftime('%Y-%m-%d')
    
    return previous_day_str


def Dir(directory_name):
    """
    Description:
    This function creates a save directory if it does not alredy exist. 
    -----------------------------------------------------------------
    Parameters:
    - directory_name (str): a string name of the directory to be created.
    -----------------------------------------------------------------
    Returns:
    - str: Name of the directory that was created or already exists.

    If the directory already exists, this function does nothing and returns 
    the name of the existing directory.
    """   
    if Path(directory_name).exists() is False:
        Path(directory_name).mkdir() 
    return directory_name


def DownloadFile(directory_name, file_name, url):
    """
    Description:
    Download a file from a given URL and save it in the specified directory
    ---------------------------------------------------------------------------
    Parameters:
    - directory_name (str): Name of the directory where the file will be saved.
    - url (str): URL of the file to download.
    ---------------------------------------------------------------------------
    Returns:
    - Path: If the download is successful (status code 200), the function saves the file 
            in the specified directory and returns the Path object of the saved file.      
    """   
    
    directory_name = f'{directory_name}/'
    download = requests.get(url)
    
    if download.status_code == 200:
        path = Path.cwd()
        file_path = path / Path(directory_name+ file_name)
        
        with open(file_path, "wb") as dataset_B3:
            dataset_B3.write(download.content)
        return file_path 
    else:
        return (f'Failed download: file not found')  

def ExtractData(file_path, referencias):
    """
    Description:
    Extract text data from specific pages of a PDF file based on given references.
    ------------------------------------------------------------------------------------
    Parameters:
    - file_path (str or Path): Path to the PDF file from which data will be extracted.
    - referencias (list of str): List of strings representing keywords 
    or references to locate in the PDF. 
    ------------------------------------------------------------------------------------
    Returns:
    - str: Extracted text data from the pages containing the references.

    This function reads the specified PDF file at 'file_path' and searches for pages 
    containing any of the given 'referencias' keywords. It extracts and concatenates 
    text from these pages into a single string ('texto_total') and returns it.
    
    If no references are found or if there are issues reading the file, an empty 
    string is returned.
    """
    #Pasta com os arquivos PDF:
    file_pdf = pyf.PdfReader(file_path)
    #Abrir arquivos:
    #for i, arquivo in enumerate (caminho.iterdir()):
        #file = arquivo
        #file_pdf = pyf.PdfReader(file)
    
        #Iterar páginas do arquivo para encontrar em que páginas estão as palavras de ref:
    indice_paginas = []
    
    for palavra in referencias:
        for indice, pagina in enumerate(file_pdf.pages):
            texto_pagina = pagina.extract_text()
            if palavra in texto_pagina:
                if indice not in indice_paginas:
                    indice_paginas.append(indice)
                break 
                    
    all_text = ''
    for index in range(indice_paginas[0],indice_paginas[-1]+1):
        page = file_pdf.pages[index]
        text = page.extract_text()
        if text !=all_text:
            all_text +=text
            
    inicio_texto = all_text.find(referencias[0])
    final_texto = all_text.find(referencias[-1], inicio_texto+1)
    
    texto_total = all_text[inicio_texto:final_texto]
            
    return texto_total

def FormatSymbolData(texto_total):
    """
    Description:
    It Extracts and formats the symbol, company name, and type data 
    from a single string text ('texto_total') using regex pattern matching.
    ----------------------------------------------------------------------------------------------------
    Parameters:
    - texto_total (str): Text containing information to be formatted.
    -----------------------------------------------------------------------------------------------------
    Returns:
    - pandas.DataFrame: DataFrame with columns 'symbol', 'company', and 'type' extracted from texto_total.

    This function applies a regex pattern to extract data from 'texto_total' based on the following format:
    - Symbol: A word of exactly 4 letters followed by one or more digits.
    - Company: Any text following the symbol until it encounters a word that starts with:
      'DR', 'UNT', 'ON', 'PN', or 'CI'. 
    - Type: One of 'DR', 'UNT', 'ON', 'PN', or 'CI' optionally followed by additional characters.
    Notice that those characters represents the listed asset classes lised 

    The extracted data is structured into a pandas DataFrame with columns 'symbol', 'company', and 'type'.

    Example:
    If 'texto_total' contains:
    "PETR4 Petroleo Brasileiro DR ON ABCD1"

    The function will return a DataFrame:
    index  | ticker    |       company         |  type
    ---------------------------------------------------   
    0      | PETR4     |  Petroleo Brasileiro  |   DR
    ---------------------------------------------------
    """
    
    pattern = r'\b(\w{4}[1-9]+)\b\s+(.*?)\s+\b((?:DR|UNT|ON|PN|CI)\w{0,1})\b'

    matches = re.findall(pattern, texto_total)

    symbols = [match[0] for match in matches]
    companies = [match[1] for match in matches]
    B3_classes = [match[2] for match in matches]
        
    df = pd.DataFrame({'ticker': symbols,
                      'company': companies,
                      'type':B3_classes})
    return df


def get_B3Symbols():
    """
    Description:
    It fetches symbols of 'Lote Padrão' such as BDRs 'patrocinados listados', ETFs, and Stocks 
    from the latest BDI-03-2 PDF - Boletim diário file available on the B3 website.

    Steps:
    1. Retrieves the date of the previous weekday using the get_previous_weekday() function.
    2. Constructs the URL and file name for the BDI-03-2 PDF file based on the retrieved date.
    3. Creates a temporary directory using the Dir() function to store the downloaded PDF file.
    4. Downloads the BDI-03-2 PDF file from the B3 website using the DownloadFile() function.
    5. Extracts text data from the downloaded PDF file related to 'Lote Padrão'using the ExtractData() function.
    6. Formats the extracted data into a pandas DataFrame with columns 'symbol', 'company', and 'type' 
       using the FormatSymbolData() function.
    7. Deletes the temporary directory and its contents using shutil.rmtree() after processing is complete.

    ----------------------------------------------------------------------------------------------------
    Returns:
    - pandas.DataFrame: DataFrame with columns 'symbol', 'company', and 'type'.

    This function retrieves the latest available BDI-03-2 PDF file from the B3 website 
    for the previous weekday's date. It extracts symbols,company names, and types 
    related to 'Lote Padrão'from the Boletim diário PDF file, formats the data into a pandas DataFrame, 
    and returns it.

    Example:
    
    index  | ticker    |       company         |  type
    ---------------------------------------------------   
    0      | PETR4     |  Petroleo Brasileiro  |   DR
    ---------------------------------------------------
    """

    date = get_previous_weekday()
    
    file_name = f"BDI_03-2_{date.replace('-', '')}.pdf"
    url = f"http://arquivos.b3.com.br/bdi/download/bdi/{date}/{file_name}"
    
    directory_name = Dir('BDI_file')
    file_path = DownloadFile(directory_name, file_name, url)
    #Para lote padrão:
    referencias = ['Lote Padrão','Fundos Imobiliários']
    
    texto_total = ExtractData(file_path, referencias)
    df = FormatSymbolData(texto_total)
    #excluir arquivos:
    
    shutil.rmtree(directory_name)
    
    return df

# Functions to get  Classificação setorial B3: 
def download_ClassifSetorial(url_dataset):
    """
    Downloads and extracts a zip file from the provided URL.
    ------------------------------------------------------------------------
    Parameters:
    - url_dataset (str): URL pointing to the zip file to be downloaded.
    ------------------------------------------------------------------------
    Returns:
    - io.BytesIO: Bytes stream of the extracted file from the downloaded zip.
      named dataset. 
    """

    file = url_dataset.split('/')[-1]

    download = requests.get(url_dataset)
    with open(file, "wb") as dataset_B3:
        dataset_B3.write(download.content)
    arquivo_zip = zipfile.ZipFile(file)
    dataset = arquivo_zip.open(arquivo_zip.namelist()[0])
    return dataset


def B3Eng_DataProcessing(df):
    """
    Description:
    The function Processes and clean DataFrame containing B3 (Brazilian Stock Exchange) sectors data in english.
    --------------------------------------------------------------------------------------------------
    Parameters:
    - df (pandas.DataFrame): DataFrame containing B3 sectors data in english.
    -------------------------------------------------------------------------------------------------
    Returns:
    pandas.DataFrame: Processed DataFrame with renamed columns and cleaned data:
        - 'SECTORS': Economic sector.
        - 'SUBSECTORS': Subsector.
        - 'SEGMENTS': Segment.
        - 'NAME': Company name.
        - 'CODE': Ticker code.
        - 'SEGMENT B3': B3 listing segment such as 'ON', 'PN', 'UNIT' and 'DR'.    
    """
    
    df.rename(columns = {'LISTING': 'CODE', 'Unnamed: 4':'SEGMENT B3'}, inplace = True)
        
    df['NAME'] = df['SEGMENTS'].copy()
        
    df.dropna(subset = ['NAME'], inplace = True)
    indexNames = df[df['SECTORS'] == 'SECTORS'].index
    df.drop(indexNames, inplace=True)
        
    df['SEGMENTS'] = np.where(df['CODE'].isna(),df['NAME'],pd.NA )    
    df['SECTORS'] = df['SECTORS'].ffill()
    df['SUBSECTORS'] = df['SUBSECTORS'].ffill()
    df['SEGMENTS'] = df['SEGMENTS'].ffill()
    df.dropna(subset = ['CODE'], inplace = True)

    df.reset_index(drop=True, inplace=True)

    df = df[['SECTORS','SUBSECTORS','SEGMENTS','NAME','CODE','SEGMENT B3']]
    
    return df

def B3Pt_DataProcessing(df):
    """
    Description:
    Processes DataFrame containing B3 (Brazilian Stock Exchange) data in Portuguese.
    -------------------------------------------------------------------------------
    Parameters:
    - df (pandas.DataFrame): DataFrame containing B3 sectors data in portuguese.

    Returns:
    pandas.DataFrame: DataFrame : Processed DataFrame with renamed columns and cleaned data:
        - 'SETOR ECONÔMICO': Setor econômico.
        - 'SUBSETOR': Subsetor.
        - 'SEGMENTO': Nome ou código do segmento.
        - 'NOME NO PREGÃO': Nome da empresa.
        - 'CÓDIGO': Código da ação.
        - 'SEGMENTO B3': Segmento de listagem na B3.
    """
    
    df.rename(columns = {'LISTAGEM': 'CÓDIGO', 'Unnamed: 4':'SEGMENTO B3'}, inplace = True)
        
    df['NOME NO PREGÃO'] = df['SEGMENTO'].copy()
        
    df.dropna(subset = ['NOME NO PREGÃO'], inplace = True)
    indexNames = df[df['SETOR ECONÔMICO'] == 'SETOR ECONÔMICO'].index
    df.drop(indexNames, inplace=True)
        
    df['SEGMENTO'] = np.where(df['CÓDIGO'].isna(),df['NOME NO PREGÃO'],pd.NA )    
    df['SETOR ECONÔMICO'] = df['SETOR ECONÔMICO'].ffill()
    df['SUBSETOR'] = df['SUBSETOR'].ffill()
    df['SEGMENTO'] = df['SEGMENTO'].ffill()
    df.dropna(subset = ['CÓDIGO'], inplace = True)

    df.reset_index(drop=True, inplace=True)

    df = df[['SETOR ECONÔMICO','SUBSETOR','SEGMENTO','NOME NO PREGÃO','CÓDIGO','SEGMENTO B3']]
    
    return df
#Functions Us exchange
def request_nasdaq(url):
    headers = {
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Java-http-client/'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        return json_data

    else:
        print(f"Failed to retrieve data: {response.status_code}")

#
def get_sectors(stock_exchange: str, symbols: list = None, B3_language: str = None) -> pd.DataFrame:
    """
    Description: 
    It retrieves economic and activity sector classifications for companies listed 
    on NASDAQ, NYSE, AMEX, or the Brazilian stock exchange (B3).

    You can leave the 'symbols' parameter as None to return data for all companies, 
    or specify a list of specific symbols.
    ---------------------------------------------------------------------------------------
    Parameters:
    - stock_exchange (str): Code for the stock exchange ('NASDAQ', 'NYSE', 'AMEX', or 'B3').
    - symbols (list, optional): List of ticker symbols (e.g., symbols = ['AAPL', 'AMD']) 
      of specific companies to retrieve sector data for. 
    - B3_language (str, optional): Language option only for B3 data ('pt' for Portuguese, default is 'eng').
    -----------------------------------------------------------------------------------------
    Returns:
    pandas.DataFrame: DataFrame containing the following columns based on the stock exchange:
        - For B3 (Brazilian stock exchange):
            - 'sector' (pt: 'SETOR ECONÔMICO'): Economic sector of the company.
            - 'subsectors (pt: 'SUBSETOR'): Subsector of the company.
            - 'segments' (pt:'SEGMENTO'): Industry of the company.
            - 'name'(pt: 'NOME NO PREGÃO'): Company name.
            - 'ticker'(pt: 'ticker'): Ticker symbol with the ordinary or commom stock number.
            - 'SEGMENT B3'(pt: SEGMENTO B3'): Type of stock
           
        - For NASDAQ, NYSE, AMEX:
            - 'sector': Sector of the company.
            - 'industry': Industry of the company.
            - 'country': Country where the company is listed.
            - 'name': Company name.
            - 'symbol': Ticker symbol.
    """     
    try:
        stock_exchange = stock_exchange.upper()
          
        if stock_exchange == 'B3':
            pt_url = r"https://www.b3.com.br/data/files/57/E6/AA/A1/68C7781064456178AC094EA8/ClassifSetorial.zip"
            eng_url = r"http://www.b3.com.br/data/files/DB/57/3B/29/78C7781064456178AC094EA8/ClassifSetorial_i.zip"
           
            if B3_language is None:
                column = 'NAME'
                url_dataset = eng_url
                dataset = download_ClassifSetorial(url_dataset)
                df = pd.read_excel(dataset, header=6)
                df_sectors = B3Eng_DataProcessing(df)
                
            elif B3_language == 'pt':
                column = 'NOME NO PREGÃO'
                url_dataset = pt_url
                dataset = download_ClassifSetorial(url_dataset)
                df = pd.read_excel(dataset, header=6)
                df_sectors = B3Pt_DataProcessing(df)
    
     
            df_tickers = get_B3Symbols()
    
            df_tickers['company'] = df_tickers['company'].str.strip()
            df_sectors[column] = df_sectors[column].str.strip()
    
            df = df_tickers.merge(df_sectors, left_on='company', right_on=column)
    
            if B3_language is None:
                df = df[['SECTORS','SUBSECTORS','SEGMENTS','NAME','SEGMENT B3', 'ticker']]
    
            else:
                df = df[['SETOR ECONÔMICO','SUBSETOR','SEGMENTO','NOME NO PREGÃO','SEGMENTO B3','ticker']]
    
            if symbols is None:
                pass
        
            else:
                tickers = [ticker.upper() for ticker in symbols]
                df = df.loc[df['ticker'].isin(tickers)]
                df = df.reset_index(drop=True)
                existing_tickers = set(df['ticker'])
      
        elif stock_exchange in ['NASDAQ', 'NYSE', 'AMEX']: 
            url = f'https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=25&exchange={stock_exchange}&download=true'
        
            json_data = request_nasdaq(url)
        
            df = pd.DataFrame(json_data['data']['rows'])
            if B3_language is None or B3_language == 'eng':
                df = df[['sector', 'industry', 'country', 'name', 'symbol']]
            else:
                print('')
                print('`B3_language` is a parameter specific to the Brazilian Exchange. The data is not available in Portuguese.')
                print('')
                df = df[['sector', 'industry', 'country', 'name', 'symbol']]
                
            if symbols is None:
                pass
                
            else:
                tickers = [ticker.upper() for ticker in symbols]
                df = df.loc[df['symbol'].isin(tickers)]
                df = df.reset_index(drop=True)
                existing_tickers = set(df['symbol'])
        else:
            print(f'stock exchange {stock_exchange} is not available')
    
    
        if symbols is not None:
            input_tickers = set(tickers)
            non_existent_tickers = input_tickers - existing_tickers
            for ticker in non_existent_tickers:
                print(f"{ticker} not found")
            
        if df.empty:
            return None
        else:
            return df

    except Exception as e:
        print(f"An error occurred: {e}") 


# Define the function to fetch historical data
def get_historical_klines(symbol, interval, start_time, end_time=None):
    base_url = 'https://api.binance.com'
    endpoint = '/api/v3/klines'
    
    params = {
        'symbol': symbol,
        'interval': interval,
        'startTime': start_time,
    }
    
    if end_time:
        params['endTime'] = end_time
    
    response = requests.get(base_url + endpoint, params=params)
    data = response.json()
    
     # Convert data to DataFrame
    df = pd.DataFrame(data, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume', 
        'close_time', 'quote_asset_volume', 'number_of_trades', 
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
    ])
    
    # Convert timestamp to readable date
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    
    return df

def get_histdata_binance(symbol, interval, start_time, end_time):
    """
    This function returns Crypto Historical Data from Binance
    
    Parameters
    ----------
    symbol     : 'BTCUSDT'      - string format
    interval   : '1m' '5m' '1d' - string format
    start_time : '2024-01-01'   - '%Y-%m-%d' - string format
    end_time   : '2024-03-01'   - '%Y-%m-%d' - string format
    
    """
    all_data = []
    start_time = int((datetime.strptime(start_time, '%Y-%m-%d')).timestamp() *1000)
    end_time = int((datetime.strptime(end_time, '%Y-%m-%d')).timestamp() *1000)
    while start_time < end_time:
        df = get_historical_klines(symbol, interval, start_time, end_time)
        if df.empty:
            break
        all_data.append(df)
        start_time = int(df['timestamp'].iloc[-1].timestamp() * 1000) + 1  # move to the next interval
    
    return pd.concat(all_data)

def get_tick_b3(date):
    """
    This function extract Tick Data from B3 api for every Instrument traded in that given day.
    It returns and Pandas DataFrame

    Parameter
    ----------
    day : '2024-07-15'

    """
    url = 'https://arquivos.b3.com.br/apinegocios/tickercsv/'+ date
    file_name = str(date+'_B3_TickData.zip')
    wget.download(url,file_name)
    
    # Get the directory of the zip file
    zip_dir = os.path.dirname(file_name)
    
    # Create a ZipFile object
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        # Extract all the contents into the directory of the zip file
        zip_ref.extractall(zip_dir)
    print('/n')
    print("1/8 - Extracted all contents of ",file_name)
    
    # Read Extracted File
    folder_ref = os.getcwd()
    files = os.listdir(folder_ref)
    files_txt = [i for i in files if i.endswith('_NEGOCIOSAVISTA.txt')]
        
    df = pd.read_csv(files_txt[0], sep=";")

    # Update PrecoNegocio
    df['PrecoNegocio'] = df.PrecoNegocio.str.replace(",", ".").astype('float')
    print('2/8 - PrecoNegocio Updated')

    # Update Codigos Participantes
    df[['CodigoParticipanteComprador','CodigoParticipanteVendedor']] = df[['CodigoParticipanteComprador','CodigoParticipanteVendedor']].fillna(0)
    df[['CodigoParticipanteComprador','CodigoParticipanteVendedor']] = df[['CodigoParticipanteComprador','CodigoParticipanteVendedor']].astype('int').astype('str')
    print('3/8 - Codigos Participantes Updated')

    #Update Datetime
    # Ensure 'HoraFechamento' is a string and pad with leading zeros to ensure it's 9 characters long
    df['HoraFechamento'] = df['HoraFechamento'].astype(str).str.zfill(9)
    # Extract the hours, minutes, seconds, and milliseconds
    df['HoraFechamento'] = df['HoraFechamento'].apply(
        lambda x: f"{x[:2]}:{x[2:4]}:{x[4:6]}.{x[6:9]}"
    )
    # Ensure 'HoraFechamento' is a string
    df['HoraFechamento'] = df['HoraFechamento'].astype(str)
    # Convert the 'HoraFechamento' to datetime with the appropriate format including milliseconds
    df['HoraFechamento'] = pd.to_datetime(df['HoraFechamento'], format='%H:%M:%S.%f').dt.time
    print('4/8 - HoraFechamento Updated')

    #Create a New Index
    str1 = df.CodigoInstrumento
    str2 = df.CodigoIdentificadorNegocio.astype(str)
    str3 = df.DataReferencia.astype(str)
    str4 = df.HoraFechamento.astype(str)
    newindex = str1+'_'+str2+'_'+str3+'_'+str4
    df['Index'] = newindex
    # Set 'HoraFechamento' column as the index
    df = df.set_index('Index')
    print('5/8 - New_Index Created')

    # Remove a column inplace
    df.drop(columns=['AcaoAtualizacao','TipoSessaoPregao','DataNegocio'], inplace=True)
    print('6/8 - Columns Remove Updated')
    #Rename Columns
    dicionario = {'DataReferencia' : 'Dia', 'CodigoInstrumento' : 'Instrumento', 'PrecoNegocio' : 'Preco', 'QuantidadeNegociada' : 'Quantidade', 'HoraFechamento' : 'Hora', 'CodigoIdentificadorNegocio' : 'Cod_Negocio', 'CodigoParticipanteComprador' : 'Comprador', 'CodigoParticipanteVendedor' : 'Vendedor'}
    df.rename(dicionario, axis = 1, inplace=True)
    print('7/8 - Columns Rename Updated')
    #Reorder Columns
    new_order = ['Cod_Negocio', 'Instrumento', 'Dia', 'Hora','Preco','Quantidade','Comprador','Vendedor']
    df = df[new_order]
    print('(8/8 - Columns New Order Updated')
    print('Data Extraction and Transformation - Done')
    
    return df

