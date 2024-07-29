import aiohttp
from bs4 import BeautifulSoup
import asyncio

async def fetch_yerlesen_son_kisi_bilgileri(program_id, year):
    if year not in [2021, 2022, 2023, 2024]:
        return {"error": "Invalid year. Only 2021, 2022, 2023 and 2024 are supported."}

    base_url = "https://yokatlas.yok.gov.tr"
    url_suffix = f"/{year}/content/lisans-dynamic/1070.php?y={program_id}" if year != 2024 else f"/content/lisans-dynamic/1070.php?y={program_id}"
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

    result = {}
    rows = table.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        if len(cols) == 2:
            key = cols[0].get_text(strip=True).replace('*', '')
            value = cols[1].get_text(strip=True)

            if key in ["Yerleştiği Puan", "Ortaöğretim Başarı Puanı", "Diploma Notu"]:
                try:
                    value = float(value.replace(',', '.'))
                except ValueError:
                    pass
            elif key in ["Yerleştiği Başarı Sırası", "Liseden Mezuniyet Senesi"]:
                try:
                    value = int(value.replace('.', ''))
                except ValueError:
                    pass

            result[key] = value

    return result
