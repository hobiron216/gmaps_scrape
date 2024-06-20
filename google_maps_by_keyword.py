import json
import sys
import os
import requests
import livepopulartimes
import datetime

def scrape(keyword, languange, category, lat, long ):
    page = -20
    # keyword = "bar di taiwan"
    # languange = "id"

    all_data = []


    def get_review(code):
        headers = {
            'accept': '*/*',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6',
            # 'cookie': 'HSID=A0DF4YICeKMsBe85p; SSID=Ao-XG3fUlR8yOPhMd; APISID=JqKd6btMHQHMtM1X/ASP-ujPhN7bsVFmW5; SAPISID=DRRD0AqsfVZJg6bq/AhXEHNf9KQwNSNHVA; __Secure-1PAPISID=DRRD0AqsfVZJg6bq/AhXEHNf9KQwNSNHVA; __Secure-3PAPISID=DRRD0AqsfVZJg6bq/AhXEHNf9KQwNSNHVA; SEARCH_SAMESITE=CgQIlZsB; __Secure-ENID=19.SE=Q7u9GB1lZ1OXdO9YpVHHucZUxgl3ITUxBfIWoI2h-_C_VXMqjYpvN0T4cYbY4JVI8eAevRqEW-gftz4Kyqg_dmsjai2Gr2oi5ulkGGW_dKcahJn7FvrLggJUhYby_ltKqc8i4ayBOHu8esRpgeriYCkwbsB29TMf8E3cBgkDVAMqxny1RsqxND_5VlrAj7W1cWC7hUe2OEj6R-mCwgkgMVKhZ_1rO7_O1xEAuZ0Rc-mhcWHBUDaljgEjgIlIXb7xB1iSiFXqiUUPxuAxjEGqniOKaeE; receive-cookie-deprecation=1; SID=g.a000kQjZRtRd8icUzl4rXy7-2IDoEXcGIibf3Q1FWKxn7VZ-0pSwZdaofHPwnJCuAkp4q_2lhwACgYKAb8SARQSFQHGX2Mi1CEgyr6Pno9PyGPY6iXWEBoVAUF8yKrcLmcRonS96kNMP-04eu1g0076; __Secure-1PSID=g.a000kQjZRtRd8icUzl4rXy7-2IDoEXcGIibf3Q1FWKxn7VZ-0pSwt9jIEVPLEcbeBw7ycjrsqAACgYKATESARQSFQHGX2MimTLcV35wZLbk3aEZ4E44VxoVAUF8yKoVMyDpvpFSmpfiTw-WmOpo0076; __Secure-3PSID=g.a000kQjZRtRd8icUzl4rXy7-2IDoEXcGIibf3Q1FWKxn7VZ-0pSwmPVHsVUzkwnNJza9SG9g3AACgYKAfsSARQSFQHGX2Mi_C-dQ2LyIhGumAv3KBs8oBoVAUF8yKrNi0kdNOiHp6BwkKoqjqaj0076; OGPC=19031986-1:; AEC=AQTF6HwPJ4JJrvd8oqdMoQfIxrWTMGAxnGoc1ZpiQSmj7VH2nMkNb5AupPk; NID=515=HjucS_FV4o5UIOVTDRGqYPPRwTtnLzMJMArrmIcPdLYbkRO0yvbD6oezF0f6mLmd2mlHrplpYrpf024VgNZ5EmwehfTcZFKMjD-lDtL4BzBswgOEa7AUpldsIReEK0ObQvdlZ7wp_nRE9SqxIeKozOnkUeiFReVkvXHb04wHxRoyI3G0MOVzEZV5fB5xhWwkt3d1WhS308bl3eAiIajd6B56nDA1cwuBTRRlY9oBmgCw4OvHclDI2rUWE5MtClHFrYPk2imR-xDRAmYnE91eZkc-o7Vorgb0oTkbbiEP4lenIFp_NS3InbMxtZOPXwqNXqHqz4MsL-jvZdXb5OEn5YSrah-GM9R57HRR26OJqVHPh3JMx_vtmkbv6pbHNpIwcarYcgn2IVv3xq_LulNmx13sm2iobvvlM5s6l7R7FNmQFfBf1xYAACZFXqsYmd1zyaqJkdSLdanveGe45a9ls2i-LCqfXOkEOxH-pSCDY_zXkJFbrIS6KTFZbvTUXXQ4gEFGjNAdwsI8PmoXp4MIqwqtH0E6_hQsRlDf-luefjjTq2Reqvtm_GAVHxrUdqZnDjMi; UULE=a+cm9sZTogMQpwcm9kdWNlcjogMTIKdGltZXN0YW1wOiAxNzE4NTEwMDExMzEyMDAwCmxhdGxuZyB7CiAgbGF0aXR1ZGVfZTc6IC02MTY0MzUxNAogIGxvbmdpdHVkZV9lNzogMTA2NTUyNjgzMAp9CnJhZGl1czogMTQ4MzgKcHJvdmVuYW5jZTogNgo=; __Secure-1PSIDTS=sidts-CjIB3EgAEv9i8gHlN2w-bIY2lWsU_ArXGYnGWmryuzrlehwleleLvkjruWhKkxFfhAttPhAA; __Secure-3PSIDTS=sidts-CjIB3EgAEv9i8gHlN2w-bIY2lWsU_ArXGYnGWmryuzrlehwleleLvkjruWhKkxFfhAttPhAA; 1P_JAR=2024-06-16-03; SIDCC=AKEyXzXMalesohGRWWJpthdvq_WeJjMWa-VFSKzMCm_dxADKTgcpjrTB9Pqm0qffsSV01DktIw; __Secure-1PSIDCC=AKEyXzUnRmKoRRAjT5H8MPP1hD5HRji13w_mY1uI2u1JiFMk4UAkgEVFRJF1Ou3lP7sZuTStcg; __Secure-3PSIDCC=AKEyXzWIvPdmcb5iwNxTzv-QG36x-JEmMFiCUOuHktETGCUhnjM7zLTqZYDl6ajXrgn6XxLm2-A',
            'priority': 'u=1, i',
            'referer': 'https://www.google.com/',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-full-version': '"125.0.6422.176"',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="125.0.6422.176", "Chromium";v="125.0.6422.176", "Not.A/Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-ch-ua-wow64': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'x-client-data': 'CIy2yQEIprbJAQipncoBCIbtygEIlaHLAQiFoM0BCLnIzQEI4YTOAQjhk84BCOmTzgEI8pvOAQiXnc4BCMadzgEIs5/OAQj/oM4BGPbJzQEY1+vNARihnc4B',
            'x-goog-ext-353267353-jspb': '[null,null,null,147535]',
            'x-maps-diversion-context-bin': 'CAE=',
        }


        response = requests.get(
            'https://www.google.com/maps/rpc/listugcposts?authuser=0&hl='+languange+'&gl='+languange+'&pb=!1m8!1s'+code+'!3s!6m4!4m1!1e1!4m1!1e3!9b0!2m2!1i10!2s!5m2!1s9mFuZp_1A4zAkPIP1aGWsAU!7e81!8m5!1b1!2b1!3b1!5b1!7b1!11m10!1e3!2e1!3sen!4sid!5m3!1s2024-06-16!3i1!4e3!6m1!1i2!13m1!1e1',
            headers=headers,
        )

        html = response.text.replace(")]}'", "").strip()
        json_data = json.loads(html)
        next_page = json_data[1].replace("==","%3D%3D")

        list_result = []
        for data in json_data[2]:
            # print(data)
            review_text = data[0][2][15][0][0].strip()
            review_rating = data[0][2][0][0]
            review_date_timestamp = int(data[0][1][2])
            review_date_formatted = str(datetime.datetime.fromtimestamp(review_date_timestamp / 1000000.0))
            review_name = data[0][1][4][0][4]
            review_photo = data[0][1][4][0][3]
            review_url = data[0][1][4][0][5]

            result = {
                "review_name": review_name,
                "review_photo": review_photo,
                "review_url": review_url,
                "review_rating": review_rating,
                "review_date_timestamp": review_date_timestamp,
                "review_date_formatted": review_date_formatted,
                "review_text": review_text
            }

            list_result.append(result)

        # next page
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'SEARCH_SAMESITE=CgQIl5sB; receive-cookie-deprecation=1; __Secure-BUCKET=CNID; SID=g.a000kQgNd_rwWR4Ed6m51ROwLImP1EbCgIwn97EyJdAWvmPDzbDjfaVGk6HTFIkZcBix9FuHNAACgYKAc8SAQASFQHGX2Mi8MQ9wCwuW0K7gfsArpYHfxoVAUF8yKoUEGSaJpugw3y-dyfICX7B0076; __Secure-1PSID=g.a000kQgNd_rwWR4Ed6m51ROwLImP1EbCgIwn97EyJdAWvmPDzbDjGPtA1FfwBOOuvsWy6MI4aQACgYKAVYSAQASFQHGX2MirP9Ha5w7khPaKY1xjWnHvxoVAUF8yKpo_qoomuEJx_pHGtHCuXbT0076; __Secure-3PSID=g.a000kQgNd_rwWR4Ed6m51ROwLImP1EbCgIwn97EyJdAWvmPDzbDjRaxeU7fhWy_DePLgYMxvagACgYKAdMSAQASFQHGX2MirDUqVwGPvuvJdBBZvW-R2hoVAUF8yKrVuZySj7Rekfndwvg6LlM-0076; HSID=ATCUy65NgJRJR6HSM; SSID=Ax0m7MKG0ZUpHjBqt; APISID=A4xkuv0zWuUNXX8y/AnmmszWKfzBlWkjQP; SAPISID=St5xHqKYikjWP_jD/AYa2-8HiDNTjcxIoX; __Secure-1PAPISID=St5xHqKYikjWP_jD/AYa2-8HiDNTjcxIoX; __Secure-3PAPISID=St5xHqKYikjWP_jD/AYa2-8HiDNTjcxIoX; OGPC=19031986-1:; AEC=AQTF6Hw-CPoNUqCD5SoV_v1JEFH61kJgsf-99GmIG7jkljDAnxKUz6VLbA; NID=515=cRA3v3xFkTqSr9j0QgCA_lmqVpC8u76KL-zzQZUtib7fGjg5rGi-YUsX4Ae_AWnCc5jazKete0_xv81xn3upYTUhU7JVsprY7qEyiucdMRFuC-V7GCZPcq8jL91GUTUKRhUt6jXREiCT7OZ5k_jfM_mlRch1-z0009Wu_y1xmfpuEaigYMBp1wjhbic2AN4y7VCNbDPDAOTD8EcZkk6bxadHKfSTX19E2Pal0Hlml9lMjx64G1Gyuf141-imfI7Ke80KNd5y0gjCDLI2j-t411-iedztiLXJ69zIL-_wRL3X3pjBwOaWawj9sHwXJpj4OOBOm4BURxywlme95Bm3efGvTnWyNqp5nrvsG0K4fHd4urDhSeyGr5FXMwJ8OxyJbk3VkAa_P-3jJ0ri80lO0IlLrfvMWkycWbva9fr8q-YUgYj9Ar_kQ1BfWTXiA_0hzxk3; OTZ=7604817_28_28__28_; 1P_JAR=2024-06-17-04; __Secure-1PSIDTS=sidts-CjAB3EgAEkFpYHOE38feMpj5MAEeBbRiVMscwiiuZs3iViRCGtnPzy_NbmgLunyVVSEQAA; __Secure-3PSIDTS=sidts-CjAB3EgAEkFpYHOE38feMpj5MAEeBbRiVMscwiiuZs3iViRCGtnPzy_NbmgLunyVVSEQAA; SIDCC=AKEyXzWjs1jilUtP2Ss2XzH6_ra8BUkissp71fiWqEbL5O5kNg9BOadRccFLD8CrFsI0gWwl2A; __Secure-1PSIDCC=AKEyXzUOt0Y5fLBUd7JMnXinOtd3qHqyJys66vtxnLDdEVYq9NYu-u4ckvIcCB6v3VsBF53HzBg; __Secure-3PSIDCC=AKEyXzXY1fkdyKrF1VlnaLOSHf7VP1KjtvEq8fZWzzaRyhlVbqvm9TyROfaDIA9cDH1bWNp5PA',
            'priority': 'u=1, i',
            'referer': 'https://www.google.com/',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-full-version': '"125.0.6422.176"',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="125.0.6422.176", "Chromium";v="125.0.6422.176", "Not.A/Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-ch-ua-wow64': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'x-client-data': 'CIm2yQEIprbJAQipncoBCNv2ygEIk6HLAQiSossBCIWgzQEIvYXOAQjik84BCOmTzgEIv5fOAQjjl84BCO6bzgEIlJ3OAQizn84BCNWgzgEY9snNARjW680BGKCdzgE=',
            'x-goog-ext-353267353-jspb': '[null,null,null,147535]',
            'x-maps-diversion-context-bin': 'CAE=',
        }

        response = requests.get(
            'https://www.google.com/maps/rpc/listugcposts?authuser=0&hl='+languange+'&gl='+languange+'&pb=!1m8!1s0x2e69f4044e5995a7%3A0x4c9df8f41001aadb!3s!6m4!4m1!1e1!4m1!1e3!9b0!2m2!1i10!2s'+next_page+'!5m2!1sAp5vZrHiJrOL4-EP_b2owAo!7e81!8m5!1b1!2b1!3b1!5b1!7b1!11m6!1e3!2e1!3sid!4sid!6m1!1i2!13m1!1e1',
            headers=headers,
        )
        html = response.text.replace(")]}'", "").strip()
        json_data = json.loads(html)


        for data in json_data[2]:
            # print(data)
            review_text = data[0][2][15][0][0].strip()
            review_rating = data[0][2][0][0]
            review_date_timestamp = int(data[0][1][2])
            review_date_formatted = str(datetime.datetime.fromtimestamp(review_date_timestamp / 1000000.0))
            review_name = data[0][1][4][0][4]
            review_photo = data[0][1][4][0][3]
            review_url = data[0][1][4][0][5]

            result = {
                "review_name": review_name,
                "review_photo": review_photo,
                "review_url": review_url,
                "review_rating": review_rating,
                "review_date_timestamp": review_date_timestamp,
                "review_date_formatted": review_date_formatted,
                "review_text": review_text
            }

            list_result.append(result)

        return list_result
    def get_photo(code, image):

        headers = {
            'accept': '*/*',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6',
            # 'cookie': 'HSID=A0DF4YICeKMsBe85p; SSID=Ao-XG3fUlR8yOPhMd; APISID=JqKd6btMHQHMtM1X/ASP-ujPhN7bsVFmW5; SAPISID=DRRD0AqsfVZJg6bq/AhXEHNf9KQwNSNHVA; __Secure-1PAPISID=DRRD0AqsfVZJg6bq/AhXEHNf9KQwNSNHVA; __Secure-3PAPISID=DRRD0AqsfVZJg6bq/AhXEHNf9KQwNSNHVA; SEARCH_SAMESITE=CgQIlZsB; __Secure-ENID=19.SE=Q7u9GB1lZ1OXdO9YpVHHucZUxgl3ITUxBfIWoI2h-_C_VXMqjYpvN0T4cYbY4JVI8eAevRqEW-gftz4Kyqg_dmsjai2Gr2oi5ulkGGW_dKcahJn7FvrLggJUhYby_ltKqc8i4ayBOHu8esRpgeriYCkwbsB29TMf8E3cBgkDVAMqxny1RsqxND_5VlrAj7W1cWC7hUe2OEj6R-mCwgkgMVKhZ_1rO7_O1xEAuZ0Rc-mhcWHBUDaljgEjgIlIXb7xB1iSiFXqiUUPxuAxjEGqniOKaeE; receive-cookie-deprecation=1; SID=g.a000kQjZRtRd8icUzl4rXy7-2IDoEXcGIibf3Q1FWKxn7VZ-0pSwZdaofHPwnJCuAkp4q_2lhwACgYKAb8SARQSFQHGX2Mi1CEgyr6Pno9PyGPY6iXWEBoVAUF8yKrcLmcRonS96kNMP-04eu1g0076; __Secure-1PSID=g.a000kQjZRtRd8icUzl4rXy7-2IDoEXcGIibf3Q1FWKxn7VZ-0pSwt9jIEVPLEcbeBw7ycjrsqAACgYKATESARQSFQHGX2MimTLcV35wZLbk3aEZ4E44VxoVAUF8yKoVMyDpvpFSmpfiTw-WmOpo0076; __Secure-3PSID=g.a000kQjZRtRd8icUzl4rXy7-2IDoEXcGIibf3Q1FWKxn7VZ-0pSwmPVHsVUzkwnNJza9SG9g3AACgYKAfsSARQSFQHGX2Mi_C-dQ2LyIhGumAv3KBs8oBoVAUF8yKrNi0kdNOiHp6BwkKoqjqaj0076; OGPC=19031986-1:; AEC=AQTF6Hwa9ORM0mmZ4z4ZbwEs1vR6tB550jJDs4uLYsRtdxe2HM5JVS0MKHE; NID=515=FAEPnDje5SwUaHkKV6zgQzXsnIJ8wZ2SS58FlMvVW6hJR6kIOoIy5okzbszqNCvAmhhqJFXpZOaHeV10wnJocZJTdvRKxUWzNOF_c973j0t0Dthf8ITLxqLhSGaj0VtHJ5K_6zUouofyhToszqDp0H5SQfNSUVyzVmbjR7N7Vk8ih0u4cSDJl4haC6qRSkGmgqRt-sxgX6kcYirCAn3xqohrEKdD_XgavvzUPZum2BMgO17O4v9QSWDBgJR8S5Esr8irNK__clbYyHDFDKq5TvLQ9EwHheOQONaMPlf6EvJadY8_yFnad9Ozp-l7TsuetedUYeF44d0edUWbDB7QAWmE0fdJX-tbL5SrPmPXu5-Prw7Ft6KLpV2BsuyLG6NyI6Fvpl95AJ-vr4D4Niew7BBW_CZG-jrlylvxO7mp4Ngc0qZj_8l3YBovOGnL5O39NAESaWM8pqJHeR--EXjJ-RKxh4H8cK2Wan9XgwByyW7QtMMD_X-ei2vECC2QAV96H_ju1HQePlrRaQfltg5aKdcCJYQKiAhcg4NC8AM4KeasC_SYDoVRPx-F3F7kEndsdDXc; 1P_JAR=2024-06-20-09; __Secure-1PSIDTS=sidts-CjIB3EgAEvvMNBhmPa46j_Rg9n1ZPo6aNWoMahFVd1FTt4Do-2UaZ2ZZvMwH6dWtqi4WjxAA; __Secure-3PSIDTS=sidts-CjIB3EgAEvvMNBhmPa46j_Rg9n1ZPo6aNWoMahFVd1FTt4Do-2UaZ2ZZvMwH6dWtqi4WjxAA; UULE=a+cm9sZTogMQpwcm9kdWNlcjogMTIKdGltZXN0YW1wOiAxNzE4ODc2MTg5MjEzMDAwCmxhdGxuZyB7CiAgbGF0aXR1ZGVfZTc6IC02MTk5NzA1NgogIGxvbmdpdHVkZV9lNzogMTA2NzQ4MzEzNgp9CnJhZGl1czogMTAxOTAwOTYxNS41NTQzMDg5CnByb3ZlbmFuY2U6IDYK; SIDCC=AKEyXzW8Wtvrz56rNbca2ED6DAcSm36xR1SFcPkwh21oSu9LYqoKNoHv3pZu8HwcAm6ICJ94ag; __Secure-1PSIDCC=AKEyXzXZ-vTCIzJmEg5kN_uUEholaKp98qb-0ddLndf85Zks00Rjpznh6eSdBfzxoAzz7cniTA; __Secure-3PSIDCC=AKEyXzXK0_juFL7Jm8UZYlFRkvHtM4_hS8OOu3FfkE61Ee82XIB2Ps98bw6WL3fO-RKcmOmpDRY',
            'priority': 'u=1, i',
            'referer': 'https://www.google.com/',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-full-version': '"126.0.6478.62"',
            'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.62", "Google Chrome";v="126.0.6478.62"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-ch-ua-wow64': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'x-client-data': 'CIy2yQEIprbJAQipncoBCIbtygEIkqHLAQiFoM0BCLnIzQEI+o/OAQjhk84BCOmTzgEI5JvOAQjym84BCMadzgEIsJ7OAQiyn84BCP+gzgEY9snNARjX680BGKGdzgEY642lFw==',
            'x-goog-ext-353267353-jspb': '[null,null,null,147535]',
            'x-maps-diversion-context-bin': 'CAE=',
        }

        response = requests.get(
            'https://www.google.com/maps/rpc/photo/listentityphotos?authuser=0&hl='+languange+'&gl='+languange+'&pb=!1e2!3m3!1s'+code+'!9e0!11s%2Fg%2F11fl7tz9q9!5m50!2m2!1i203!2i100!3m2!2i20!5b1!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!6m3!1sY8RzZvor6IPj4Q_RmpLgBg!7e81!15i16698!16m4!1m1!1BCgIgARICEAE!2b1!4e1',
            headers=headers,
        )

        html = response.text.replace(")]}'", "").strip()
        json_data = json.loads(html)
        # print(json_data)

        for data in json_data[0]:
            image_url = data[6][0].replace("w203-h270-k-no", "s516-k-no")
            image.append(image_url)

        return image

    headers = {
        'authority': 'www.google.com',
        'accept': '*/*',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6',
        # 'cookie': 'SEARCH_SAMESITE=CgQIsZcB; __Secure-ENID=10.SE=mFgkRqluBg7ydmuCWnCl-ZnYNE_wv9FZgn_mO1mJ_jxSrsirF4w28jZAkFUV1TgCXJkprP6t1sjc3y6zR6bycks1D9Ox7BM3Oy-oOPsDOOT05o6YUwRzKzGpy2kebdjN2J5hYTH-nyo32hbmDUfZqjltc6Jbe5yvphOPuMb2aGh_9KqwcZzXJzWmPGUWhAfrTTS4PQeiNh-0cZHIonTa_Ay-P8IwGe3jVRNoaU25QzXq7E8PPS6SnvNh_F5i; OGPC=19033657-2:19033669-1:19033886-1:19022519-1:; SID=UwjZRkTBmeisWjFqopeKg57UgqVAmsVyqjaruyvV_l53S1BlECFCL8OOb6xojkHg3pGITQ.; __Secure-1PSID=UwjZRkTBmeisWjFqopeKg57UgqVAmsVyqjaruyvV_l53S1Bld4Wa6TZGziagxoWNhBaoGA.; __Secure-3PSID=UwjZRkTBmeisWjFqopeKg57UgqVAmsVyqjaruyvV_l53S1BlTWYSMx39sc2AHz5zouTmlQ.; HSID=A7EyqgjBg91SEC9pm; SSID=APVZ4vSiqOVzm9yBP; APISID=enarVCldd_KlrqIj/A-gBVw0z4w3OgwJyo; SAPISID=xqEh7n_dKLYH4sMb/A4Cgr4HMvk2VWtGTe; __Secure-1PAPISID=xqEh7n_dKLYH4sMb/A4Cgr4HMvk2VWtGTe; __Secure-3PAPISID=xqEh7n_dKLYH4sMb/A4Cgr4HMvk2VWtGTe; OTZ=6965527_28_28__28_; 1P_JAR=2023-04-01-03; AEC=AUEFqZduBumdDc-9xOqD9Uw8XSuxXSRTzv4GOFz17VctKgKbiXR1pFApbA; NID=511=XWThteGiyUL9TjVSzW7csAvfPNGRbyjm2WCmzqeDcDfmefyM2USLdTXP7znZnaiW459Saf7ZIX4DLUDXMYycSyFVTN9FA82RkH-JRYh6lc-XT3AeBikkaQ-A1iVNqmzmWHZLsrmyOt4p2i0x03bX3Ne0LLzpXBRWKHdTsXgPPN1RWJLxUE4UxuGcCiz04AtZBY_DfotSs-Dy2IxtwF7Fmx5OXnZIxoItWJbpnK4pCoxfH3UndHgAatpXqI1m5j2nTlPOt4uVcUadldh2BmuPRM0PEcyLI5dh27BduUq8gOJohjZH8ZCgXJDNQFzj2VlF-zGZT8BxpzqYGcoOGZT2fN8yW8yvcYTx7kbSdWYH0BoGX21h-1BbZu19equiVwUPIQ7wLVJL32eWF2bjqMN7hSqK1WbROmUJgCBleVw2kFpIi-gQ_uM4LCJjn1jsRrCqA4H2cMlaL4TS37wTuOv-CoFutV3pK8xK3myizTI9_JvpK85N79ZkNyNRGFCzzMzWEpYtgLe16kFJNlIfmmpA8fBOTPxfnhgeH3qRwTzy; DV=k43586wj0T5d4NvUndzzyhmNsSStcxge9TXKlwa5EAEAAGCqGssnH9E83QAAAFQ5Rwsg6qLjTgAAALwkxYOqKaGkFAAAAA; SIDCC=AFvIBn_8obCbO8PVgUBXgJCBM46JyYeQ9yHcKcMP_EPXoiWzkwp69vGelHu5iLPM-sOwD44jfWQ; __Secure-1PSIDCC=AFvIBn-wJWSKr2o5cF4nmV6_ARFKxPYddvSLYEqSW5Ye4R1mkYab35Rl4H4DhUVERe_PGUlzHw; __Secure-3PSIDCC=AFvIBn_SN4gB4CyIuTNMWsIgNJU5UZ85svhxhXzK9JA9pafEolS_wjjHcSkP5SwecisF0dDzz9Y',
        'referer': 'https://www.google.com/',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"111.0.5563.147"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="111.0.5563.147", "Not(A:Brand";v="8.0.0.0", "Chromium";v="111.0.5563.147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'x-client-data': 'CIy2yQEIprbJAQjEtskBCKmdygEI0KDKAQiG7coBCJKhywEI2P/MAQiFk80BCOKVzQEI4ZfNAQjjl80BCLiZzQEI6JvNAQjMnM0BCPeczQEIwJ/NAQjbn80BCO+fzQEIhaDNAQiVoc0B',
        'x-goog-ext-353267353-bin': 'IM+ACQ==',
        'x-maps-diversion-context-bin': 'CAE=',
    }


    while True:
        page+=20
        # if page >60:
        #     break
        if len(all_data)>100 :
            break
        print(page)
        response = requests.get(
            'https://www.google.com/search?tbm=map&authuser=0&hl='+languange+'&gl='+languange+'&pb=!4m8!1m3!1d126917.68788722652!2d'+long+'!3d'+lat+'!3m2!1i1024!2i768!4f13.1!7i20!8i' + str(page) + '!10b1!12m27!1m1!18b1!2m3!5m1!6e2!20e3!6m12!4b1!49b1!63m0!73m0!74i150000!75b1!85b1!89b1!91b1!110m0!114b1!149b1!10b1!14b1!16b1!17m1!3e1!20m2!5e2!6b1!19m4!2m3!1i360!2i120!4i8!20m57!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m2!1seqQnZLDaKtqI4-EPl6C4uAs!7e81!24m75!1m22!13m9!2b1!3b1!4b1!6i1!8b1!9b1!14b1!20b1!25b1!18m11!3b1!4b1!5b1!6b1!13b1!14b1!15b1!17b1!21b1!22b0!25b0!2b1!5m6!2b1!3b1!5b1!6b1!7b1!10b1!10m1!8e3!11m1!3e1!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!29b1!30m1!2b1!36b1!39m3!2m2!2i1!3i1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!71b1!72m4!1m2!3b1!5b1!4b1!89b1!103b1!113b1!26m4!2m3!1i80!2i92!4i8!30m28!1m6!1m2!1i0!2i0!2m2!1i458!2i768!1m6!1m2!1i974!2i0!2m2!1i1024!2i768!1m6!1m2!1i0!2i0!2m2!1i1024!2i20!1m6!1m2!1i0!2i748!2m2!1i1024!2i768!34m19!2b1!3b1!4b1!6b1!7b1!8m6!1b1!3b1!4b1!5b1!6b1!7b1!9b1!12b1!14b1!20b1!23b1!25b1!26b1!37m1!1e81!42b1!46m1!1e2!47m0!49m6!3b1!6m2!1b1!2b1!7m1!1e3!50m25!1m21!2m7!1u3!4sOpen+now!5e1!9s0ahUKEwjE0oes3of-AhVaxDgGHRcQDrcQ_KkBCPwFKBY!10m2!3m1!1e1!2m7!1u2!4sTop+rated!5e1!9s0ahUKEwjE0oes3of-AhVaxDgGHRcQDrcQ_KkBCP0FKBc!10m2!2m1!1e1!3m1!1u2!3m1!1u3!4BIAE!2e2!3m1!3b1!59BQ2dBd0Fn!67m3!7b1!10b1!14b0!69i640&q=' + keyword + '&tch=1&ech=2&psi=eqQnZLDaKtqI4-EPl6C4uAs.1680319611551.1&',
            # cookies=cookies,
            headers=headers,
        )
        html = response.text.replace('/*""*/','')

        json_data = json.loads(html)
        json_data = json.loads(str(json_data['d']).replace(")]}'",""))



        loop=0

        for data in json_data[0][1]:
            image_list = []
            place_name = ""
            operational_time_list = []
            # review20": ""
            category_result = ""
            # "link_menu": ""
            link_web = ""
            no_telp = ""
            popular_time = []
            review = ""
            facilities = []




            # "facilities": ""
            # loop+=1
            # if loop==1:
            #     continue

            try :
                if data[14]:

                    place_name = data[14][11]
                    alamat = data[14][39]
                    try :
                        no_telp = data[14][178][0][0]
                    except:
                        no_telp = ""
                    try :
                        rating = data[14][4][7]
                    except:
                        rating = 0
                    koordinat = str(data[14][9][2]) +"," + str(data[14][9][3])


                    try :
                        operational_times = data[14][34][1]
                        operational_time_list = []

                        for operational_time in operational_times:
                            data_time = operational_time[0] + " " + operational_time[1][0]
                            data_time = data_time.replace("\u202f", "")
                            try:
                                operational_time_list.append(data_time)
                            except:
                                continue
                    except:
                        pass

                    category_result = data[14][164][0][1]

                    if category not in category_result :
                        # print("sini")
                        continue
                    try :
                        link_web = data[14][7][0]
                    except:
                        pass


                    try :
                        popular_time = livepopulartimes.get_populartimes_by_formatted_address(place_name + ", " + data[14][2][0])['populartimes']
                    except:
                        pass
                    link_menu = "https://maps.google.com/?cid=" + data[14][37][0][0][29][1]

                    try :
                        review = get_review(data[14][10])
                    except:
                        review = ""


                    try:

                        image_list.append(data[14][72][0][1][6][0])
                    except Exception as e:
                        print(e)
                        pass


                    try:
                        image_list = get_photo(data[14][10], image_list)
                    except:
                        pass

                    try :
                        for facilities_data in data[14][100][1]:
                            facilities_name = facilities_data[1]
                            facilities_detail = []
                            for facilities_detail_data in facilities_data[2]:
                                facilities_detail.append(facilities_detail_data[1])


                            result_facility = {
                                "facilities_name" : facilities_name,
                                "facilities_detail" : facilities_detail
                            }
                            facilities.append(result_facility)
                    except:
                        pass

                    place_id = data[14][78]
                    result = {
                        "place_id" : place_id,
                        "keyword" : keyword,
                        "image": image_list,
                        "place_name" : place_name,
                        "operational_time" :operational_time_list,
                        "review" : review,
                        "category" : category_result,
                        "link_menu" : link_menu,
                        "link_web" : link_web,
                        "no_telp" : no_telp,
                        "popular_time" : popular_time,
                        "facilities" : facilities
                    }

                    all_data.append(result)


            except Exception as e:

                exc_type, exc_obj, exc_tb = sys.exc_info()

                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

                # print(exc_type, fname, exc_tb.tb_lineno)

                continue
        if (len(json_data[0][1]) == 1):
            break
    with open("data_google_"+ keyword +".json", 'w', encoding="utf-8") as outfile:
        json.dump(all_data,outfile,ensure_ascii=False, indent=4)

    return all_data