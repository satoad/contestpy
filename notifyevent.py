import asyncio

class NotifyEvent(asyncio.Event):
    def __init__(self):
        super().__init__()
        self.set_count = 0
        self.calls = 0
        self.ev_call = {}

        self.new_event = asyncio.Event()

    def set(self, name=None):
        self.new_event.set()

        if self.set_count != 0:
            self.clear()

        self.set_count += 1
        self.name = name

        super().set()

    async def wait(self):
        await self.new_event.wait()
        await super().wait()
        self.new_event.clear()
        return self.name

    def call(self, name):
        self.calls += 1
        if name in self.ev_call.keys():
            self.ev_call[name] += 1
        else:
            self.ev_call[name] = 1
        return self.calls - self.ev_call[name]

async def task(name, event):
    while True:
        event_name = await event.wait()
        if event_name is not None:
            if event_name == name:
                total = event.call(name)
                print(f"{name}: {event.ev_call[name]} / {total}")
        else:
            break