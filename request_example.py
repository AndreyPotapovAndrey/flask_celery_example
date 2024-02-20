import requests

with open('example/zhan_zhar.jpeg', 'rb') as f:
    image_1 = f.read()
    with open('example/valeri_nikolaev.jpg', 'rb') as f:
        image_2 = f.read()
        response = requests.post('http://127.0.0.1:5000/comparison/',
                                 files={'image_1': image_1,
                                        'image_2': image_2})
        print(response)

# resp = requests.post('http://127.0.0.1:5000/comparison', files={
#     'image_1': open('example/valeri_nikolaev.jpg', 'rb'),
#     'image_2': open('example/zhan_zhar.jpeg', 'rb')
# })
# resp_data = resp.json()
# print(resp_data)
# task_id = resp_data.get('task_id')
# print(task_id)
# #
#
#
# resp = requests.get(f'http://127.0.0.1:5000/comparison/{task_id}')
# print(resp.json())
# time.sleep(3)
#
# resp = requests.get(f'http://127.0.0.1:5000/comparison/{task_id}')
# print(resp.json())
