import asyncio
from aio_easycodefpy import Codef, ServiceType, encrypt_rsa

demo_client_id = ''
demo_client_secret = ''

client_id = ''
client_secret = ''

public_key = ''

async def main():
    # 비동기 컨텍스트 매니저 사용 가능
    async with Codef() as codef:
        codef.public_key = public_key

        # 데모 클라이언트 정보 설정
        # - 데모 서비스 가입 후 코드에프 홈페이지에 확인 가능(https://codef.io/#/account/keys)
        # - 데모 서비스로 상품 조회 요청시 필수 입력 항목
        codef.set_demo_client_info(demo_client_id, demo_client_secret)

        # 정식 클라이언트 정보 설정
        # - 정식 서비스 가입 후 코드에프 홈페이지에 확인 가능(https://codef.io/#/account/keys)
        # - 정식 서비스로 상품 조회 요청시 필수 입력 항목
        codef.set_client_info(client_id, client_secret)

        # 요청 파라미터 설정
        # - 계정관리 파라미터를 설정(https://developer.codef.io/cert/account/cid-overview)
        account_list = []
        account = {
            'countryCode':  'KR',
            'businessType': 'BK',
            'clientType':   'P',
            'organization': '0004',
            'loginType':    '1',
            'id':           "user_id",
        }

        # 비밀번호 설정
        pwd = encrypt_rsa("password", codef.public_key)
        account['password'] = pwd
        account_list.append(account)

        parameter = {
            'accountList': account_list,
        }

        # 요청
        res = await codef.create_account(ServiceType.SANDBOX, parameter)
        print(res)


asyncio.get_event_loop().run_until_complete(main())