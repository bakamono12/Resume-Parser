import requests


def test_api():
    url = 'http://127.0.0.1:5000/parse'  # Update the URL to match your Flask app route
    files = {'resume': ('ATS_classic_HR_resume.pdf', open('static/ATS_classic_HR_resume.pdf', 'rb'))}
    response = requests.post(url, files=files)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Error:", response.status_code)


if __name__ == '__main__':
    test_api()
