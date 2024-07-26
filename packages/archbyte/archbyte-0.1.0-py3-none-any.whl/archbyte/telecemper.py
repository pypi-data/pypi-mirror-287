from telethon import TelegramClient, events
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import DeleteChatUserRequest, SendMessageRequest
from telethon.sessions import StringSession
from telethon.tl.types import Channel, Chat
import asyncio
import logging
from datetime import datetime
import random

class Telecemper:
    def __init__(self, api_id, api_hash, phone_number, session_string=None):
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone_number = phone_number
        self.client = None
        self.session_string = session_string
        self.leave_log = []
        self.join_log = []
        self.activity_log = []
        self.loop = asyncio.get_event_loop()
        self.spam_keywords = [
            'free giveaway', 'limited offer', 'act now', 'exclusive deal',
            'earn money fast', 'get rich quick', 'investment opportunity',
            'lottery winner', 'unclaimed funds', 'miracle cure'
        ]
    
    async def init_client(self):
        if self.client is None:
            self.client = TelegramClient(StringSession(self.session_string), self.api_id, self.api_hash)
            await self.client.connect()

    async def get_code(self):
        await self.init_client()
        await self.client.send_code_request(self.phone_number)
        return "Verification code sent. Please check your Telegram app."

    async def submit_code(self, code):
        try:
            await self.client.sign_in(phone=self.phone_number, code=code)
            self.session_string = self.client.session.save()
            await self.setup_event_handler()
            return "Code submitted. Bot is now running.", self.session_string
        except Exception as e:
            logging.error(f"Error submitting code: {e}")
            return f"Error submitting code: {str(e)}", None

    async def login_with_session(self):
        try:
            await self.init_client()
            if await self.client.is_user_authorized():
                await self.setup_event_handler()
                return "Logged in successfully with session string."
            else:
                return "Failed to log in with session string."
        except Exception as e:
            logging.error(f"Error logging in with session string: {e}")
            return f"Error logging in with session string: {str(e)}"

    async def setup_event_handler(self):
        @self.client.on(events.NewMessage())
        async def check_spam(event):
            if event.is_private:
                return

            message = event.message.text.lower()
            
            if any(keyword in message for keyword in self.spam_keywords):
                try:
                    chat = await event.get_chat()
                    
                    if isinstance(chat, Chat):
                        await self.client(DeleteChatUserRequest(chat_id=chat.id, user_id='me'))
                        await self.client(SendMessageRequest(
                            peer=chat.id,
                            message="CeilPrimal bot removed its master from the group because it's sketchy."
                        ))
                        log_message = f'Left group: {chat.title}'
                    elif isinstance(chat, Channel):
                        await self.client(LeaveChannelRequest(chat))
                        log_message = f'Left channel: {chat.title}'
                    
                    self.leave_log.append(log_message)
                    self.activity_log.append(f"[{datetime.now()}] {log_message}")
                    logging.info(log_message)
                    
                except Exception as e:
                    error_message = f'Failed to leave chat: {e}'
                    self.leave_log.append(error_message)
                    self.activity_log.append(f"[{datetime.now()}] {error_message}")
                    logging.error(error_message)

        @self.client.on(events.ChatAction)
        async def handler(event):
            if event.user_added:
                if event.user_id == self.client.get_me().id:
                    chat = await event.get_chat()
                    join_message = f"Bot was added to {chat.title}"
                    self.join_log.append(join_message)
                    self.activity_log.append(f"[{datetime.now()}] {join_message}")
                    logging.info(join_message)
                else:
                    user = await event.get_user()
                    chat = await event.get_chat()
                    add_message = f"{user.first_name} {user.last_name} was added to {chat.title}"
                    self.activity_log.append(f"[{datetime.now()}] {add_message}")
                    logging.info(add_message)
            elif event.user_kicked or event.user_left:
                user = await event.get_user()
                chat = await event.get_chat()
                leave_message = f"{user.first_name} {user.last_name} left or was kicked from {chat.title}"
                self.activity_log.append(f"[{datetime.now()}] {leave_message}")
                logging.info(leave_message)

    async def leave_all_chats(self):
        dialogs = await self.client.get_dialogs()
        total_chats = sum(1 for dialog in dialogs if isinstance(dialog.entity, (Chat, Channel)))
        left_chats = 0

        for dialog in dialogs:
            if isinstance(dialog.entity, (Chat, Channel)):
                try:
                    delay = random.uniform(1, 9)
                    await asyncio.sleep(delay)

                    if isinstance(dialog.entity, Chat):
                        await self.client(DeleteChatUserRequest(chat_id=dialog.id, user_id='me'))
                        await self.client(SendMessageRequest(
                            peer=dialog.id,
                            message="CeilPrimal bot removed its master from the group because it's sketchy."
                        ))
                        log_message = f'Left group: {dialog.title}'
                    elif isinstance(dialog.entity, Channel):
                        await self.client(LeaveChannelRequest(dialog.entity))
                        log_message = f'Left channel: {dialog.title}'
                    
                    left_chats += 1
                    progress = f"Progress: {left_chats}/{total_chats}"
                    self.leave_log.append(f"{log_message} (Delay: {delay:.2f}s) - {progress}")
                    self.activity_log.append(f"[{datetime.now()}] {log_message} (Delay: {delay:.2f}s) - {progress}")
                    logging.info(f"{log_message} (Delay: {delay:.2f}s) - {progress}")
                    
                except Exception as e:
                    error_message = f'Failed to leave chat {dialog.title}: {e}'
                    self.leave_log.append(error_message)
                    self.activity_log.append(f"[{datetime.now()}] {error_message}")
                    logging.error(error_message)

        return f"Attempted to leave all groups and channels. Left {left_chats} out of {total_chats} chats."

    def run_coroutine_threadsafe(self, coroutine):
        return asyncio.run_coroutine_threadsafe(coroutine, self.loop).result()

    def get_logs(self):
        return {
            'leave_log': self.leave_log,
            'join_log': self.join_log,
            'activity_log': self.activity_log
        }
