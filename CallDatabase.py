from linebot.models import FlexSendMessage
import psycopg2
import os

def line_insert_record(record_list):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    table_columns = '(user_id, time_record, body_record)'
    postgres_insert_query = f"""INSERT INTO self_body {table_columns} VALUES (%s,%s,%s)"""

    cursor.executemany(postgres_insert_query, record_list)
    conn.commit()

    message = f"恭喜您！ {cursor.rowcount} 筆資料成功紀錄！"
    print(message)

    cursor.close()
    conn.close()
    
    return message


def database_search(user):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    
    postgres_select_query = f"""SELECT * FROM self_body WHERE user_id='{user}' ORDER BY record_no DESC;"""
    
    cursor.execute(postgres_select_query)
    raw = cursor.fetchmany(3)
    message = []
    
    for i in raw:
        message.append(str(i[2]))
        message.append(str(i[3]))
       
    message = str(message)

     
    cursor.close()
    conn.close()
    
    return message
flex_message = FlexSendMessage(
            alt_text='過去紀錄',
            contents={
                        "type": "carousel",
                        "contents": [
                            {
                            "type": "bubble",
                            "size": "nano",
                            "header": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "日期："+ message[0]
                                    "color": "#ffffff",
                                    "align": "start",
                                    "size": "md",
                                    "gravity": "center"
                                }
                                ],
                                "backgroundColor": "#27ACB2",
                                "paddingTop": "19px",
                                "paddingAll": "12px",
                                "paddingBottom": "16px"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "身體狀況："+ message[1]
                                        "color": "#8C8C8C",
                                        "size": "sm",
                                        "wrap": True
                                    }
                                    ],
                                    "flex": 1
                                }
                                ],
                                "spacing": "md",
                                "paddingAll": "12px"
                            },
                            "styles": {
                                "footer": {
                                "separator": False
                                }
                            }
                            },
                            {
                            "type": "bubble",
                            "size": "nano",
                            "header": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "日期："+ message[2]
                                    "color": "#ffffff",
                                    "align": "start",
                                    "size": "md",
                                    "gravity": "center"
                                }
                                ],
                                "backgroundColor": "#FF6B6E",
                                "paddingTop": "19px",
                                "paddingAll": "12px",
                                "paddingBottom": "16px"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "身體狀況："+ message[3]
                                        "color": "#8C8C8C",
                                        "size": "sm",
                                        "wrap": True
                                    }
                                    ],
                                    "flex": 1
                                }
                                ],
                                "spacing": "md",
                                "paddingAll": "12px"
                            },
                            "styles": {
                                "footer": {
                                "separator": False
                                }
                            }
                            },
                            {
                            "type": "bubble",
                            "size": "nano",
                            "header": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "日期："+ message[4]
                                    "color": "#ffffff",
                                    "align": "start",
                                    "size": "md",
                                    "gravity": "center"
                                }
                                ],
                                "backgroundColor": "#A17DF5",
                                "paddingTop": "19px",
                                "paddingAll": "12px",
                                "paddingBottom": "16px"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "身體狀況："+message[5]
                                        "color": "#8C8C8C",
                                        "size": "sm",
                                        "wrap": True
                                    }
                                    ],
                                    "flex": 1
                                }
                                ],
                                "spacing": "md",
                                "paddingAll": "12px"
                            },
                            "styles": {
                                "footer": {
                                "separator": False
                                }
                            }
                            }
                        ]
                        }
        )
        line_bot_api.reply_message(event.reply_token, flex_message)

