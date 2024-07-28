import aiohttp
from bs4 import BeautifulSoup
import asyncio

async def fetch_tercih_istatistikleri(program_id, year):
    if year not in [2021, 2022, 2023, 2024]:
        return {"error": "Invalid year. Only 2021, 2022, 2023 and 2024 are supported."}

    base_url = "https://yokatlas.yok.gov.tr"
    url_suffix = f"/{year}/content/lisans-dynamic/1080.php?y={program_id}" if year != 2024 else f"/content/lisans-dynamic/1080.php?y={program_id}"
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
    tables = soup.find_all('table', {'class': 'table table-bordered'})

    if len(tables) < 2:
        return {"error": "Required tables not found in the HTML content"}

    result = {
        'genel_istatistikler': {},
        'tercih_sira_dagilimi': []
    }

    # First table: General statistics
    rows = tables[0].find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 2:
            key = cols[0].get_text(strip=True)
            value = cols[1].get_text(strip=True)
            if len(cols) == 3:
                value = [value, cols[2].get_text(strip=True)]
            result['genel_istatistikler'][key] = value

    # Second table: Preference order distribution
    headers = [header.get_text(strip=True) for header in tables[1].find_all('th')]
    rows = tables[1].find_all('tr')
    for row in rows[1:]:  # Skip the header row
        cols = row.find_all('td')
        row_data = {}
        for i, header in enumerate(headers):
            value = cols[i].get_text(strip=True).replace('.', '') if header == 'Aday Sayısı' else cols[i].get_text(strip=True)
            row_data[header] = int(value) if header == 'Aday Sayısı' else value
        result['tercih_sira_dagilimi'].append(row_data)

    return result
