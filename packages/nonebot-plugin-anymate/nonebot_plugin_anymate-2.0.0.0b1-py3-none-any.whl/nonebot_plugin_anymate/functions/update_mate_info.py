from ..api.api_operate import api_client
from ..config import Config
from ..sql_operate import SQL_Operate

from nonebot import get_plugin_config, on_command
from nonebot.adapters import Event
from nonebot.params import ArgStr

any_config = get_plugin_config(Config)

# 未完善，请勿使用！！会造成信息丢失
update_info = on_command("更新信息", aliases={"更新角色信息"}, priority=130)
tempId = None

@update_info.handle()
async def init(event: Event):
    user_id = event.get_user_id()


    mateId_list: list = await SQL_Operate.query_data_by_anything(
        any_config.db_dir, any_config.user_table_name, user_id, "mateId", "user_id"
    )
    if not mateId_list:
        await update_info.finish("未找到账号，请先使用/anylogin指令绑定账号")
       
    await update_info.send(f"共有{len(mateId_list)}个账户\nmateId: {str(mateId_list)}")
    await update_info.send("请输入需要修改信息的角色mateId")


@update_info.got("mateId")
async def get_mateId(event: Event, mateId: str = ArgStr()):
    tempId = mateId
    user_id = event.get_user_id()
    if tempId == "退出":
        await update_info.finish("已退出")
        
    user_id_list = await SQL_Operate.query_data_by_anything(
        any_config.db_dir,
        any_config.user_table_name,
        tempId,
        "user_id",
        "mateId",
    )
    if user_id_list[0] != user_id:
        await update_info.reject("mateId不存在!\n请重新输入:")
    await update_info.send("请输入要修改的姓名: ")

@update_info.got("name")
async def update_name(event: Event, name: str = ArgStr()):
    if name == "退出":
        await update_info.finish("已退出")
    cookies = {}
    token_list = await SQL_Operate.query_data_by_anything(
        any_config.db_dir,
        any_config.user_table_name,
        tempId,
        "XSRF_TOKEN",
        "mateId",
    )
    session_list = await SQL_Operate.query_data_by_anything(
        any_config.db_dir,
        any_config.user_table_name,
        tempId,
        "anymate_session",
        "mateId",
    )
    remember_key_list = await SQL_Operate.query_data_by_anything(
        any_config.db_dir,
        any_config.user_table_name,
        tempId,
        "remember_key",
        "mateId",
    )
    remember_web_list = await SQL_Operate.query_data_by_anything(
        any_config.db_dir,
        any_config.user_table_name,
        tempId,
        "remember_web",
        "mateId",
    )
    UUID_list: str = await SQL_Operate.query_data_by_anything(
        any_config.db_dir, any_config.user_table_name, tempId, "UUID", "mateId"
    )

    cookies["XSRF-TOKEN"] = token_list[0]
    cookies["anymate_session"] = session_list[0]
    cookies[remember_key_list[0]] = remember_web_list[0]

    # 通过remember更新token
    temp, new_cookies = await api_client.get_token_by_remember(cookies=cookies)

    result, new_cookies = await api_client.update_mate_info(name=name, UUID=UUID_list[0], cookies=new_cookies)

    if result["code"] != 200:
        await update_info.send(f"mateId: {tempId}\n信息修改出错！错误信息: {result}")
    else:
        await SQL_Operate.insert_or_update_user_data(
            db_dir=any_config.db_dir,
            table_name=any_config.user_table_name,
            token=new_cookies["XSRF-TOKEN"],
            session=new_cookies["anymate_session"],
            mateId=tempId,
        )
        await update_info.send(f"Anymate\nmateId: {tempId}\n名字修改 {name} 完成！")
