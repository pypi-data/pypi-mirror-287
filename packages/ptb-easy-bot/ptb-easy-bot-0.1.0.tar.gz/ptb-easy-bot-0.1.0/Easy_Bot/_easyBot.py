from telegram import Bot , InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import Application 
from telegram.ext import CommandHandler as COMMANDS
from telegram.ext import CallbackQueryHandler as CALLBACKS
from telegram.ext import InlineQueryHandler as INLINE_QUERY
from telegram.ext import MessageHandler  as MESSAGE_HANDLER
from telegram.ext import filters as Filters
from telegram._utils.defaultvalue import DEFAULT_80 ,DEFAULT_IP ,DEFAULT_NONE ,DEFAULT_TRUE ,DefaultValue
from telegram._utils.types import SCT, DVType, ODVInput
from typing import TYPE_CHECKING,Any,AsyncContextManager,Awaitable,Callable,Coroutine,DefaultDict,Dict,Generator,Generic,List,Mapping,NoReturn,Optional,Sequence,Set,Tuple,Type,TypeVar,Union

LOGO = """
........................................
.#####...####...##...##...####...#####..
.##..##.##..##..###.###..##..##..##..##.
.#####..######..##.#.##..##..##..##..##.
.##.....##..##..##...##..##..##..##..##.
.##.....##..##..##...##...####...#####..
........................................    
   ├ ᴄᴏᴘʏʀɪɢʜᴛ © 𝟸𝟶𝟸𝟹-𝟸𝟶𝟸𝟺 ᴘᴀᴍᴏᴅ ᴍᴀᴅᴜʙᴀsʜᴀɴᴀ. ᴀʟʟ ʀɪɢʜᴛs ʀᴇsᴇʀᴠᴇᴅ.
   ├ ʟɪᴄᴇɴsᴇᴅ ᴜɴᴅᴇʀ ᴛʜᴇ  ɢᴘʟ-𝟹.𝟶 ʟɪᴄᴇɴsᴇ.
   └ ʏᴏᴜ ᴍᴀʏ ɴᴏᴛ ᴜsᴇ ᴛʜɪs ғɪʟᴇ ᴇxᴄᴇᴘᴛ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴛʜᴇ ʟɪᴄᴇɴsᴇ.
"""

class Client():
    def __init__(
            self, 
            TOKEN: str, 
            PORT: DVType[int] = DEFAULT_80,
            WEBHOOK_URL:  Optional[str] = None,
            HANDLERS: Dict = {},
    ):
        self.token = TOKEN
        self.port = PORT
        self.webhook_url = WEBHOOK_URL
        self.handlers = HANDLERS
        self.app = Application.builder().token(self.token).build()

        for handler , command_and_function in self.handlers.items():
            handler_list = [] 
            for command , function in dict(command_and_function).items():
                if handler == "Error":
                    self.app.add_error_handler(function)
                elif command != None:
                    self.app.add_handler(handler(command , function))
                elif handler == MESSAGE_HANDLER:
                    self.app.add_handler(handler(command & ~Filters.COMMAND, function))
                else:    
                    self.app.add_handler(handler(function))
                handler_list.append(handler)


    def run_polling(
            self,
            drop_pending_updates:Optional[bool] = None,
            ):
        print(LOGO + "\n\n" )
        print("Bot Started")
        
        try:
            if self.webhook_url != None:
                print("running webhook...")
                self.app.run_webhook(
                    port=self.port,
                    listen="0.0.0.0",
                    webhook_url=self.webhook_url,
                    drop_pending_updates = drop_pending_updates,
                )
            else:
                print("running polling..")
                self.app.run_polling(
                    drop_pending_updates = drop_pending_updates,
                )
        except Exception as e:
            print(e)
        print("Bot Stoped")




    
