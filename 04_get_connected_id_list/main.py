import asyncio
from aio_easycodefpy import Codef, ServiceType

demo_client_id = ''
demo_client_secret = ''

client_id = ''
client_secret = ''

public_key = ''

# 코드에프 인스턴스 생성
async def main():
    codef = Codef()
    codef.public_key = public_key

    # 데모 클라이언트 정보 설정
    # - 데모 서비스 가입 후 코드에프 홈페이지에 확인 가능(https://codef.io/#/account/keys)
    # - 데모 서비스로 상품 조회 요청시 필수 입력 항목
    codef.set_demo_client_info(demo_client_id, demo_client_secret)

    # 정식 클라이언트 정보 설정
    # - 정식 서비스 가입 후 코드에프 홈페이지에 확인 가능(https://codef.io/#/account/keys)
    # - 정식 서비스로 상품 조회 요청시 필수 입력 항목
    codef.set_client_info(client_id, client_secret)

    # 요청
    res = await codef.get_connected_id_list(ServiceType.SANDBOX, None)
    print(res)

    await codef.close()


asyncio.get_event_loop().run_until_complete(main())