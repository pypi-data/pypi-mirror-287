import aiohttp
from bs4 import BeautifulSoup
import asyncio

async def fetch_ogrenim_durumu(program_id, year):
    if year not in [2021, 2022, 2023, 2024]:
        return {"error": "Invalid year. Only 2021, 2022, 2023 and 2024 are supported."}

    base_url = "https://yokatlas.yok.gov.tr"
    url_suffix = f"/{year}/content/onlisans-dynamic/3030a.php?y={program_id}" if year != 2024 else f"/content/onlisans-dynamic/3030a.php?y={program_id}"
    url = f"{base_url}{url_suffix}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=headers, ssl=False) as response:
                response.raise_for_status()
                html_content = await response.text()
        except aiohttp.ClientError as e:
            return {"error": f"Failed to fetch data from YOKATLAS: {str(e)}"}

    soup = BeautifulSoup(html_content.replace('---','0'), 'html.parser')
    table = soup.find('table', {'class': 'table table-bordered'})

    if not table:
        return {"error": "Table not found in the HTML content"}

    headers = [header.get_text(strip=True) for header in table.find_all('th')]
    rows = table.find('tbody').find_all('tr')

    result = []
    toplam = {}

    for row in rows:
        cols = row.find_all('td')
        row_data = {}
        for i, header in enumerate(headers):
            if i == 0:  # Öğrenim Durumu
                row_data['Öğrenim Durumu'] = cols[i].get_text(strip=True)
            elif i < len(cols):
                value = cols[i].get_text(strip=True).replace('%', '').replace(',', '.')
                if value == '---':
                    row_data[header] = None
                else:
                    try:
                        row_data[header] = float(value) if '.' in value else int(value)
                    except ValueError:
                        row_data[header] = value
        
        if row_data['Öğrenim Durumu'] == 'Toplam':
            toplam = row_data
        else:
            result.append(row_data)

    return {
        'ogrenim_durumu': result,
        'toplam': toplam
    }
