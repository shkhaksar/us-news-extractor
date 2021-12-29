import pyexcel as pe
import requests

if __name__ == "__main__":
    data = []

    base_url = 'https://www.usnews.com/best-graduate-schools/api/search?program=top-engineering-schools&specialty=mechanical-engineering&_sort=name-asc&_page={}'
    page = 1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

    for page in range(1, 20):
        url = base_url.format(page)
        r = requests.get(url, headers=headers)
        res = r.json()
        for i, item in enumerate(res.get('data').get('items')):
            data.append({
                'name': item.get('name'),
                'city': item.get('city'),
                'state': item.get('state'),
                'url': item.get('url'),
                'avg_quant_gre': item.get('schoolData').get('avg_quant_gre'),
                'c_mech_mean': item.get('schoolData').get('c_mech_mean'),
            })

    # save all the data as CSV
    sorted_data = sorted(data, key=lambda i: i['c_mech_mean'])
    sorted_data.reverse()
    pe.save_as(records=sorted_data, dest_file_name="universities.xls")
    pe.save_as(records=sorted_data, dest_file_name="universities.csv")
